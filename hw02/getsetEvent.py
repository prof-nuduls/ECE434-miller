#!/usr/bin/env python3
# //////////////////////////////////////
#   Derick Miller
#   December 
# 	getsetEvent.py
#   Like getset.py but uses events.
#   Get the value of P8_16 and write it to P9_14. 
#     P8_16 is line 14 on chip 1.  P9_14 is line 18 of chip 1.
# 	Wiring:	Attach a switch to P8_16 and 3.3V and an LED to P9_14.
# 	Setup:	sudo apt uupdate; sudo apt install libgpiod-dev
#           Run: gpioinfo | grep -i -e chip -e P9_14 to find chip and line numbers
# 	See:	https://github.com/starnight/libgpiod-example/blob/master/libgpiod-led/main.c
# //////////////////////////////////////
# Based on https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/tree/bindings/python/examples

import gpiod
import sys

CONSUMER='getset'
CHIP0='0'
CHIP1='1'
getoffsets0=[30,31] # P8_16
setoffests0=[5,4] # P9_14

getoffsets1=[28,18] # P8_16
setoffests1=[16,19] # P9_14



def print_event(event):
    if event.type == gpiod.LineEvent.RISING_EDGE:
        evstr = ' RISING EDGE'
    elif event.type == gpiod.LineEvent.FALLING_EDGE:
        evstr = 'FALLING EDGE'
    else:
        raise TypeError('Invalid event type')

    print('event: {} offset: {} timestamp: [{}.{}]'.format(evstr,
                                                           event.source.offset(),
                                                           event.sec, event.nsec))

chip0 = gpiod.Chip(CHIP0)

getlines0 = chip0.get_lines(getoffsets0)
getlines0.request(consumer=CONSUMER, type=gpiod.LINE_REQ_EV_BOTH_EDGES)

setlines0 = chip0.get_lines(setoffests0)
setlines0.request(consumer=CONSUMER, type=gpiod.LINE_REQ_DIR_OUT)

chip1 = gpiod.Chip(CHIP1)

getlines1 = chip1.get_lines(getoffsets1)
getlines1.request(consumer=CONSUMER, type=gpiod.LINE_REQ_EV_BOTH_EDGES)

setlines1 = chip1.get_lines(setoffests1)
setlines1.request(consumer=CONSUMER, type=gpiod.LINE_REQ_DIR_OUT)


print("Hit ^C to stop")

while True:
    ev_lines0 = getlines0.event_wait()
    ev_lines1 = getlines1.event_wait()
    if ev_lines0:
        for line in ev_lines0:
            event = line.event_read()
            print_event(event)
    vals0 = getlines0.get_values()

    if ev_lines1:
        for line in ev_lines1:
            event = line.event_read()
            print_event(event)
    vals1 = getlines1.get_values()
    #print(vals)
    
    # for val in vals:
    #     print(val, end=' ')
    #print('\r', end='')
    setlines0.set_values(vals1)

    setlines1.set_values(vals0)
