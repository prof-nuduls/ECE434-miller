#!/usr/bin/env python3
# Reading a TMP101 Sensor

import smbus
import gpiod
import time
#Derick Miler
# December 20, 2022
# Uses I2C smbus to configure the TMP101 sensors in to interrupt mode
# sets the T high and T low registers and whenever a temperature is 
# below the low level or above the high level it sends a 1 on the GPIO pin
# and then prints the value to the terminal when detected

# NOTE: it will send a one once it goes below or above the temperature the first time
# however, it will not send another interrupt unless it does the opposite of what it first detected
# e.g. temp goes above 27 C it won't send a interrupt unless it goes below the low level temp 23 in this case


# Initialize the I2C bus
bus = smbus.SMBus(2)

# Initialize the GPIO chip and lines
chip = gpiod.Chip('0')
lines = chip.get_lines([3, 2])
lines.request(consumer='Temp Sensor', type=gpiod.LINE_REQ_EV_BOTH_EDGES)
thigh = 27
tlow = 23
# Set up the sensors
# Address 0x4a
bus.write_byte_data(0x4a, 1, 0b11100110)
bus.write_byte_data(0x4a, 2, tlow) #Set low temperature limit to 23 Celsius
bus.write_byte_data(0x4a, 3, thigh)  # Set high temperature limit to 25 Celsius

# Address 0x49
bus.write_byte_data(0x49, 1, 0b11100110) 
bus.write_byte_data(0x49, 2, tlow)  # Set low temperature limit to 23 Celsius
bus.write_byte_data(0x49, 3, thigh)  # Set high temperature limit to 27 Celsius

while True:
    # Check for alerts on the GPIO lines
    vals = lines.get_values()
    if vals[0] == 1:
        # Alert on P9_21
        data = bus.read_byte_data(0x4a, 0)
        print(f" ALERT Temperature: {data} Celsius")
    if vals[1] == 1:
        # Alert on P9_22
        data = bus.read_byte_data(0x49, 0)
        print(f"ALERT 1 Temperature: {data} Celsius")
    time.sleep(0.25)
    print("non")
