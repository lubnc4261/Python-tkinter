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

# the tab code
tabControl = ttk.Notebook(win)


tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="tab 1")
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="tab 2")


tabControl.pack(expand=1, fill="both")

# Start the GUI
win.mainloop()