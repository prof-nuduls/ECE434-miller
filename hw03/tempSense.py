#!/usr/bin/env python3
# Reading a TMP101 Sensor

import smbus
import time
import gpiod 

#Derick Miler
# December 20, 2022
# Uses I2C smbus to read in the temperature from two TMP101 sensors in 
# Celsius and then print it out to the terminal

## I2C Bus for TMP101 Sensors
bus = smbus.SMBus(2)
address = 0x4a
address1 = 0x49

while True:
    temp=bus.read_byte_data(address,0)
    temp1=bus.read_byte_data(address1,0)
    print("Sensor 1: ", temp, "°C","Sensor 2: ",temp1,"°C" ,end="\r")

    time.sleep(0.25)
