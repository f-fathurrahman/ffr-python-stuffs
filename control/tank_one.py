# http://apmonitor.com/che263/index.php/Main/PythonDynamicSim

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def tank_one(h,t):
   # constants
   c1 = 0.13
   Ac = 3.0 # m^2
   # inflow
   qin = 0.5 # m^3/hr
   # outflow
   qout1 = c1 * h[0]**0.5
   # differential equations
   dhdt1 = (qin - qout1) / Ac
   # overflow conditions
   if h[0] >= 1 and dhdt1 >= 0 :
       dhdt1 = 0
   dhdt = [dhdt1]
   return dhdt

# integrate the equations
t = np.linspace(0,10) # times to report solution
h0 = [0.0]            # initial conditions for height
y = odeint(tank_one, h0, t) # integrate

# plot results
plt.figure(1)
plt.plot(t,y[:,0], 'b-')
plt.xlabel('Time (hrs)')
plt.ylabel('Height (m)')
plt.legend()
plt.show()


