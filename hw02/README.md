# HW02--GPIO Speed
### Derick Miller

---
## Buttons and LEDs
> I used pins P9_11 through P9_18 on the Beagle Bone Black. Where P9_11 through P9_14 were used for push buttons, wired one side to 3.3V and the other to a pull down resistor and the other side to the GPIO pin. Then P9_15 through P9_18 were used for LEDs, wired one side to a current-limiting resistor to GND and the other to the GPIO pin.

---
## Measuring a GPIO pin on an Oscilloscope
1. I find the min voltage to be nearly 0, and the max voltage to be around 3.2 to 3.3V.
2. The period was 212ms and the frequency __ Hz.
3. This is quite a bit farther away from 100ms than I expected it to be.
4. They differ because opening and closing a file every cycle is really slow
5. I use about __ % CPU when running the script
6. I experimented with the sleep values and found ...
7. The period is fairly stable with ...
8. Once I launch vi the period loses some stability xxx
9. yes?
10. Yes, I find that switching from bash to sh makes the period slightly faster
11. The shortest period I got was found to be xxx ms

---
## Table of GPIO Method Comparison
|method|period|frequency|CPU Usage|
|---|---|---|---|
|Python||||
|C||||
|toggle1.py||||
|toggle1.c||||
|toggle2.py||||
|toggle2.c||||

---
## Security

---
## Updated Etch-a-Sketch
>Notes:
