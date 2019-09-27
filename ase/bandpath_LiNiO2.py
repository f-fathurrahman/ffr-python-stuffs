import numpy as np
from ase import Atoms

Natoms = 4

A = 5.07202 # in angstrom
LatVecs = np.zeros((3,3))
LatVecs[0,:] = [1.000000000000000, 0.000000000000000, 0.000000000000000] 
LatVecs[1,:] = [0.836301242074196, 0.548270218510140, 0.000000000000000] 
LatVecs[2,:] = [0.836301242074196, 0.249697083586569, 0.488110232379448] 
LatVecs = A*LatVecs
print(LatVecs)

coords = np.zeros((Natoms,3))
coords[0,:] = [0.000000000000000, 0.000000000000000, 0.000000000000000]
coords[1,:] = [0.741937000000000, 0.741937000000000, 0.741937000000000]
coords[2,:] = [0.258063000000000, 0.258063000000000, 0.258063000000000]
coords[3,:] = [0.500000000000000, 0.500000000000000, 0.500000000000000]
print(coords)
coords = np.matmul(coords, LatVecs)

atsymbs = ["Ni", "O", "O", "Li"]

atoms = Atoms(symbols=atsymbs, positions=coords, cell=LatVecs, pbc=[True,True,True])
atoms.write("TEMP_atoms.xsf")


from ase.dft.kpoints import get_special_points
spec_kpts = get_special_points(atoms.cell, lattice="orthorhombic")
print(spec_kpts)