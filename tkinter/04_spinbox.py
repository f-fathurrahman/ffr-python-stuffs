import tkinter as tk
from tkinter import ttk

root = tk.Tk()

label = tk.Label(root, text="Example spinbox")
label.pack()

my_spinbox = tk.Spinbox(root, from_=0.3, to=1.0, increment=0.01)
my_spinbox.pack()

root.mainloop()

