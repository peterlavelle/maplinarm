maplinarm
=========

Python script to control the Maplin USB robotic arm on your Raspberry PI.

Requirements
============

- Raspian
- Python 2.7
- pip
- pyusb Library

Installaion
===========

- Make the script executable with the command: chmod 755 maplinrobot.py
- Install pip with the command: sudo apt-get install python-pip -y
- Install pyusb Library via pip with the command: pip install pyusb

Moving the Arm
==============

Commands are stored in a dictionary. Valid commands to send to the arm are:

- 'base-anti-clockwise' - Rotates the base ant-clockwise
- 'base-clockwise' - Rotates the base clockwise
- 'shoulder-up' - Raises the shoulder
- 'shoulder-down' - Lowers the shoulder
- 'elbow-up' - Raises the elbow
- 'elbow-down' - Lowers the elbow
- 'wrist-up' - Raises the wrist
- 'wrist-down' - Lowers the wrist
- 'grip-open' - Opens the grip
- 'grip-close' - Closes the grip
- 'light-on' - Turns on the LED in the grip
- 'light-off' - Turns the LED in the grip off
- 'stop' - Stops all movement of the arm




