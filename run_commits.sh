#!/bin/bash

echo "Starting Auto-Commit System..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed!"
    echo "Please install Python from python.org"
    exit 1
fi

# Install requirements if needed
echo "Installing requirements..."
pip3 install -r requirements.txt

echo ""
echo "Running main script..."
python3 main.py