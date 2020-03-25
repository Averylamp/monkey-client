#!/bin/bash

# Changes to directory of the script
cd "$(dirname "$0")"
apt-get install python3-venv
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python monkey-client.py