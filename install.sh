#x708 V1.3 Powering on /reboot /full shutdown through hardware
#!/bin/bash

echo '#!/bin/bash

SHUTDOWN=5
REBOOTPULSEMINIMUM=200
REBOOTPULSEMAXIMUM=600
echo "$SHUTDOWN" > /sys/class/gpio/export
echo "in" > /sys/class/gpio/gpio$SHUTDOWN/direction
BOOT=12
echo "$BOOT" > /sys/class/gpio/export
echo "out" > /sys/class/gpio/gpio$BOOT/direction
echo "1" > /sys/class/gpio/gpio$BOOT/value

echo "X708 Shutting down..."

while [ 1 ]; do
  shutdownSignal=$(cat /sys/class/gpio/gpio$SHUTDOWN/value)
  if [ $shutdownSignal = 0 ]; then
    /bin/sleep 0.2
  else  
    pulseStart=$(date +%s%3N)
    while [ $shutdownSignal = 1 ]; do
      /bin/sleep 0.02
      if [ $(($(date +%s%3N)-$pulseStart)) -gt $REBOOTPULSEMAXIMUM ]; then
        echo "X708 Shutting down", SHUTDOWN, ", shutting down RaspiBlitz ..."
        sudo off
        exit
      fi
      shutdownSignal=$(cat /sys/class/gpio/gpio$SHUTDOWN/value)
    done
    if [ $(($(date +%s%3N)-$pulseStart)) -gt $REBOOTPULSEMINIMUM ]; then 
      echo "X708 Rebooting", SHUTDOWN, ", rebooting RaspiBlitz ..."
      sudo restart
      exit
    fi
  fi
done' > /etc/x708pwr.sh
sudo chmod +x /etc/x708pwr.sh
sudo sed -i '$ i /etc/x708pwr.sh &' /etc/rc.local 


#X708 full shutdown through Terminal
#!/bin/bash

echo '#!/bin/bash

BUTTON=13

echo "$BUTTON" > /sys/class/gpio/export;
echo "out" > /sys/class/gpio/gpio$BUTTON/direction
echo "1" > /sys/class/gpio/gpio$BUTTON/value

SLEEP=${1:-4}

re='^[0-9\.]+$'
if ! [[ $SLEEP =~ $re ]] ; then
   echo "error: sleep time not a number" >&2; exit 1
fi

echo "X708 Shutting down..."
/bin/sleep $SLEEP

echo "0" > /sys/class/gpio/gpio$BUTTON/value
' > /usr/local/bin/x708softsd.sh
sudo chmod +x /usr/local/bin/x708softsd.sh
printf "%s\n" "alias x708off='sudo x708softsd.sh'" >> ~/.bashrc 

