import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Medan listrik pada titik (x,y) akibat muatan pada titik r0
def calc_E(q, r0, x, y):
    den = np.hypot(x-r0[0], y-r0[1])**3
    Ex = q * (x - r0[0]) / den
    Ey = q * (y - r0[1]) / den
    return Ex, Ey

nx, ny = 100, 100
x = np.linspace(-2, 2, nx)
y = np.linspace(-2, 2, ny)
X, Y = np.meshgrid(x, y)

# Buat multipol dengan dengan nq muatan dengan tanda yang berbeda
# dan yang terletak pada lingkaran
Nargs = int(sys.argv[1])
nq = 2**Nargs
charges = [] # list berisi muatan dan posisi x dan y muatan
for i in range(nq):
    q = i%2 * 2 - 1
    charges.append((q, (np.cos(2*np.pi*i/nq), np.sin(2*np.pi*i/nq))))

Ex = np.zeros((ny, nx))
Ey = np.zeros((ny, nx))
for charge in charges:
    # Hitung medan akibat tiap titik untuk setiap muatan
    ex, ey = calc_E(*charge, x=X, y=Y)
    Ex = Ex + ex
    Ey = Ey + ey

# Plot medan vektor
fig = plt.figure()
ax = fig.add_subplot(111)
# warna berdasarkan magnitudo medan
color = 2 * np.log(np.hypot(Ex, Ey)) 
ax.streamplot(x, y, Ex, Ey, color=color, linewidth=1, cmap=plt.cm.jet,
              density=1, arrowstyle='->', arrowsize=1.5)

# Plot lingkaran untuk melambangkan muatan
charge_colors = {True: '#aa0000', False: '#0000aa'}
for q, pos in charges:
    ax.add_artist(Circle(pos, 0.05, color=charge_colors[q>0]))

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
ax.set_aspect('equal')
plt.tight_layout()
plt.savefig("IMG_E_field_" + str(nq) + ".png", dpi=150)

