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

# Container that hold the labels
buttons_frame = ttk.LabelFrame(win, text="Labels ")
# buttons_frame = ttk.LabelFrame(win, text=" ")             # No LabelFrame name
buttons_frame.grid(column=0, row=7)
# buttons_frame.grid(column=0, row=7, padx=20, pady=20)     # will change the position of the label on the GUI

# place labels into the container element
ttk.Label(buttons_frame, text="Label 1 ").grid(column=0, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label 2 ").grid(column=1, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label 3 ").grid(column=2, row=0, sticky=tk.W)

# Start the GUI
win.mainloop()