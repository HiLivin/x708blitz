#!/bin/bash

# Revert the changes made by install.sh and remove the repository
sudo sed -i '/x708/d' /etc/rc.local
sudo sed -i '/x708/d' /home/admin/.bash_aliases

sudo rm /etc/x708pwr.sh
sudo rm /usr/local/bin/x708softsd.sh

sed -i '183c OPTIONS+=(OFF "PowerOff RaspiBlitz")' /home/admin/00mainMenu.sh
sed -i '344c \ \ \ \ \ \ \ \ OFF)' /home/admin/00mainMenu.sh
sed -i '351c \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ sudo /home/admin/config.scripts/blitz.shutdown.sh' /home/admin/00mainMenu.sh

rm -rf /home/admin/x708blitz
