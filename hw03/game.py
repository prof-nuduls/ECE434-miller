#!/usr/bin/env python3
import time
import smbus
import gpiod

eQEP = '2'
COUNTERPATH = '/dev/bone/counter/'+eQEP+'/count0'
eQEP1 = '1'
COUNTERPATH1 = '/dev/bone/counter/'+eQEP1+'/count0'

ms = 75
maxCount = '1000000'

f = open(COUNTERPATH+'/ceiling','w')
f.write(maxCount)
f.close()
f = open(COUNTERPATH1+'/ceiling','w')
f.write(maxCount)
f.close()

f = open(COUNTERPATH+'/enable','w')
f.write('1')
f.close()
f = open(COUNTERPATH1+'/enable','w')
f.write('1')
f.close()

bus = smbus.SMBus(2)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70

delay = 1; # Delay between images in s

bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

# The first byte is GREEN, the second is RED.
game = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
game_init = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
bus.write_i2c_block_data(matrix, 0, game)

f = open(COUNTERPATH+'/count','r')
f1 = open(COUNTERPATH1+'/count','r')

olddata = -1
olddata1 = -1

f.seek(0)
prev_count = f.read()[:-1]
ccw_count = 0
cw_count = 0
target = 3


f1.seek(0)
prev_count1 = f1.read()[:-1]
ccw_count1 = 0
cw_count1 = 0
L = ''
R = ''
max = 8
x = 0
y = 0
game[15-x] += 0x01
game[14-x] += 0x01
bus.write_i2c_block_data(matrix, 0, game)
CONSUMER='getset'
CHIP1='0'
getoffsets1=[30] 

chip1 = gpiod.Chip(CHIP1)
getlines1 = chip1.get_lines(getoffsets1)
getlines1.request(consumer=CONSUMER, type=gpiod.LINE_REQ_EV_BOTH_EDGES)
while True:
    f.seek(0)
    data = f.read()[:-1]
    if data != olddata:
            # Compare the current count to the previous count to determine the direction of rotation
        if data > prev_count:
            ccw_count += 1
        elif data < prev_count:
            cw_count += 1
    if (ccw_count >= target or cw_count >= target):
        if (ccw_count >= target):
            R = "CW"
        else:
            R = "CCW"
        ccw_count = 0
        cw_count = 0
    prev_count = data


    f1.seek(0) 
    data1 = f1.read()[:-1]   

    if data1 != olddata1:
            # Compare the current count to the previous count to determine the direction of rotation
        if data1 > prev_count1:
            ccw_count1 += 1
        elif data1 < prev_count1:
            cw_count1 += 1
    if (ccw_count1 >= target or cw_count1 >= target):
        if (ccw_count1 >= target):
            L = 'CCW'
        else:
            L = 'CW'

        ccw_count1 = 0
        cw_count1 = 0
    vals1 = getlines1.get_values()
    if vals1[0] == 1:
        for i in range (len(game)):
            game[i] = game[i] & 0x00
    elif R == 'CCW':
        y -= 1
        if (y <= 0):
            y = 0   
        for i in range (8):
            game[i*2+1] = game[i*2+1] & 0x00
        game[15-x] = game[15-x] | 2**y
        game[14-x] = game[14-x] | 2**y

    elif R == 'CW':
        y += 1
        if (y >= max):
            y = max -1
        for i in range (8):
            game[i*2+1] = game[i*2+1] & 0x00
        game[15-x] = game[15-x] | 2**y
        game[14-x] = game[14-x] | 2**y
    elif L == 'CCW':
        x -= 2
        if (x <= 0):
            x = 0
        for i in range (8):
            game[i*2+1] = game[i*2+1] & 0x00
        game[15-x] = game[15-x] | 2**y
        game[14-x] = game[14-x] | 2**y
    elif L == 'CW':
        x += 2
        if (x >= 2*max):
            x = 2*max -2
        for i in range (8):
            game[i*2+1] = game[i*2+1] & 0x00
        game[15-x] = game[15-x] | 2**y
        game[14-x] = game[14-x] | 2**y
    

    bus.write_i2c_block_data(matrix, 0, game)
    R = ''
    L = ''
    prev_count1 = data1
    time.sleep(ms/1000)

