# HW02--GPIO Speed
### Derick Miller

---
## Buttons and LEDs
> I used pins P9_11 through P9_18 on the Beagle Bone Black. Where P9_11 through P9_14 were used for push buttons, wired one side to 3.3V and the other to a pull down resistor and the other side to the GPIO pin. Then P9_15 through P9_18 were used for LEDs, wired one side to a current-limiting resistor to GND and the other to the GPIO pin.

---
## Files and How to run them
#### game_gpiod.sh
> run in the command window, utilizes the buttons on P9_11 through P9_14 and these control the cursor to draw on the screen. There isn't a clear button yet, I was too lazy to add another button. Ctrl + C to quit.
#### togglegpio.sh
> script file to toggle gpio pin, run in cmd line followed by GPIO number and period. (may need to uncomment the sleep line)
#### togglegpio.py
> direct method of toggling gpio pin with python
#### getsetEvent.py
> gets events from the buttons P9_11 through P9_14 and outputs the results onto the LEDs on P9_15 through P9_18
#### togglepin
> this is the compiled file of togglegpio.c, which uses lseek() to directly toggle a gpio pin. run in cmd line followed by period. (may need to uncomment the sleep line)
#### toggle1
> this is the compiled version of the toggle1.c, which uses C and gpiod to toggle a gpio pin.
#### toggle2
> this is the compiled version of the toggle2.c, which uses C and gpiod to toggle 2 gpio pins.
#### toggle1.py
> uses python and gpiod to toggle a gpio pin.
#### toggle2.py
> uses python and gpiod to toggle 2 gpio pins.




---
## Measuring a GPIO pin on an Oscilloscope
1. I find the min voltage to be -40mV, and the max voltage to be around 3.36V.
2. The period was 242.8 ms and the frequency 4.119 Hz.
3. it is 142.8 ms away from 100ms.
4. They differ because other processes on the chip slow and can interrupt the program.
5. I use about 2.0 % CPU when running the script
6. I experimented with the sleep values and found 

|sleep time|period|CPU Usage|
|---|---|---|
|0.1|242.18ms|2.0 %|
|0.01|49.67ms|8.8 %|
|0.001|31.93 ms|14.7 %|
|0|29.85 ms|14.2%|
|0 clean| 17.83 ms|18.2%|



7. The period is fairly stable with variation of about 1 ms.
8. Once I launch vi the period loses some stability and variations can reach up to 10ms or more at times
9. Yes after removing a few lines that were not needed I found that the period improved significantly from 29.85ms to 17.83ms once cleaned.
10. Yes, I find that switching from bash to sh makes the period slightly faster, but not a large amount faster for sleep of 0.1 it improved to 230ms from the 242 ms, and at the cleaned file for the fastest time the time for bash was 25ms vs the 17.83ms found using sh.
11. The shortest period I got was found to be 17.83 ms.

---
## Python
1. The period was 65.48 us and the frequency was 15.27kHz
2. I found that this was using 95 % of my CPU

---
## Table of GPIO Method Comparison
|method|period|frequency|CPU Usage|
|---|---|---|---|
|sh|17.83ms|56.09 Hz|18.2 %|
|Python|65.48 us|15.27 kHz|95%|
|C|10.33 us|96.81 kHz|98.1 %|
|toggle1.py|17.80 us|56.18kHz|96.8 %|
|toggle1.c|3.79 us|263.53 kHz|98.1 %|
|toggle2.py|18.37 us|54.438 kHz|97.5 %|
|toggle2.c|4.41 us|241.38 kHz|98.1%|

---
## getsetEvent.py
works

---
## Security
1. ![changed name of port 22](https://github.com/prof-nuduls/ECE434-miller/blob/main/hw02/images/port_num.PNG) 
   changed name of port 22
3. ![created a fail2ban server](https://github.com/prof-nuduls/ECE434-miller/blob/main/hw02/images/fail2ban_start.PNG) 
   created a fail2ban server
---
## Updated Etch-a-Sketch
>Notes: ran into a lot of issues with retrieving values, found this to be due to curses.getch() looking for input through both gpiod and curses window shown not to work well together but overall went well.


# hw02 grading

| Points      | Description |
| ----------- | ----------- |
|  2/2 | Buttons and LEDs 
|  8/8 | Etch-a-Sketch works
|      | Measuring a gpio pin on an Oscilloscope 
|  2/2 | Questions answered
|  4/4 | Table complete
|  2/2 | gpiod
|      | Security
|  1/1 | ssh port | I assume you mean port 2022
|  1/1 | fail2ban
| 20/20   | **Total**

(Demo your etch-a-sketch and I'll give some points back.)

Sorry about that I forgot to record your demo.  It's fixed now.