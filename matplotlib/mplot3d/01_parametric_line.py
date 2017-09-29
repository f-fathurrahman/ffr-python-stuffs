import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

t = np.arange(0,1.0,0.02)
x = 0.5*t**2
y = 0.5*(t-1.0)**2
z = x + np.sin(y)

ax.plot(x, y, z);

plt.savefig("01.png", dpi=300)
plt.show()
