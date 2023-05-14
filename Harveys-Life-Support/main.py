#lot  left, but it works! clean up things. going play cod bye.

import machine
import time 
import ntptime
from machine import RTC, Pin, SoftI2C, PWM
import SSD1306 

# OLED pin assignment
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 64 # positions 0 - 20 is the yellow display portion
oled = SSD1306.SSD1306_I2C(oled_width, oled_height, i2c)


oled.text('Fuck Harvey Dent', 0, 50)
oled.show()
time.sleep(10)
oled.fill(0)
oled.show()

# Led pin assignment
led3=Pin(14,Pin.OUT)
led4=Pin(27,Pin.OUT)
led5=Pin(26,Pin.OUT)

# Servo
servo = PWM(Pin(19))
servo.freq(50)

# Time shit
rtc = RTC()

ntptime.settime()
(year, month, day, weekday, hours, minutes, seconds, subseconds) = rtc.datetime()

sec = ntptime.time()
timezone_hour = -5
timezone_sec = timezone_hour * 3600
sec = int(sec + timezone_sec)
(year, month, day, hours, minutes, seconds, weekday, yearday) = time.localtime(sec)
rtc.datetime((year, month, day, 0, hours, minutes, seconds, 0))



time.sleep(1)
led3.value(1)
time.sleep(1)
time.sleep(1)
led5.value(1)
time.sleep(3)
led3.value(0)
led5.value(0)

while True:
    
    (year, month, day, weekday, hours, minutes, seconds, subseconds) = rtc.datetime()
    feed = f'{hours}{minutes}'
    print(feed)
    
    # Breakfast 11ish
    if feed == '510':
        print('Did you make it though the night?') # motor code goes here, not print statement, should also be a function.  
        time.sleep(5)
        print('Calm down, you didnt almost die, heres your breakfast turdbucket.')
        time.sleep(120)                                ## Adjust sleep time to 900 for 15 mins
        print('Yes I know, you get more...')
        print('Here. Now fuck off.')
        led3.value(1)
        time.sleep(50)
        print('Stage 1 complete at:', feed)
        oled.text('420! Dabtime!!', 0, 0)
        oled.show()
        servo.duty(70)
    # Lunch 17ish
    elif feed == '635': 
        print('ITS FINALLY DINNER...maybe youll shut the fuck up now you bootleg Heathcliff lookin ass..') 
        time.sleep(2)
        print('Ole Thundercats reject.\nMore like thunderthighs.')
        time.sleep(120)                                 ## Adjust to 900
        print('Heres the rest.')
        led4.value(1)
        print('Honestly. Youre a disapointment.')
        time.sleep(10)
        print('Im sure that food tastes like sadness.')
        time.sleep(50)
        print('Stage 2 complete at:', feed)
        oled.text('Second did it, also', 0, 30)
        oled.show()
    # Dinner
    elif feed == '757':
        print('Oh dinner time? Worked up quite a hunger today Im sure.')
        print('Lots of bug watching and licking your dick I\'m  sure.') 
        time.sleep(120)
        print('Better make this last all night, no more till the morning idiot.')
        led5.value(1)
        print('Maybe get some thumbs or some new friends to get you more food.')
        time.sleep(50)
        print('Stage 3 complete at:', feed)
        oled.text('Last did it', 0, 50)
        oled.show()
    time.sleep(30)
   

    ## Maybe a counter added to update time every so often? Or maybe a list with times? try moving time code to boot file, and making a varible feed = localtime(hours, minutes).
    ## maybe insults can come from a list using somthing like 'print(insultlist(random))', then feed cycle can be function