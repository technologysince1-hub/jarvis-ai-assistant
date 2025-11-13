#!/bin/bash

echo "========================================"
echo "JARVIS AI Assistant - Installation Script"
echo "========================================"
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.7+ from https://python.org"
    exit 1
fi

# Check Python version
python3 -c "import sys; exit(0 if sys.version_info >= (3, 7) else 1)"
if [ $? -ne 0 ]; then
    echo "ERROR: Python 3.7+ is required"
    echo "Please upgrade your Python installation"
    exit 1
fi

echo "Python found. Installing dependencies..."
echo "========================================"

# Upgrade pip
python3 -m pip install --upgrade pip

# Install core dependencies
echo "Installing core dependencies..."
python3 -m pip install eel
python3 -m pip install pyttsx3
python3 -m pip install speechrecognition
python3 -m pip install pyaudio
python3 -m pip install psutil
python3 -m pip install requests
python3 -m pip install pillow
python3 -m pip install opencv-contrib-python
python3 -m pip install numpy
python3 -m pip install pyautogui
python3 -m pip install pywhatkit
python3 -m pip install schedule
python3 -m pip install cryptography
python3 -m pip install qrcode

echo
echo "Installing AI dependencies..."
python3 -m pip install groq
python3 -m pip install google-generativeai
python3 -m pip install hugchat

echo
echo "Installing optional dependencies..."
python3 -m pip install pvporcupine
python3 -m pip install pygame
python3 -m pip install gtts

echo
echo "========================================"
echo "Installation completed successfully!"
echo "========================================"
echo

# Create configuration files if they don't exist
if [ ! -f "groq_config.py" ]; then
    echo "Creating groq_config.py..."
    echo 'GROQ_API_KEY = "your-groq-api-key-here"' > groq_config.py
fi

if [ ! -f "gemini_config.py" ]; then
    echo "Creating gemini_config.py..."
    echo 'GEMINI_API_KEY = "your-gemini-api-key-here"' > gemini_config.py
fi

echo
echo "========================================"
echo "SETUP INSTRUCTIONS:"
echo "========================================"
echo "1. Edit groq_config.py and add your Groq API key"
echo "2. Edit gemini_config.py and add your Gemini API key"
echo "3. For phone integration, enable USB debugging on Android"
echo "4. Run: python3 run.py"
echo
echo "For face authentication setup, run: python3 setup_face_auth.py"
echo
echo "========================================"
echo "Installation complete! Ready to run JARVIS."
echo "========================================"