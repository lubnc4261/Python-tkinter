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

# Creating three checkbuttons
ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number, state="readonly")
number_chosen["values"] = (1, 2, 3, 500, 4, 5, 6, 7, 8, 9, 10)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text="disabled", variable=chVarDis, state="disabled")
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.grid(column=2, row=4, sticky=tk.W)

win.mainloop()