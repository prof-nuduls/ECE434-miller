#!/usr/bin/env python3

# game.sh

# Derick Miller
# ECE434 hw01 - Etch-a-Sketch 
# December 7, 2022

# Description: run this in your command prompt and it will open up a game of etch a sketch.

import curses
from curses import wrapper
import time

# curses window setup
def main():
    wrapper(curses_main)

# the actual game and control/input monitoring
def curses_main(screen):
    curses.curs_set(0)

    Welcome(screen)
    max = game(screen)
    printBounds(screen,max)
    x = 0
    y = 0
    screen.addstr(y+1,x+1,"*")
    while True:
        c = screen.getch()
        if c == ord('q'):
            break
        elif c == curses.KEY_UP:
            y -= 1
        elif c == curses.KEY_DOWN:
            y += 1
        elif c == curses.KEY_LEFT:
            x -= 2
        elif c == curses.KEY_RIGHT:
            x += 2
        elif c == ord('c'):
            screen.clear()
            screen.refresh()
        else:
            pass
        
        if (x >= max*2):
            x = max*2 - 2
        if (y >= max):
            y = max - 1
        if (x <= 0):
            x = 0
        if (y <= 0):
            y = 0   
        printBounds(screen,max)
        screen.addstr(y+1,x+1,"*")
        screen.refresh()

    
        

## function definitions

# welcome page
def Welcome(screen):
    screen.addstr(0,0,"HELLO! Welcome to Etch-a-Sketch!")
    screen.refresh()
    time.sleep(2)
    screen.addstr(1,0,"----------------------------------")
    screen.addstr(2,0,"            Instructions          ")
    screen.addstr(3,0,"----------------------------------")
    screen.addstr(4,0,"- begin by choosing the canvas size, when prompted")
    screen.addstr(5,0,"- control your cursor with the arrow keys")
    screen.addstr(6,0,"- clear the canvas by clicking 'c'")
    screen.addstr(7,0,"- exit the game by clicking 'q' ")
    screen.refresh()
    time.sleep(3)
    screen.addstr(10,0,"click SPACE to continue")
    while True:
        c = screen.getch()
        if (c == ord(' ')):
            break
        else:
            pass
    screen.clear()
    screen.refresh()
   

# gets the canvas size 
def game(screen):
    while True:
        try:
            num = game_size = int(get_input(screen,0,0,"type any integer and click enter to determine canvas size e.g. 8 = 8x8: "))
            break

        except ValueError:
            screen.clear()
            screen.addstr(0,0,'Please enter an integer. Try Again.')
            screen.refresh()
            time.sleep(2)
            screen.clear()
            
    screen.addstr(0,0,"\n\ryou have made the canvas {} by {}\n\r".format(game_size,game_size))
    screen.refresh()
    time.sleep(2)
    screen.clear()

    return game_size

# reads users input on curses window 
def get_input(screen, r, c, prompt_string):
    curses.echo() 
    screen.addstr(r, c, prompt_string)
    screen.refresh()
    input = screen.getstr(r + 1, c, 20)
    return input  #       ^^^^  reading input at next line  

#prints the bounds for the game and the instructions
def printBounds(screen,max):
    for i in range(max+2):
        for j in range((2*max)+1):
            if ((i == 0) or (i==max+1)):
                screen.addstr(i,j,"-")
            if ((j == 0) or (j== (2*max))):
                screen.addstr(i,j,"|")
    
    screen.addstr(max+9,0,"            Instructions          ")
    screen.addstr(max+10,0,"- control your cursor with the arrow keys")
    screen.addstr(max+11,0,"- clear the canvas by clicking 'c'")
    screen.addstr(max+12,0,"- exit the game by clicking 'q' ")
                
main()