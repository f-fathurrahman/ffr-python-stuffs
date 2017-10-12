from __future__ import print_function
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection='3d')

colors = ('r', 'g', 'b', 'k')
Npoints = 20
x = np.random.sample(Npoints*len(colors))
y = np.random.sample(Npoints*len(colors))

c_list = []
for c in colors:
    c_list.append([c]*Npoints)

# by using zdir='y', the y value of these points is fixed to zs value 0
# and the (x,y) points are plotted on the x and z axes
ax.scatter(x, y, zs=0, zdir='y', c=c_list, label='points in (x,z)')

ax.legend()
ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.set_zlim(0,1)
ax.set_xlabel('X')
ax.set_ylabel('X')
ax.set_zlabel('X')

ax.view_init(elev=20., azim=-35.)
plt.show()
