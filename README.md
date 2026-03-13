# rfidPasswordManager
I am very new to most stuff in coding so this is a very simple program and has no real practical application except for being off the internet no matter what.

The materials needed are:
Raspberry pi (any model that matches with the gpio pins of the pi 4),
RC522 RFID reader,
A screen of some kind

Relevent libraries:
MFRC522 https://github.com/pimylifeup/MFRC522-python ,
tkinter,
subprocces,
time,
sys,
RPi.GPIO

fullGUI.py is the base I used in order to make the program, it is very simple an works fine.

To run, just run the command python3 rfidPasswordManager.py, make sure you are in a virtual environment or have global installs of all needed libraries.

Looking at loginScreen.png, it shows a simple text box displayin 'Please Scan RFID', first press get passwords, then put RFID tag up to the scanner, if the id matches it will proceed to the screen shown in passwordScreen.png

It works simply like editing a text file, make sure to press save changes, otherwise any change to the text file will not be saved. Lock passwords will bring back up the login screen. 

As said before, this is for a device that will not be discoverable on the internet or network since there is no type of security such as encryption, and that the RFID tag id needs to be in the python file (line 11 of rfidPasswordManager.py).

Note: the file path on lines 38, 58, and 63 in rfidPasswordManager.py will need to be changed in order to match whatever the user id is for your pi (default is pi4)
