from ase import Atoms, Atom
from gpaw import GPAW, FermiDirac

a = 10.  # Size of unit cell (Angstrom)

# Hydrogen atom:
atoms = Atoms('Ni2',
             positions=[(0.0,0.0,0.0),(1.5,0.0,0.0)],
             cell=(a, a + 0.0001, a + 0.0002))  # Break cell symmetry
atoms.center()

# gpaw calculator:
calc = GPAW(xc='PBE',
            eigensolver='rmm-diis',  # This solver can parallelize over bands
            occupations=FermiDirac(0.01), 
            txt='-',
            )

atoms.set_calculator(calc)

e1 = atoms.get_potential_energy()
calc.write('Ni2.gpw')


