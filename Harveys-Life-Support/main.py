#lot  left, but it works! clean up things. going play cod bye.

import machine
import time 
import ntptime
import framebuf
import SSD1306
from machine import RTC, Pin, SoftI2C, PWM
from insults import catdoing
from servo import Servo

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

## Circles
images0 = []###############################################Change for circles
for s in range(1,7):
    with open('circles%s.pbm' % s, 'rb') as q:
        q.readline() # Magic number
        q.readline() # Creator comment
        q.readline() # Dimensions
        data1 = bytearray(q.read())
    fbuf = framebuf.FrameBuffer(data1, 128, 64, framebuf.MONO_HLSB)
    images0.append(fbuf)
with open('circles1.pbm', 'rb') as f:
    f.readline() # Magic number
    f.readline() # Creator comment
    f.readline() # Dimensions
    data = bytearray(f.read())
fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)

def circles():
    r = 0
    while r < 4:
        for i in images0:
            oled.blit(i, 0, 0)
            oled.show()
            time.sleep(0.2)
        r += 1

## Yawns
images = []
for n in range(1,20):
    with open('yawn%s.pbm' % n, 'rb') as f:
        f.readline() # Magic number
        f.readline() # Creator comment
        f.readline() # Dimensions
        data = bytearray(f.read())
    fbuf1 = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)
    images.append(fbuf1)
with open('yawn1.pbm', 'rb') as f:
    f.readline() # Magic number
    f.readline() # Creator comment
    f.readline() # Dimensions
    data = bytearray(f.read())
fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)

def yawns():
    r = 0
    while r < 1:
        for i in images:
            oled.blit(i, 0, 0)
            oled.show()
            time.sleep(.15)
        r += 1

catdid = [[0, 30, catdoing]]

# OLED pin assignment
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 64 # positions 0 - 20 is the yellow display portion
oled = SSD1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Led pin assignment
led3=Pin(14,Pin.OUT)
led4=Pin(27,Pin.OUT)
led5=Pin(26,Pin.OUT)

# Servo
flap=Servo(pin=19)

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

circles() 

## Start intro screen
oled.text('Fuck You', 0, 30) #scroll in? Cat animation?? something, were going play cod instead of this
oled.show()
time.sleep(1)
oled.text('Harvey Dent', 0, 40)
oled.show()
time.sleep(10)
oled.fill(0)
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
       
    oled.text(feed, 96, 0), oled.show()
    
    # Breakfast 11ish
    if feed == '1030':
        oled.text(catdoing, 0, 30)
        oled.show()
        flap.move(70)
        time.sleep(900)
        oled.text(catdoing, 0, 30)
        time.sleep(900)
    # Lunch 17ish
    elif feed == '1620': 
        oled.text('Dabtime!')
        oled.show()
        time.sleep(4)
        oled.fill(0)
        oled.show()
        oled.text(catdoing, 0, 30)
        oled.show()
        flap.move(10)
        time.sleep(900)
        oled.text(catdoing, 0, 30)
        time.sleep(900)
    # Dinner
    elif feed == '2230':
        oled.text(catdoing, 0, 30)
        oled.show()
        flap.move(10)
        time.sleep(900)
        oled.text(catdoing, 0, 30)
        time.sleep(900)
    time.sleep(30)
    yawns()