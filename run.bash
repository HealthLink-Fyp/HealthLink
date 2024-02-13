#!/bin/bash

# Check if .venv folder exists
if [ -d ".venv" ]; then
    echo "Virtual environment found. Skipping requirements installation."
else
    echo "Installing requirements..."
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt --quiet
fi

# Migrate Project
python3 manage.py makemigrations
python3 manage.py migrate

# Run Django project
python3 manage.py runserver

