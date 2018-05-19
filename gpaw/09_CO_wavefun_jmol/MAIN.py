from ase import Atoms
from gpaw import GPAW

d = 1.1
a = 5.0
c = a/2

atoms = Atoms("CO", positions=[ (c - 0.5*d, c, c), (c + 0.5*d, c, c) ], cell=(a,a,a))

calc = GPAW( nbands=5, h=0.2, txt="LOG1" )
atoms.set_calculator( calc )

energy = atoms.get_potential_energy()
forces = atoms.get_forces()

print("energy = ", energy)
print("forces = ")
print(forces)

calc.write("CO.gpw", mode="all")
