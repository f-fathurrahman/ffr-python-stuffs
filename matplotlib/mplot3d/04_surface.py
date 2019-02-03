import numpy as np

import matplotlib.pyplot as plt
from matplotlib import cm

from mpl_toolkits.mplot3d import Axes3D

x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(x, y)

Z = np.sin(X)*np.sin(Y)

fig = plt.figure()
ax = fig.gca(projection="3d")

ax.plot_surface(X, Y, Z, cmap=cm.jet)

ax.view_init(elev=45.0, azim=45)

plt.savefig("TEMP_04.png", dpi=300)

