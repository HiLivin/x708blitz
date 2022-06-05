#!/usr/bin/env python

import struct
import smbus
import sys
import subprocess

from gpiozero import InputDevice

MIN_VOLTAGE = 4.0   # (volts) shutdown when voltage drops below this value

PLD_PIN = 6         # Power loss detection pin


def readVoltage(bus):

  address = 0x36
  read = bus.read_word_data(address, 2)
  swapped = struct.unpack("<H", struct.pack(">H", read))[0]
  voltage = swapped * 1.25 / 1000 / 16
  return voltage


def readCapacity(bus):

  address = 0x36
  read = bus.read_word_data(address, 4)
  swapped = struct.unpack("<H", struct.pack(">H", read))[0]
  capacity = swapped/256
  if capacity > 100:
     capacity = 100
  return capacity


bus = smbus.SMBus(1)

status = ""
voltage = readVoltage(bus)
capacity = readCapacity(bus)
pld = InputDevice(PLD_PIN).value

if pld:
  status = "ONBATT"
else:
  status = "ONLINE"

# software shutdown when AC is off and battery voltage LOW
if pld and (voltage < MIN_VOLTAGE):
  status = "SHUTTING DOWN"
  subprocess.Popen("/usr/local/bin/x708softsd.sh", shell=True)

print("{},{:.2f}V|{:.0f}%%,".format(status,voltage,capacity))

