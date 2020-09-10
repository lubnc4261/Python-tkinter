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

# Adding a Label
ttk.Label(win, text="Label").grid(column=0, row=0)

# Start the GUI
win.mainloop()