#!/bin/bash
echo -e "Starting forwarding of startup-script to monkey-client.log\n\n" >> /var/log/monkey-client.log
touch /startup-script.lock

mkdir -p /home/monkey
git clone https://github.com/Averylamp/monkey-client.git /home/monkey/monkey-client

echo -e "Starting installation of python3-dev venv \n\n"
apt-get update && apt-get -y install python3-venv

/home/monkey/monkey-client/start.sh 2>&1 | tee /var/log/monkey-client.log &

sleep 1
cat > "/startup-script.sh" <<- ENDSTARTUPSCRIPT

