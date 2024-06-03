# 交叉编译器路径
CC = /home/gcl/kunm/loongarch64/loongarch64-linux-gnu-2021-12-10-vector/bin/loongarch64-linux-gnu-gcc

# 编译选项
CFLAGS = -Wall -O2

# 目标文件
TARGET = program

# 源文件列表
SRCS = main.c gpio.c

# 对应的目标文件列表
OBJS = $(SRCS:.c=.o)

# 默认目标
all: $(TARGET)

# 生成可执行文件
$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $@ $^

# 编译每个源文件为目标文件
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# 清理生成的文件
clean:
	rm -f $(OBJS) $(TARGET)

