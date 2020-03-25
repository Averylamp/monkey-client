#!/bin/bash
echo -e "Starting forwarding of startup-script to monkey-client.log\n\n" >> /var/log/monkey-client.log
touch /startup-script.lock

mkdir -p /home/monkey
git clone https://github.com/Averylamp/monkey-client.git /home/monkey/monkey-client

echo -e "Starting installation of python3-dev venv \n\n"
apt-get update && apt-get -y install python3-venv


# Installs gcsfuse
export GCSFUSE_REPO=gcsfuse-`lsb_release -c -s`
echo "deb http://packages.cloud.google.com/apt $GCSFUSE_REPO main" | sudo tee /etc/apt/sources.list.d/gcsfuse.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
apt-get update && apt-get install gcsfuse


/home/monkey/monkey-client/start.sh 2>&1 | tee /var/log/monkey-client.log &

sleep 1

# Runs the startup script as an acutal script after putting it into the startup script directory
# https://stackoverflow.com/questions/23929235/multi-line-string-with-extra-space-preserved-indentation
cat > "/startup-script.sh" <<- ENDSTARTUPSCRIPT
