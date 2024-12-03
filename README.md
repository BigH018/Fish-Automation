# Fish Bot Automation Tool

## Overview
**Fish Bot** is a Python-based automation tool designed to streamline repetitive tasks in games like Roblox. It provides two main functionalities:

1. **Appraisal Bot**: Automates the process of fish appraisal by using Optical Character Recognition (OCR) to detect specific words on the screen.
2. **Equip Bot**: Automates the equipping process for items such as Advanced Diving Gear, Super Flippers, and Fish Radar.

With a user-friendly interface and customizable settings, this tool ensures an efficient and seamless experience.

## Features

### 1. **Appraisal Bot**
- Utilizes EasyOCR for detecting specific words from a predefined screen area.
- Automates actions like interacting with in-game characters and selecting items.
- Configurable settings for:
  - Capture area.
  - Target words for appraisal.
  - Hotkeys for starting and stopping the bot.
  - Timing adjustments for optimal performance.

### 2. **Equip Bot**
- Automates equipping in-game items with predefined sequences.
- Supports customization of:
  - Hotkeys for starting the bot.
  - Timing between actions and clicks for improved reliability.
  
### 3. **Graphical User Interface**
- Built with Dear PyGui for easy configuration of bot settings.
- Includes a tutorial section to guide users step-by-step through setup and usage.

### 4. **Interactive Screen Area Selection**
- Uses Tkinter to let users interactively select screen regions for OCR.

## Usage

### 1. **Appraisal Bot Setup**
- Launch the app and navigate to the "Appraisal Bot" tab.
- Configure the following:
  - **Capture Area**: Use the "Set Capture Area" button to select the screen region for OCR.
  - **Target Word**: Enter the word to search for during appraisals.
  - **Hotkeys**: Assign hotkeys for starting and stopping the bot.
  - **Wait Time**: Adjust timing settings for stable operation.

### 2. **Equip Bot Setup**
- Navigate to the "Equip Bot" tab.
- Configure the following:
  - **Hotkey**: Assign a hotkey for starting the Equip Bot.
  - **Timing Settings**: Set wait times for actions and clicks.

### 3. **Tutorial**
- Access the tutorial from the main window to learn how to use the tool effectively.

## Architecture

### Code Breakdown
- **`bot.py`**: Handles OCR and action loops for the Appraisal Bot.
- **`equipt.py`**: Contains logic for automating item equipping.
- **`gui.py`**: Provides the graphical interface using Dear PyGui.
- **`main.py`**: The central controller, integrating the GUI, bots, and hotkey monitoring.
- **`screenData.py`**: Allows users to select screen regions interactively.
- **`tutorial.py`**: Provides in-app tutorials for both bots.

## Required Libraries
This project requires the following Python libraries:
- **easyocr**
- **numpy**
- **Pillow**
- **pynput**
- **keyboard**
- **dearpygui**
- **tkinter** (built-in with Python)
- **threading** (built-in with Python)
- **time** (built-in with Python)

## Acknowledgments
- Thanks to the creators of EasyOCR, Dear PyGui, and Tkinter for the foundational libraries.

## Screenshots

### 1. Main GUI Window
![Main GUI](media/screenshot1.png)

### 2. Tutorial in Action
![Tutorial Window](media/screenshot2.png)
