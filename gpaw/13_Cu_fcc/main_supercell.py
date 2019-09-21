from ase.build import bulk
from ase.build import find_optimal_cell_shape, make_supercell
import numpy as np

conf = bulk("Cu", cubic=True)

#P1 = find_optimal_cell_shape(conf.cell, 32, "sc")
P1 = np.identity(3)*4
print(P1)

a = make_supercell(conf, P1, wrap=True, tol=1e-5)
a.write("Cu_super.xsf")