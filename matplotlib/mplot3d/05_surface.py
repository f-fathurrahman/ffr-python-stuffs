import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import matplotlib
matplotlib.style.use("classic")

fig = plt.figure()
ax = Axes3D(fig)

X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)

X, Y = np.meshgrid(X, Y)

R = np.sqrt(X ** 2 + Y ** 2)
Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.jet)
ax.contourf(X, Y, Z, zdir="z", offset=-2, cmap=plt.cm.jet)
ax.set_zlim(-2, 2)

ax.view_init(elev=45.0, azim=45)
plt.savefig("TEMP_05.png", dpi=300)

