import gr
from gr.pygr import plot
from math import pi
import numpy as np

L = 5.0
x = np.linspace(0,L,100)
y1 = np.sin(2*pi*x/L)
y2 = np.cos(2*pi*x/L)

gr.beginprint("TEMP_08.pdf")
plt = plot(x, y1, x, y2)
gr.endprint()
