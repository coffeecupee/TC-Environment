#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <string.h>
#include <time.h>
#include "gpio.h"

#define BUFFER_SIZE 128

int call_gpio_button()
{
    gpio_init();
    gpio_enable(48, 0);
    // 循环
    while (1)
    {
        usleep(100000);
        if (gpio_read(48))
        {
            return 1;
        }
    }
}

void call_program()
{
    printf("open\n");
    pid_t pid = fork();
    if (pid == 0)
    {
        // 子进程调用program
        execlp("./program", "program", NULL);
        exit(0);
    }
    else if (pid > 0)
    {
        wait(NULL);
    }
}

void process_python_output(const char *python_output)
{
    if (strcmp(python_output, "True\n") == 0)
    {
        call_program();
    }
}

void capture_photo()
{
    // 调用client2.py并获取Python脚本的输出
    int python_pipe[2];
    if (pipe(python_pipe) == -1)
    {
        perror("Error creating pipe");
        return;
    }

    pid_t pid = fork();

    if (pid == 0)
    {
        // 子进程
        close(python_pipe[0]); // 关闭读取端

        // 将标准输出重定向到管道的写入端
        dup2(python_pipe[1], STDOUT_FILENO);

        execlp("python3", "python3", "client2.py", NULL);
        exit(0);
    }
    else if (pid > 0)
    {
        // 父进程
        close(python_pipe[1]); // 关闭写入端

        char python_output[BUFFER_SIZE];
        ssize_t bytes_read = read(python_pipe[0], python_output, sizeof(python_output) - 1);
        if (bytes_read > 0)
        {
            python_output[bytes_read] = '\0';
            // printf("Received Python output: %s\n", python_output);
            process_python_output(python_output);
        }

        wait(NULL);
    }
}

int main()
{
    while (1)
    {
        printf("waitting...\n");
        if (call_gpio_button() == 1)
        {
            printf("Input\n");
            capture_photo();
            sleep(2);
        }

        sleep(1);
    }

    return 0;
}
