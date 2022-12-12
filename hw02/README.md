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
5. I use about 1.2 % CPU when running the script
6. I experimented with the sleep values and found ...

7. The period is fairly stable with variation of about 1 ms.
8. Once I launch vi the period loses some stability xxx
9. yes?
10. Yes, I find that switching from bash to sh makes the period slightly faster
11. The shortest period I got was found to be xxx ms

---
## Table of GPIO Method Comparison
|method|period|frequency|CPU Usage|
|---|---|---|---|
|bash|42 ms|23.79 Hz||
|Python|186.7 us|5.35kHz||
|C|65.48 us|15.27 kHz||?
|toggle1.py|10.33 us|96.81 kHz||?
|toggle1.c|17.80 us|56.18kHz||?
|toggle2.py|3.79 us|263.53 kHz||?
|toggle2.c|18.37 us|54.438 kHz||?
|toggle2.c|4.41 us|241.38 kHz||?

---
## Security

---
## Updated Etch-a-Sketch
>Notes:
