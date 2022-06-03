# x708blitz :zap:

*This is a fork of [x708v2.0](https://github.com/suptronics/x708v2.0) modified to integrate the X708 UPS HAT with [RaspiBlitz](https://github.com/rootzoll/raspiblitz) node*

**The scripts manage button action, AC power loss detection, battery level, fan speed and ensure a safe shutdown of `bitcoind`, `lnd` etc. before cutting off the power**

Safe shutdown is triggered by:
- board button
- low battery voltage when AC is lost
- `x708off` command

> **Scripts were tested on Geekworm/Suptronics X708 v1.2 board with RaspiBlitz v1.7.2**

## Contents
- `x708.info.py` - Fetch AC status & battery voltage. Auto shutdown when AC is lost and battery low
- `x708.fan.py` - Automatic fan speed control based on custom-set CPU temperature thresholds
- `install.sh` - Install bash and python scripts, add `x708off` command
- `uninstall.sh` - Revert the changes and remove the repository

## Setup

#### On RaspiBlitz patched with `HiLivin/raspiblitz:feature-x708-support` type:
```
sudo /home/admin/config.scripts/blitz.ups.sh on x708
```

#### You may change the custom values in the scripts:
In file `/home/admin/x708blitz/x708.info.py`:
```
MIN_VOLTAGE = 4.0   # (volts) shutdown when voltage drops below this value
```

In file `/home/admin/x708blitz/x708.fan.py`:
```
HIGH_THRESHOLD = 40 # (degrees Celsius) Fan running at high speed at this temperature.
LOW_THRESHOLD = 32  # (degress Celsius) Fan running at low speed  at this temperature.
SLEEP_INTERVAL = 1  # (seconds) How often do we check the core temperature.
```

#### Restart to apply changes:
```
restart
```

_When done you should be able to safely shutdown your RaspiBlitz with `x708off` command or by holding the board button for 3-7 seconds._

_To safely reboot use `restart` command as usual or hold the button for 1-2 seconds._

_Shutting down with the old `off` won't turn off the X708 board!_

_The UPS info should be seen on the status screen just right to your node's alias._


#### To uninstall use this command:
```
sudo /home/admin/config.scripts/blitz.ups.sh off
```

## Links
### Geekworm wiki
- https://wiki.geekworm.com/X708
