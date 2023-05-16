#lot  left, but it works! clean up things. going play cod bye.

import machine
import time 
import ntptime
from machine import RTC, Pin, SoftI2C, PWM
import SSD1306 
from insults import catdoing
import framebuf

def scroll_screen_in_out(screen):
  for i in range (0, (oled_width+1)*2, 1):
    for line in screen:
      oled.text(line[2], -oled_width+i, line[1])
    oled.show()
    if i!= oled_width:
      oled.fill(0)

def scroll_in_screen(screen):
  for i in range (0, oled_width+1, 4):
    for line in screen:
      oled.text(line[2], -oled_width+i, line[1])
    oled.show()
    if i!= oled_width:
      oled.fill(0)

def scroll_out_screen(speed):
  for i in range ((oled_width+1)/speed):
    for j in range (oled_height):
      oled.pixel(i, j, 0)
    oled.scroll(speed,0)
    oled.show()

# OLED pin assignment
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 64 # positions 0 - 20 is the yellow display portion
oled = SSD1306.SSD1306_I2C(oled_width, oled_height, i2c)


oled.text('Fuck You', 0, 30) #scroll in? Cat animation?? something, were going play cod instead of this
oled.show()
time.sleep(1)
oled.text('Harvey Dent', 0, 40)
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

catdid = [[0, 30, catdoing]]
insult = scroll_in_screen(catdid) #why is this doing?

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


time.sleep(4)
led3.value(1)
time.sleep(1)
time.sleep(1)
led5.value(1)
time.sleep(1)
led3.value(0)
led5.value(0)

with open('1s.pbm', 'rb') as f:
    f.readline() # Magic number
    f.readline() # Creator comment
    f.readline() # Dimensions
    data = bytearray(f.read())
fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)

oled.invert(0)
oled.blit(fbuf, 0, 20)
oled.show()



while True:
    
    (year, month, day, weekday, hours, minutes, seconds, subseconds) = rtc.datetime()
    feed = f'{hours}{minutes}'
    if len(feed) == 1: # if the hours are between 1 and 9, and :00 minutes it will insert 00
        feed = f'{hours}00'
    elif len(str(minutes)) == 1: ## if the minutes are :0x it will insert the middle 0
        feed = f'{hours}0{minutes}'
    else:
        feed = f'{hours}{minutes}'
       ##todo: This mostly works. Need to adjust to insert zeros on xx0x times

    
    oled.text(feed, 96, 0), oled.show()
    
    # Breakfast 11ish
    if feed == '1030':
        insult
        time.sleep(5)
        print('Calm down, you didnt almost die, heres your breakfast turdbucket.')
        time.sleep(900)                                ## Adjust sleep time to 900 for 15 mins
        print('Yes I know, you get more...')
        print('Here. Now fuck off.')
        led3.value(1)
        time.sleep(50)
        print('Stage 1 complete at:', feed)
        oled.text('420! Dabtime!!', 0, 0)
        oled.show()
        servo.duty(70)
    # Lunch 17ish
    elif feed == '1620': 
        print('ITS FINALLY DINNER...maybe youll shut the fuck up now you bootleg Heathcliff lookin ass..') 
        time.sleep(2)
        print('Ole Thundercats reject.\nMore like thunderthighs.')
        time.sleep(900)                               
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
    elif feed == '2230':
        oled.text('')
        time.sleep(900)
        print('Better make this last all night, no more till the morning idiot.')
        led5.value(1)
        print('Maybe get some thumbs or some new friends to get you more food.')
        time.sleep(50)
        print('Stage 3 complete at:', feed)
        oled.text('Last did it', 0, 50)
        oled.show()
    time.sleep(30)
    oled.fill(0), oled.show() ## todo: change this to just wipe clock 

    ## Maybe a counter added to update time every so often? Or maybe a list with times? try moving time code to boot file, and making a varible feed = localtime(hours, minutes).
    ## maybe insults can come from a list using somthing like 'print(insultlist(random))', then feed cycle can be function