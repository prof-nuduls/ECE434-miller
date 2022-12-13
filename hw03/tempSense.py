#!/usr/bin/env python3
# Reading a TMP101 Sensor

import smbus
import time
bus = smbus.SMBus(2)
address = 0x4a

while True:
    temp = bus.read_byte_data(address, 0)
    print(temp, end="\r")
    time.sleep(0.25)