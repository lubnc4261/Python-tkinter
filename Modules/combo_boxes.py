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

# Adding the Button

ttk.Label(win, text="Pick a number:").grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number)
number_chosen["values"] = (1, 2, 4, 69, 420)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

# Start the GUI
win.mainloop()