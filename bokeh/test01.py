import bokeh
import numpy as np
import bokeh.plotting as bp
bp.output_file("bokeh1.html", mode="inline")
x = np.linspace(0,2*np.pi,1024)
y = np.cos(x)*np.sin(2*x)
fig = bp.figure()
fig.line(x,y)
bp.save(fig)

