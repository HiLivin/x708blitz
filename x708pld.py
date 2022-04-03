#!/usr/bin/env python
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN)

def my_callback(channel):
    if GPIO.input(6):     # if port 6 == 1
        print ("---AC Power Loss OR Power Adapter Failure---")
    else:                  # if port 6 != 1
        print ("---AC Power OK,Power Adapter OK---")

GPIO.add_event_detect(6, GPIO.BOTH, callback=my_callback, bouncetime=500)

print ("1.Make sure your power adapter is connected")
print ("2.Disconnect and then connect the power adapter again to test")
print ("3.When power adapter disconnected, you will see: AC Power Loss or Power Adapter Failure")
print ("4.When power adapter reconnected, you will see: AC Power OK, Power Adapter OK")

input("Testing Started")

