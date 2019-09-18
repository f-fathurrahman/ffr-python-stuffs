import numpy as np
from ase.build import bulk
from gpaw import GPAW, PW

a0 = 4.04
al = bulk("Al", "fcc", a=a0)
cell0 = np.copy(al.cell)

ecut = 400.0

for k in range(4, 17):

    al.calc = GPAW(mode=PW(ecut),
                   xc="PBE",
                   kpts=(k, k, k),
                   basis="dzp",
                   txt="LOG_Al-kpt-%02d.txt" % k)

    for eps in np.linspace(-0.02, 0.02, 5):
        al.cell = (1 + eps) * cell0
        al.get_potential_energy()
