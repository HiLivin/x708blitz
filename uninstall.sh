#!/bin/bash

# Revert the changes made by install.sh and remove the repository
sudo sed -i '/x708/d' /etc/rc.local
sudo sed -i '/x708/d' /home/admin/.bash_aliases

sudo rm /etc/x708pwr.sh
sudo rm /usr/local/bin/x708softsd.sh

patch -u -R /home/admin/00mainMenu.sh -i /home/admin/x708blitz/00mainMenu.sh.diff

rm -rf /home/admin/x708blitz
