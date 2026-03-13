import tkinter as tk
from tkinter import messagebox
import os

# simple, closes the program by quiting the window
def closeProgram():
    window.quit()

# gets rid of the unlock button, gives the passwords, lock, and save button
def unlockPasswords():
    frame.pack(side = tk.TOP, pady = 100)
    lockButton.pack(side = tk.BOTTOM)
    saveButton.pack(side = tk.BOTTOM)
    passwordButton.pack_forget()
    logins.pack()

    with open('/home/pi4/Documents/passwords.txt', 'r') as file:
        contents = file.read()
        logins.insert('1.0', contents)


# gets rid of the lock button and frame while also clearing the contents of the frame
def lockPasswords():
    passwordButton.pack(side = tk.BOTTOM)
    lockButton.pack_forget()
    frame.pack_forget()
    logins.delete('1.0', tk.END)
    saveButton.pack_forget()

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
passwordButton = tk.Button(window, text = 'get your passwords', width = 25, command = unlockPasswords)
lockButton = tk.Button(window, text = 'lock passwords', width = 25, command = lockPasswords)
saveButton = tk.Button(window, text = 'save changes', width = 25, command = lambda: saveChanges(logins))
frame = tk.Frame(window, bg = 'white', width = 800, height = 400, bd = 3, relief = tk.RIDGE)
logins = tk.Text(frame, width = 750, height = 20)

# start window
closeButton.pack(side = tk.BOTTOM, pady = 20)
passwordButton.pack(side = tk.BOTTOM)
window.mainloop()

