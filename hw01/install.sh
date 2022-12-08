#!/usr/bin/env python3

#import curses

# demo-ncurses-hello-world.py

import curses
from curses import wrapper
import sys

def main():
    wrapper(curses_main)


def curses_main(stdscr):
    Welcome(stdscr)
    game(stdscr)

    while True:
        c = stdscr.getch()
        if c == ord('q'):
            break
        elif c == curse.KEY_UP:
            y -= 1
        elif c == curse.KEY_DOWN:
            y += 1
        elif c == curse.KEY_LEFT:
            x -= 1
        elif c == curse.KEY_RIGHT:
            x += 1

        
        

## function definitions
def Welcome(stdscr):
    stdscr.addstr(0,0,"\nHELLO! Welcome to Etch-a-Sketch!\n\r")
    stdscr.addstr(0,0,"----------------------------------\n\r")
    stdscr.addstr(0,0,"            Instructions          \n\r")
    stdscr.addstr(0,0,"begin by choosing the canvas size, then choose your start position\n\r")
    stdscr.addstr(0,0,"then the game will begin and you can move your cursor\n\n\r")
    stdscr.refresh()

def game(stdscr):
    game_size = int(get_input(stdscr,0,0,"enter any integer to determine canvas size e.g. 8 = 8x8: "))

    stdscr.addstr(0,0,"\n\ryou have made the canvas {} by {}\n\r".format(game_size,game_size))
    stdscr.refresh()


    x,y = get_input(stdscr,3,0,"where do you want to start? e.g. 0,0 for (0,0):  ").split(",")
    x = int(x)
    y = int(y)
    stdscr.refresh()

    while(1):
        stdscr.refresh()
        if (x <= game_size and y <= game_size):
            stdscr.addstr(0,0,"\n\ryou are starting at ({},{})\n\r".format(x,y))
            break
        else:
            stdscr.addstr(0,0,"\n\r that is not a possible starting point!\n\r\n")
            x,y = get_input(stdscr,0,0,"where do you want to start? e.g. 0,0 for (0,0):  ").split(",")
            x = int(x)
            y = int(y)
    return game_size,x,y
    
def get_input(stdscr, r, c, prompt_string):
    curses.echo() 
    stdscr.addstr(r, c, prompt_string)
    stdscr.refresh()
    input = stdscr.getstr(r + 1, c, 20)
    return input  #       ^^^^  reading input at next line  

main()