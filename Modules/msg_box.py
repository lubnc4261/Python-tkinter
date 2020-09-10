# imports
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg

# create instance
win=tk.Tk()

# Add a title
win.title("GUI")

# Adds the standart geometry
win.geometry("900x900")

# Disable resizing the gui x, y
win.resizable(False, False)

# Display a MSG
def _msgBox():
    msg.showinfo("Info Box", "Created in tkinter in:\n 2020 lol im learing")
    #answer = msg.askyesornocancel("multiple choice")
    #print(answer)
    #if answer == True:
    #   <sth>

# Display a Warning
def _msgWar():
    msg.showwarning("HU", "May include buggs")

# Display a Error
def _msgErr():

    msg.showerror("No u", "lmao")


# Just the command so it need to be called 
ui = ttk.Button(win, width=12, command=_msgBox)
ui.grid(column=0, row=0)

#
uio = ttk.Button(win, width=12, command=_msgWar)
uio.grid(column=1, row=0)

#
uiü = ttk.Button(win, width=12, command=_msgErr)
uiü.grid(column=2, row=0)

# Start the GUI
win.mainloop()