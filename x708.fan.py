#!/usr/bin/env python3

import time

from gpiozero import OutputDevice
from gpiozero import CPUTemperature

ON_THRESHOLD = 40	# (degrees Celsius) Fan running at high speed at this temperature.
OFF_THRESHOLD = 32	# (degress Celsius) Fan running at low speed  at this temperature.
SLEEP_INTERVAL = 1	# (seconds) How often we check the core temperature.
GPIO_PIN = 16		# Fan speed control pin


if __name__ == '__main__':
    # Validate the on and off thresholds
    if OFF_THRESHOLD >= ON_THRESHOLD:
        raise RuntimeError('OFF_THRESHOLD must be less than ON_THRESHOLD')

    fan = OutputDevice(GPIO_PIN)

    while True:
        temp = int(CPUTemperature().temperature)

        # Switch to high speed fan if the temperature has reached the limit and the fan
        # isn't already running high
        # NOTE: `fan.value` returns 1 for "on" and 0 for "off"
        if temp > ON_THRESHOLD and not fan.value:
            fan.on()

        # Switch to low speed if the fan is runnning high and the temperature has dropped
        elif fan.value and temp < OFF_THRESHOLD:
            fan.off()

        time.sleep(SLEEP_INTERVAL)
