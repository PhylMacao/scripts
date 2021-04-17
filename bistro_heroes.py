#!/usr/bin/env python3

from ppadb.client import Client
import time

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

button1_x= 1376
button1_y = 165
slide1_x = 800
slide1_y = 550
slide2_x = 1170
slide2_y = 550
button2_x = 870
button2_y = 775


if len(devices) == 0:
    print("No device attached!")
    quit()

while True:
    device = devices[0]
    device.shell("input tap " + str(button1_x) + " " + str(button1_y))
    time.sleep(1)
    device.shell("input touchscreen swipe " + str(slide1_x) + " " + str(slide1_y) + " " + str(slide2_x) + " " + str(slide2_y) + " 500")
    time.sleep(1)
    device.shell("input touchscreen tap " + str(button2_x) + " " + str(button2_y))
    time.sleep(0.1)
    device.shell("input touchscreen tap 850 700")
    time.sleep(0.1)
    device.shell("input touchscreen tap 500 500")
    time.sleep(0.1)
    device.shell("input touchscreen tap 500 500")

# image = device.screencap()
# with open('screen.png', 'wb') as f:
#     f.write(image)