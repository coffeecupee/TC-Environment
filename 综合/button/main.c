#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include "gpio.h"

int main(void){

	// 初始化 gpio
	gpio_init();
	gpio_enable(48,0);


	// 循环
	while(1)
	{
		usleep(100000);
		
    if(gpio_read(48)){
      printf("%d",gpio_read(48));
      break;
    }
	}
}

