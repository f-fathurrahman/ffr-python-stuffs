import tkinter as tk
from tkinter import ttk

root = tk.Tk()

my_str = tk.StringVar()
entry1 = tk.Entry(root, textvariable=my_str)

entry1.pack()

root.mainloop()

