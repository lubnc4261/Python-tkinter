# imports
import tkinter as tk
from tkinter import ttk

# create instance
win=tk.Tk()

# Add a title
win.title("GUI")

# Adds the standart geometry
win.geometry("900x900")

# Disable resizing the gui x, y
win.resizable(False, False)

# Adding a Label that will get modified
Label = ttk.Label(win, text="The Label")   # basic label text
Label.grid(column=0, row=0)

# Button Clicked Event
def clicked():
    action.configure(text="I GOT CLICKED") # that will be replace the button text
    Label.configure(foreground="red")      # color of the text
    Label.configure(text="Im Red Now")     # replacing the Label text

# Adding the Button for the Label
action = ttk.Button(win, text="Click me pls", command=clicked) #Button text with the command
action.grid(column=1, row=0)

# Start the GUI
win.mainloop()