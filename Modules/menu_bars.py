# imports
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu

# create instance
win=tk.Tk()

# Add a title
win.title("GUI")

# Adds the standart geometry
win.geometry("900x900")

# Disable resizing the gui x, y
win.resizable(False, False)

# Exit the GUI Function (clean)
def _quit():
    win.quit()
    win.destroy()
    exit()

# Creating a Menu Bar
menu_bar = Menu(win)
win.config(menu=menu_bar)

# Create the menu and add some tabs
file_menu = Menu(menu_bar, tearoff=0)   # Removes the Start line that can create a new window
file_menu.add_command(label="New")
file_menu.add_separator()               # Creates a line throught the Entries
file_menu.add_command(label="Exit", command=_quit)       # creates a working Exit entry
menu_bar.add_cascade(label="file", menu=file_menu)

# Creates another Menu tab Bar and items
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About")

# Start the GUI
win.mainloop()