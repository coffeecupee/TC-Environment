#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include "gpio.h"

int main(void){
	printf("我亮了");
	// 初始化 gpio
	gpio_init();
	// 使能为输出模式
	gpio_enable(45,1);
	//gpio_enable(46,1);
	// 循环
	gpio_write(45,1);
	//gpio_write(46,1);
	sleep(10);
	gpio_write(45,0);
	//gpio_write(46,0);
	printf("我bu亮了");
	return 0;
}
