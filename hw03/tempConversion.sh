#!/bin/sh

while true
do 
    tempC=`i2cget -y 2 0x4a 0` # Temperature in C
    tempF=$((($tempC*9/5) + 32))
    tempC2=`i2cget -y 2 0x49 0` # Temperature in C
    tempF2=$((($tempC2*9/5) + 32))
    printf "tempSensor 1: $tempF °F tempSensor 2: $tempF2 °F\r"
done