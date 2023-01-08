# HW03--I2C and LED Matrix
### Derick Miller



---

## Pins

> 


---

## Files and How to run them

#### setup.sh

> sets up the pins P8_33, P8_35, P8_41, and P8_42 to be in eqep mode to be used by the rotary encoders, you will need to disable the hdmi pins too.

#### tempConversion.sh

> reads in temperatures from the TMP101 sensors from the terminal with i2cget and converts them to farenheit and prints to the terminal

#### tempSense.py

> reads in temperatures from the TMP101 sensors using the smbus on python. prints the values in celsius to the terminal.

#### tempSenseAlert.py

> sets the high and low threshold temperatures, then when ALERT is activated it prints the temperature recorded. NOTE: if it goes above high temperature threshold it will not trigger until it goes to the lower temperature threshold and vice versa

#### game_key.py

> etch-a-sketch on the 8x8 led matrix controlled using keyboard arrow keys, and 'c' to clear

#### game.py

> final version of etch-a-sketch which uses 2 rotary encoders to control the cursor on the LED matrix, and a button to clear the matrix.



---

## Rotary Encoders and Etch-a-Sketch 

>Notes: Ran into a lot of issues with Rotary encoders, but was able to get write example code that prints the count to the terminal. Then I got it to print whether the movement was CW or CCW based on the value of the previous count and the current count. However when you go below zero it loops back and causes a false CW movement so I added a portion that will count up to a target number of CW or CCW events then it will commit to the CW or CCW movement sort of like a debouncer in a way.


# hw03 grading

| Points      | Description | | |
| ----------- | ----------- |-|-|
|  8/8 | TMP101 
|  2/2 |   | Documentation 
|  5/5 | Etch-a-Sketch
|  3/3 |   | setup.sh
|  2/2 |   | Documentation
| 20/20 | **Total**

*My comments are in italics. --may*

*Looks good.*