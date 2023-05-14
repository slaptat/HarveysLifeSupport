# boot.py -- run on boot-up

import network


sta_if = network.WLAN(network.STA_IF)

x = 0
if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.active(True)
    sta_if.connect("__Hell_Hole__", "1Ky9An9Re0")
    while not sta_if.isconnected():
        x += 1
        pass
    print('network config:', sta_if.ifconfig())
if x == 5:
    print('Starting offline.')
    exec(open("main.py"))