#!/bin/bash

# Changes to directory of the script
cd "$(dirname "$0")"
echo -e "Starting installation of python3-dev venv \n\n"
apt-get update && apt-get -y install python3-venv
echo -e "Creating venv \n\n"
python3 -m venv venv
echo -e "Activating venv \n\n"
source venv/bin/activate

echo -e "Installing Requirements \n\n"
pip install -r requirements.txt

echo -e "Running monkey \n\n"
python monkey-client.py