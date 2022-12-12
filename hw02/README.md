# HW02--GPIO Speed
### Derick Miller

---
## Buttons and LEDs
> I used pins P9_11 through P9_18 on the Beagle Bone Black. Where P9_11 through P9_14 were used for push buttons, wired one side to 3.3V and the other to a pull down resistor and the other side to the GPIO pin. Then P9_15 through P9_18 were used for LEDs, wired one side to a current-limiting resistor to GND and the other to the GPIO pin.

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
## Security

---
## Updated Etch-a-Sketch
>Notes:
