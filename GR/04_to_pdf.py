import gr
from gr.pygr import *

x = [-3.3 + t*0.1 for t in range(66)]
y = [t**5 - 13*t**3 + 36*t for t in x]

gr.beginprint("04_simple.pdf")
plot(x, y)
gr.endprint()

