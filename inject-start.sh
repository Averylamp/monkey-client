#!/bin/bash
mkdir -p /home/monkey
git clone https://github.com/Averylamp/monkey-client.git /home/monkey/monkey-client

/home/monkey/monkey-client/start.sh & >> /var/log/monkey-client.log
