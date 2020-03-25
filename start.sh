#!/bin/bash

# Changes to directory of the script
cd "$(dirname "$0")"

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python monkey-client.py