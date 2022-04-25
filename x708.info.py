#!/usr/bin/env python

import struct
import smbus
import sys
import subprocess
import RPi.GPIO as GPIO

MIN_VOLTAGE = 4.0         # (volts) shutdown when voltage drops below this value

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN)    # PLD pin, high when the AC power loss is detected
GPIO.setup(13, GPIO.OUT)  # shutdown pin


def readVoltage(bus):

  address = 0x36
  read = bus.read_word_data(address, 2)
  swapped = struct.unpack("<H", struct.pack(">H", read))[0]
  voltage = swapped * 1.25 / 1000 / 16
  return voltage


bus = smbus.SMBus(1)

status = ""
voltage = readVoltage(bus)
pld = GPIO.input(6)

GPIO.cleanup()

if pld:
  status = "ONBATT"
else:
  status = "ONLINE"

# software shutdown when AC is off and battery voltage LOW
if pld and (voltage < MIN_VOLTAGE):
  status = "SHUTTING DOWN"
  subprocess.Popen("/usr/local/bin/x708softsd.sh", shell=True)

print(status + "," + "{:.2f}".format(voltage) + "V,")

