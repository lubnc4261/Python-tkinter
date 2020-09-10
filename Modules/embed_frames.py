# imports
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# create instance
win=tk.Tk()

# Add a title
win.title("GUI")

# Adds the standart geometry
win.geometry("900x900")

# Disable resizing the gui x, y
win.resizable(False, False)

# Creating a container that contains all other widgets
xyz = ttk.LabelFrame(win, text="GUI")
xyz.grid(column=0, row=0, padx=8, pady=4)

# using xyz to add a label instead of win
label = ttk.Label(xyz, text="Whats up : ")
label.grid(column=0, row=0)

# text entry box
tz = ttk.Entry(win, width=12)
tz.grid(column=1, row=0)

# Adds a button
ui = ttk.Button(win, text="hmm")
ui.grid(column=2, row=0)

# Start the GUI
win.mainloop()