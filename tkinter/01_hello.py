from tkinter import *

# import themed Tk widget library
from tkinter.ttk import *
# the Tk widgets will be replaced by better-looking ttk widgets
# wherever applicable

root = Tk()

label1 = Label(root, text="Hello from ffr")
label1.pack()

label2 = Label(root, text="Hello again from ffr")
label2.pack()

root.mainloop()
