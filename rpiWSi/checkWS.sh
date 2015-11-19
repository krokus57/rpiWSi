#!/bin/bash

#while true; do

echo " "
echo "Test rpi WS is running"
if  pgrep -f "python /root/rpiWS/rpiWS.py"; then 

#ifconfig wlan0 | grep -q "inet addr:" ; then
        echo "*** running ok***"
else
        echo "    Problem. Restarting."
	sudo python /root/rpiWS/rpiWS.py &
fi

#done
