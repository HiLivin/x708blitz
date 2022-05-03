#!/usr/bin/env python3

import time

from gpiozero import OutputDevice
from gpiozero import CPUTemperature

HIGH_THRESHOLD = 40   # (degrees Celsius) Fan running at high speed at this temperature.
LOW_THRESHOLD = 32  # (degress Celsius) Fan running at low speed  at this temperature.
SLEEP_INTERVAL = 1  # (seconds) How often do we check the core temperature.

FAN_PIN = 16        # Fan speed control pin


if __name__ == '__main__':

  # Validate the on and off thresholds
  if LOW_THRESHOLD >= HIGH_THRESHOLD:
    raise RuntimeError('LOW_THRESHOLD must be less than HIGH_THRESHOLD')

  fan = OutputDevice(FAN_PIN)

  while True:
    temp = int(CPUTemperature().temperature)

    # Switch to high speed fan if the temperature has reached the limit and the fan
    # isn't already running high
    # NOTE: `fan.value` returns 1 for "on" and 0 for "off"
    if temp > HIGH_THRESHOLD and not fan.value:
      fan.on()

    # Switch to low speed if the fan is runnning high and the temperature has dropped
    elif fan.value and temp < LOW_THRESHOLD:
      fan.off()

    time.sleep(SLEEP_INTERVAL)

