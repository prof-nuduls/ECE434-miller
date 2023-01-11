# Homework 4
> Derick Miller
> Date: January 9, 2023

## Memory Map 
## Memory Map

| Block Name  | Start Address (hex)  | End Address (hex) |
|-------------|---------------|-------------|
| GPMC        | 0x00000000    | 0x1FFFFFFF  |
| EMIF0 SDRAM | 0x80000000    | 0xBFFFFFFF  |
| GPIO0       | 0x44E07000    | 0x44E07FFF  |
| UART0       | 0x44E09000    | 0x44E09FFF  |
| I2C0        | 0x44E0B000    | 0x44E0BFFF  |
| UART1       | 0x48022000    | 0x48022FFF  |
| UART2       | 0x48024000    | 0x48024FFF  |
| I2C1        | 0x4802A000    | 0x4802AFFF  |
| McSPI0      | 0x48030000    | 0x48030FFF  |
| GPIO1       | 0x4804C000    | 0x4804CFFF  |
| I2C2        | 0x4819C000    | 0x4809CFFF  |
| McSPI1      | 0x481A1000    | 0x481A1FFF  |
| UART3       | 0x481A6000    | 0x481A6FFF  |
| UART4       | 0x481A8000    | 0x481A8FFF  |
| UART5       | 0x481AA000    | 0x481AAFFF  |
| GPIO2       | 0x481AC000    | 0x481ACFFF  |
| GPIO3       | 0x481AE000    | 0x481AEFFF  |

---

##GPIO via nmap
#### nmap_GPIO.py
> uses 2 switches on GPIO1[18] and GPIO0[30] to toggle USR2 and USR3 LEDs with nmap.
#### nmap_GPIO_Toggle.py 
> This uses GPIO1[28] or P9_12 to toggle as fast as possible while using nmap. I found the period to be 5.19us which I found is faster than than the python gpiod which was 17.80us but still slower than the gpiod in c which was at 3.79us.

---

## i2c via the kernel
#### tempSemse.sh
> reads and then prints to the terminal the temperature off of i2c bus 2 at address 0x49

---

## LED Matrix from browser
#### game.py
> flask app that controls LED matrix on i2c bus 2 and address 0x70. Click buttons UP, DOWN, LEFT, and RIGHT to draw on the Matrix then press clear to erase the board.

---

## LCD 
#### added tux onto the display
 ![](https://github.com/prof-nuduls/ECE434-miller/blob/main/hw04/Images/image1.png) 
   

