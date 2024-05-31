#!/bin/bash

# Update package list
sudo apt-get update
sudo apt-get clean
sudo apt-get autoremove
# Install pip
sudo apt install python3-pip
pip install --upgrade pip
# Install dependencies
pip install --no-cache-dir -r requirements.txt
python3 -m spacy download en_core_web_lg
pip install gunicorn
# Django setup
python3 manage.py collectstatic --noinput
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput