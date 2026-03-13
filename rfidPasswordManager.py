import tkinter as tk
from tkinter import messagebox
import os
import subprocess
from time import sleep
import sys
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()

MASTER_ID = 

def scanID():
    # This will pause the UI until a card is scanned
    # We will improve how this is called below
    id, text = reader.read()

    if id == MASTER_ID:
        unlockPasswords()
    else:
        messagebox.showerror("Access Denied", "Unauthorized RFID Tag")

# simple, closes the program by quiting the window
def closeProgram():
    GPIO.cleanup()
    window.quit()

# gets rid of the unlock button, gives the passwords, lock, and save button
def unlockPasswords():
    loginFrame.pack_forget()
    passwordButton.pack_forget()
    loginText.delete('1.0', tk.END)

    frame.pack(side = tk.TOP, pady = 100)
    lockButton.pack(side = tk.BOTTOM)
    saveButton.pack(side = tk.BOTTOM)
    logins.pack()
    with open('/home/pi4/Documents/passwords.txt', 'r') as file:
        contents = file.read()
        logins.insert('1.0', contents)

# gets rid of the lock button and frame while also clearing the contents of the frame
def lockPasswords():
    lockButton.pack_forget()
    frame.pack_forget()
    logins.delete('1.0', tk.END)
    passwordButton.pack(side = tk.BOTTOM)
    saveButton.pack_forget()

    loginFrame.pack()
    loginText.pack()
    text = 'Please scan RFID'
    loginText.insert('1.0', text)

# saves changes to file
def saveChanges(text_widget):
    changes = logins.get('1.0', tk.END)
    with open('/home/pi4/Documents/passwords.txt', 'w') as file:
        file.write(changes)

#check to see if password file already exists
try:
        with open('/home/pi4/Documents/passwords.txt', 'x') as file:
            print(f'file was created')
except FileExistsError:
    print(f'file already exists ')

# preperation for application window
window = tk.Tk()
window.title('Password Manager')
window.after(500, lambda: window.attributes('-fullscreen', True))

closeButton = tk.Button(window, text = 'close program', width = 25, command = closeProgram)
passwordButton = tk.Button(window, text = 'get your passwords', width = 25, command = scanID)
lockButton = tk.Button(window, text = 'lock passwords', width = 25, command = lockPasswords)
saveButton = tk.Button(window, text = 'save changes', width = 25, command = lambda: saveChanges(logins))
frame = tk.Frame(window, bg = 'white', width = 800, height = 400, bd = 3, relief = tk.RIDGE)
logins = tk.Text(frame, width = 750, height = 20)
loginFrame = tk.Frame(window, bg = 'white', width = 800, height = 400, bd = 3, relief = tk.RIDGE)
loginText = tk.Text(loginFrame, width = 750, height = 20)

# start window
closeButton.pack(side = tk.BOTTOM, pady = 20)
passwordButton.pack(side = tk.BOTTOM)
loginFrame.pack()
loginText.pack()
text = 'Please scan RFID'
loginText.insert('1.0', text)
window.mainloop()


