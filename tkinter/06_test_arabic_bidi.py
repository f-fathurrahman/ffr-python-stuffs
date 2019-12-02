# !/usr/bin/python3
from tkinter import *

import arabic_reshaper

from tkinter import messagebox
from bidi.algorithm import get_display

text_to_be_reshaped = "ﺏﺎﻃﻭ"
reshaped_text = arabic_reshaper.reshape(text_to_be_reshaped)

bidi_text = get_display(reshaped_text)

top = Tk()
top.geometry("500x500")
#B = Button(top, text=bidi_text, font=("Monaco", 72))
B = Button(top, text="Bebebebeb", font=("Monaco", 72))
B.place(x=0,y=0)
top.mainloop()