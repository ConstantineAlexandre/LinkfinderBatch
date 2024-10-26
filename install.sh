#!/bin/bash

# Get the path from CheeseBurger.py
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SCRIPT_PATH="$SCRIPT_DIR/LinkfinderBatch.py"

# Change the CheeseBurger.py file to executable
chmod +x "$SCRIPT_PATH"

# Create a symbolic link in /usr/local/bin
ln -sf "$SCRIPT_PATH" /usr/local/bin/LinkfinderBatch

echo "LinkfinderBatch has been successfully installed. Now you can run it with the command 'LinkfinderBatch' in the terminal."