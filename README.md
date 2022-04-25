# [WIP] x708blitz :zap:

**This is a fork of [x708v2.0](https://github.com/suptronics/x708v2.0) modified to be compatible with [RaspiBlitz](https://github.com/rootzoll/raspiblitz)**

**The UPS HAT safely shutdowns `bitcoind` etc. before cutting off the power when:**
- the board button was pressed
- the AC power is lost and battery is low

**`The scripts were tested on Geekworm/Suptronics X708 v1.2 board with RaspiBlitz v1.7.2`**

Still, it's' WORK IN PROGRESS ***USE AT YOUR OWN RISK!***

## Contents
- `x708.info.py` - Reading AC status & battery voltage. Auto shutdown when battery is low and AC is gone
- `x708.fan.py` - Automatic fan speed control depending on custom-set CPU temperature thresholds
- `install.sh` - Install script creates board signal managers and adds `x708off` bash command
- `uninstall.sh` - Uninstall script reverts the changes and removes the repository

## Setup

#### On RaspiBlitz patched with HiLivin/raspiblitz:feature-x708-support:
```
sudo /home/admin/config.scripts/blitz.ups.sh on x708
```

#### If you wish, you may change the custom values in the scripts:
In file `x708.info.py`:
```
MIN_VOLTAGE = 4.0   # (volts) shutdown when voltage drops below this value
```

In file `x708.fan.py`:
```
ON_THRESHOLD = 40   # (degrees Celsius) Fan running at high speed at this temperature.
OFF_THRESHOLD = 32  # (degress Celsius) Fan running at low speed  at this temperature.
SLEEP_INTERVAL = 1  # (seconds) How often we check the core temperature.
```

#### Reboot to apply changes:
```
restart
```

_When done you should be able to safely shutdown your RaspiBlitz with `x708off` command or by holding the board button for 3-7 seconds._

_To safely reboot use `restart` command (as usual) or hold the button for 1-2 seconds._

_Shutting down with the old `off` won't turn off the X708 board._

_The UPS info should be seen on the status screen just right to your node's alias._

## Link to the Geekworm wiki
- https://wiki.geekworm.com/X708

## TODO:
- [x] Modify RaspiBlitz menu entry to perform X708 software shutdown instead of `off`
- [x] Include battery and AC supply info on the status screen (done by RaspiBlitz `_background.scan.sh`)
- [x] Include uninstall script
