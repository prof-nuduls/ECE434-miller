#!/usr/bin/env python3

import gpiod
import sys
import time
import smbus

from flask import Flask, render_template, request
app = Flask(__name__)
bus = smbus.SMBus(2)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70

bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

# The first byte is GREEN, the second is RED.
game = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
]
bus.write_i2c_block_data(matrix, 0, game)
max = 8
x = 0
y = 0

game[15-x] += 0x01
game[14-x] += 0x01
bus.write_i2c_block_data(matrix, 0, game)

#initialize GPIO status variable
DownSts = 0
UpSts = 0
LeftSts = 0
RightSts = 0
def update():
    bus.write_i2c_block_data(matrix, 0, game)
    
@app.route("/")
def index():
	# Read Sensors Status
    DownSts = '0'
    UpSts = '0'
    LeftSts = '0'
    RightSts = '0'
    templateData = {
                'title' : 'Etch-a-Sketch',
                'Down'  : DownSts,
                'Up'  : UpSts,
                'Left'  : LeftSts,
                'Right'  : RightSts,
        }
    return render_template('index.html', **templateData)

@app.route("/<action>")
def action(action):
    DownSts = '0'
    UpSts = '0'
    LeftSts = '0'
    RightSts = '0'
    clear = '0'
    max = 8
    global x
    global y
    
    
    if action == "DownOn":
        DownSts = '1'
        y += 1
        if (y >= max):
            y = max -1
        for i in range (8):
            game[i*2+1] = game[i*2+1] & 0x00
        game[15-x] = game[15-x] | 2**y
        game[14-x] = game[14-x] | 2**y
        update()
        DownSts = '0'

    if action == "UpOn":
        UpSts = '1'
        y -= 1
        if (y <= 0):
            y = 0   
        for i in range (8):
            game[i*2+1] = game[i*2+1] & 0x00
        game[15-x] = game[15-x] | 2**y
        game[14-x] = game[14-x] | 2**y
        update()
        UpSts = '0'

    if action == "LeftOn":
        LeftSts = '1'
        x -= 2
        if (x <= 0):
            x = 0
        for i in range (8):
            game[i*2+1] = game[i*2+1] & 0x00
        game[15-x] = game[15-x] | 2**y
        game[14-x] = game[14-x] | 2**y
        update()
        LeftSts = '0'
        
    if action == "RightOn":
        RightSts = '1'
        x += 2
        if (x >= 2*max):
            x = 2*max -2
        for i in range (8):
            game[i*2+1] = game[i*2+1] & 0x00
        game[15-x] = game[15-x] | 2**y
        game[14-x] = game[14-x] | 2**y
        update()
        RightSts = '0'    
    if action == 'Clear':
        for i in range (len(game)):
            game[i] = game[i] & 0x00
        update()
                
    templateData = {
                'Down'  : DownSts,
                'Up'  : UpSts,
                'Right'  : RightSts,
                'Left'  : LeftSts,
                'Clear': clear,
    }
    return render_template('index.html', **templateData)
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8081, debug=True)

