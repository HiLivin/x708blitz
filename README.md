#x708blitz :zap:

**It's a fork of suptronics/x708v2.0 repository modified to be compatible with RaspiBlitz.
The board safely shutdowns `bitcoind` etc. before cutting off the power.
The scripts were tested on Geekworm/Suptronics X708 v1.2 board with RaspiBlitz v1.7.2, still use at your own risk!**

##Contents
`x708bat.py`  -- Reading battery voltage & capacity. Automatic safe shutdown when battery low 
`x708fan.py` -- Automatic fan speed control depending on custom CPU temperature thresholds
`x708pld.py` -- Testing the power loss detection 
`x708plsd.py` -- Automatic safe shutdown after AC power loss or power adapter failure 
`install.sh` -- Install script adds `x708off` bash command and manages board button action

##Setup

####Enable I2C interface and install prerequisites:
```
sudo raspi-config nonint do_i2c 0
sudo apt-get install python3-smbus i2c-tools
```

####Clone the repository and run the installation script:
```
git clone https://github.com/HiLivin/x708blitz.git
cd x708blitz
chmod +x install.sh
sudo bash install.sh
```

####To use a python script check it first to edit custom parameters and proceed:
```
sudo echo "python3 $PWD/SCRIPT_NAME.py &" >> /etc/rc.local
```

####Reboot to apply changes:
```
sudo restart
```

When done you should be able to safely shutdown your RaspiBlitz with `x708off` command or by holding the board button for 3-7 seconds.
To safely reboot use `restart` command (as usual) or hold the button for 1-2 seconds.
Shutting down with the old `off` won't turn off the X708 board.

##Link to the Geekworm wiki
- https://wiki.geekworm.com/X708

##TODO:
- [ ] Modify RaspiBlitz menu to perform X708 software shutdown instead of `off`
- [ ] Include battery and AC supply info on the status screen
- [ ] Include uninstall script
