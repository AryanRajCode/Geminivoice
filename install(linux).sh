#!/bin/bash

# Function to check if Python is installed
check_python() {
    if ! command -v python3 &>/dev/null; then
        echo "Python 3 is not installed. Installing Python..."
        # Install Python
        sudo apt update
        sudo apt install python3 -y
        echo "Python installed successfully."
    else
        echo "Python 3 is already installed."
    fi
}

# Function to install dependencies
install_dependencies() {
    echo "Installing dependencies..."
    # Install dependencies using pip
    pip3 install -r requirements.txt
    echo "Dependencies installed successfully."
}

# Check if requirements.txt exists
if [ -f requirements.txt ]; then
    check_python
    install_dependencies
    # Run the Python main script
    echo "Running main.py..."
    python3 main.py
else
    echo "Error: requirements.txt not found."
fi
