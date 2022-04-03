#!/usr/bin/env python
import struct
import smbus
import sys
import time
import RPi.GPIO as GPIO

SLEEP_INTERVAL = 10  # (seconds) How often we check the battery status
MIN_VOLTAGE = 3.0	# (volts) Shutdown when voltage drops below this value

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
GPIO.setwarnings(False)

def readVoltage(bus):

     address = 0x36
     read = bus.read_word_data(address, 2)
     swapped = struct.unpack("<H", struct.pack(">H", read))[0]
     voltage = swapped * 1.25 /1000/16
     return voltage


def readCapacity(bus):

     address = 0x36
     read = bus.read_word_data(address, 4)
     swapped = struct.unpack("<H", struct.pack(">H", read))[0]
     capacity = swapped/256
     return capacity


bus = smbus.SMBus(1)

while True:

 print ("******************")
 print ("Voltage:%5.2fV" % readVoltage(bus))
 print ("Capacity:%5i%%" % readCapacity(bus))

#Set battery low voltage to shut down
 if readVoltage(bus) < MIN_VOLTAGE:

         print ("Battery LOW!!!")
         print ("Shutdown in 5 seconds")
         time.sleep(5)
         GPIO.output(13, GPIO.HIGH)
         time.sleep(3)
         GPIO.output(13, GPIO.LOW)

 time.sleep(SLEEP_INTERVAL)

