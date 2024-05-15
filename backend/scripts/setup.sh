#!/bin/bash

# Update package list
sudo apt-get update

# Install pip
sudo apt install python3-pip

# Install Poetry
pip install poetry

# Add Poetry to PATH
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

# Install Just
wget -qO - 'https://proget.makedeb.org/debian-feeds/prebuilt-mpr.pub' | gpg --dearmor | sudo tee /usr/share/keyrings/prebuilt-mpr-archive-keyring.gpg 1> /dev/null
echo "deb [arch=all,$(dpkg --print-architecture) signed-by=/usr/share/keyrings/prebuilt-mpr-archive-keyring.gpg] https://proget.makedeb.org prebuilt-mpr $(lsb_release -cs)" | sudo tee /etc/apt/sources.list.d/prebuilt-mpr.list
sudo apt update
sudo apt install just

# Install opencv
sudo apt-get install python3-opencv

# Create a new virtual environment
cd backend
poetry shell
poetry install

# Run database migrations
just db

# Create a superuser
just admin

# Start the development server
just
