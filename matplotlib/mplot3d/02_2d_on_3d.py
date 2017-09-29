from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# use ax.plot's zdir keyword

fig = plt.figure()
ax = fig.gca(projection='3d')

# sin curve using x and y axes
x = np.linspace(0, 1, 100)
y = np.sin(x*2*np.pi)/2 + 0.5
ax.plot(x, y, zs=0, zdir='z', label='curve in (x,y)', marker='o', linewidth=2)

ax.legend()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.view_init(elev=20.0, azim=-35)

plt.show()
plt.savefig('02.png', dpi=300)
