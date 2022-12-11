#!/usr/bin/python 
# togglegpio.py

# Derick Miller
# December 10, 2022
# Description: Blinks an LED on P9_15 as fast as possible

import time
import os

# P9.15 is 48
pin = "48"
GPIOPATH = '/sys/class/gpio/'

# Make sure pin is exported
if (not os.path.exists(GPIOPATH+"gpio"+pin)):
    f = open(GPIOPATH+"export","w")
    f.write(pin)
    f.close()

# Make it an output pin
f = open(GPIOPATH+"gpio"+pin+"/direction","w")
f.write("out")
f.close()

f = open(GPIOPATH+"gpio"+pin+"/value","w")
# Blink
while True:
    f.seek(0)
    f.write("1")
    time.sleep(0.5)

    f.seek(0)
    f.write("0")
    time.sleep(0.5)
f.close()


