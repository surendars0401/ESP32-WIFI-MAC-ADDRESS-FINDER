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
   How to Run
   Connect your ESP32 device to your computer via a USB-to-COM adapter.

Run the application using the following command:

python mac_address_finder.py
In the application window:

Select the appropriate COM port from the dropdown.
Click on the "Get MAC Address" button to retrieve and display the MAC address of the ESP32 device.
Troubleshooting
No COM ports detected: Ensure that the ESP32 is properly connected and that the drivers for the USB-to-COM adapter are installed.

esptool not found error: Make sure esptool is correctly installed. You can install it by running:

pip install esptool
Timeout issues: If the connection times out, verify that the correct COM port is selected and that the ESP32 is powered on and properly connected.

Acknowledgements
This application uses esptool, a widely used tool for flashing ESP32 devices and retrieving hardware information.
The PyQt5 library is used for building the graphical user interface.
