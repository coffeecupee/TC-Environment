#define MAP_SIZE 0x1000
#define REG_BASE 0x1fe00000
#define GPIO_EN 0x500
#define GPIO_OUT 0x510
#define GPIO_IN 0x520

extern unsigned char *map_base;
//init
int gpio_init(void);
int gpio_enable(int gpio_num,int val);
int gpio_close(void);
int gpio_write(int gpio, int val);
int gpio_read(int gpio_num);
