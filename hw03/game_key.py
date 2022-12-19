#!/usr/bin/env python3

# game.sh

# Derick Miller
# ECE434 hw01 - Etch-a-Sketch 
# December 7, 2022

# Description: run this in your command prompt and it will open up a game of etch a sketch.

import curses
from curses import wrapper
import time
#!/usr/bin/env python3
# Write an 8x8 Red/Green LED matrix
# https://www.adafruit.com/product/902

import smbus
import time
bus = smbus.SMBus(2)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70

delay = 1; # Delay between images in s

bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

# The first byte is GREEN, the second is RED.
game = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
]


bus.write_i2c_block_data(matrix, 0, game)

# curses window setup
def main():
    wrapper(curses_main)

# the actual game and control/input monitoring
def curses_main(screen):
    curses.curs_set(0)

   
    max = 8
    x = 0
    y = 0

    game[15-x] += 0x01
    bus.write_i2c_block_data(matrix, 0, game)
    while True:
        c = screen.getch()
        if c == ord('q'):
            break
        elif c == curses.KEY_UP:
            y -= 1
            if (y <= 0):
                y = 0   
            game[15-x] = game[15-x] | 2**y
        elif c == curses.KEY_DOWN:
            y += 1
            if (y >= max):
                y = max -1
            game[15-x] = game[15-x] | 2**y
        elif c == curses.KEY_LEFT:
            x -= 2
            if (x <= 0):
                x = 0
            game[15-x] = game[15-x] | 2**y
        elif c == curses.KEY_RIGHT:
            x += 2
            if (x >= 2*max):
                x = 2*max -2
            game[15-x] = game[15-x] | 2**y
        elif c == ord('c'):
            for i in range (len(game)):
                game[i] = game[i] & 0x00
        else:
            pass
        bus.write_i2c_block_data(matrix, 0, game)
        screen.refresh()

    
    
                
main()