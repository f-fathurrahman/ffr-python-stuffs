import numpy as np
from ase.build import bulk
from gpaw import GPAW, PW

a0 = 4.04
al = bulk("Al", "fcc", a=a0)
cell0 = np.copy(al.cell)

for ecut in range(200, 501, 50):

    al.calc = GPAW(mode=PW(ecut),
                   xc="PBE",
                   kpts=(8, 8, 8),
                   txt="LOG_Al-ecut-%d.txt" % ecut)

    for eps in np.linspace(-0.02, 0.02, 5):
        al.cell = (1 + eps) * cell0
        al.get_potential_energy()
