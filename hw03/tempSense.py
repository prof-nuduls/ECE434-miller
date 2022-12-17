#!/usr/bin/env python3
# Reading a TMP101 Sensor

import smbus
import time
import gpiod 

CONSUMER='get'
CHIP='0'
getoffsets=[3,2] # P9_21, P9_22

chip = gpiod.Chip(CHIP)
getlines = chip.get_lines(getoffsets)
getlines.request(consumer=CONSUMER, type=gpiod.LINE_REQ_EV_BOTH_EDGES)

## I2C Bus for TMP101 Sensors
bus = smbus.SMBus(2)
address = 0x4a
address1 = 0x49

setLow = int(input('Pick a low temp threshold:'))
setHigh = int(input('Pick a high temp threshold:'))
setLow1 = int(input('Pick a low temp threshold:'))
setHigh1 = int(input('Pick a high temp threshold:'))

bus.write_byte_data(address,2,setLow)
bus.write_byte_data(address,3,setHigh)
bus.write_byte_data(address1,2,setLow1)
bus.write_byte_data(address1,3,setHigh1)
bus.write_byte_data(address,1,2)
bus.write_byte_data(address1,1,2)
while True:
    vals = getlines.get_values()
    if (vals[0] == 1):
        temp=`i2cget -y 2 0x4a 01`
        print("Sensor 1: ",temp, end="\r")
    if(vals[1]==1):
        temp1=`i2cget -y 2 0x49 01`
        print("Sensor 2: ",temp1, end="\r")
    print(vals, end = "\r")

    time.sleep(0.25)