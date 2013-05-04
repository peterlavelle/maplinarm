maplinrobot.py
==============

Python script to control the Maplin USB robotic arm on your Raspberry PI.

Requirements
============

- Raspian
- Python 2.7
- pip
- pyusb Library

Installation
===========

- Create a new udev rules file at <strong>/etc/udev/rules.d/85-robotarm.rules</strong> with the contents
<pre>
SUBSYSTEM=="usb", ATTRS{idVendor}=="1267", ATTRS{idProduct}=="0000", ACTION=="add", GROUP="plugdev", MODE="0666"
</pre>
- Add your user to the plugdev group using the command: <pre>sudo usermod -aG plugdev yourusername</pre>
- Reboot the Pi with the command: <pre>sudo shutdown -r now</pre>
- Make the script executable with the command: <pre>chmod 755 maplinrobot.py</pre>
- Install pip with the command: <pre>sudo apt-get install python-pip -y</pre>
- Install pyusb Library via pip with the command: <pre>sudo pip install pyusb</pre>
- Open the script and edit it to suit your needs (See Example Usage section for more info.)
- type <strong> ./maplinrobot.py </strong> to run. If you have problems running as a normal user, try running the script as root.

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

Example Usage
=============

-At the bottom of the script uncomment the lines below:

<pre>
s = MaplinRobot()
s.MoveArm(t=1.0, cmd='base-clockwise')
</pre>

This will rotate the base of the arm clockwise for 1 second. Duration of each command is set by passing a float value 
to the <strong>t</strong> parameter. 

The argument passed to the <strong>cmd</strong> parameter can be any command in the Moving the Arm section above.



