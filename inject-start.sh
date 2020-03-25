#!/bin/bash

tail -f /var/log/syslog | grep "startup-script" > /var/log/monkey-client.log 2>&1 &

mkdir -p /home/monkey
git clone https://github.com/Averylamp/monkey-client.git /home/monkey/monkey-client

/home/monkey/monkey-client/start.sh & >> /var/log/monkey-client.log 2>&1 &
