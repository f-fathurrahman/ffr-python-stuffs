import os
from gr.pygr import *
import numpy as np

os.environ["GKS_WSTYPE"] = "pdf"

x = np.linspace(-10.0,10.0,50)
y = np.linspace(-10.0,10.0,50)

X, Y = np.meshgrid(x,y)

Z = ( np.exp( -X**2 - Y**2 ) + 
      np.exp( -(X + 5.0)**2 - (Y - 5.0)**2 ) )

# Rosenbrock function
#a = 5.0
#b = 100
#Z = (a - X)**2 + b*(Y - X**2)**2

contour(Z)

