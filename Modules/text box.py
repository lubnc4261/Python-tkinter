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

# Create the Click Function
def click():
    action.configure(text="Hey " + name.get())

# Adding a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=0)

# Adding the Button
action = ttk.Button(win, text="Click Me", command=click)
action.grid(column=0, row=1)
#action.configure(state="disabled")       # disable the Button Widget

name_entered.focus()     # Place the cursor into the name Entry

# Start the GUI
win.mainloop()