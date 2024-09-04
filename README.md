# ESP32-WIFI-MAC-ADDRESS-FINDER

This is a PyQt5 desktop application that allows users to retrieve the MAC address of an ESP32 device connected to their system via a COM port. The application automatically detects the available COM ports, allows the user to select one, and runs the `esptool` to read the MAC address from the connected ESP32 device.

## Features

- Automatically detects available COM ports and allows users to refresh the list.
- Provides real-time connection status updates.
- Retrieves the MAC address of the connected ESP32 device using `esptool`.
- Displays the retrieved MAC address in a copyable format.
- Includes a progress bar during the connection process.

## Requirements

- Python 3.x
- `PyQt5` for the GUI framework
- `esptool` for interacting with the ESP32 device
- `pyserial` for detecting and working with COM ports

## Installation

 Clone the repository:
   git clone <repository-url>
   cd <repository-directory>
   
Install the required dependencies:


pip install pyqt5 pyserial esptool
