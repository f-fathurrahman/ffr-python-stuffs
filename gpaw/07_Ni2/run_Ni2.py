from ase import Atoms, Atom
from gpaw import GPAW, FermiDirac
from gpaw import Mixer, Davidson, PW

a = 10.  # Size of unit cell (Angstrom)

# Hydrogen atom:
atoms = Atoms('Ni2',
             positions=[(0.0,0.0,0.0),(2.0,0.0,0.0)],
             cell=(a, a, a),  # Break cell symmetry
			 magmoms=[0.5,0.5],
			 pbc=False)
atoms.center()
atoms.write("Ni2.xsf")

# gpaw calculator:
calc = GPAW( mode=PW(),
             xc='PBE',
             eigensolver=Davidson(3),  # This solver can parallelize over bands
             occupations=FermiDirac(0.01),
             mixer=Mixer(0.02,1,100),
             txt='LOG1'
            )

atoms.set_calculator(calc)

e1 = atoms.get_potential_energy()
calc.write('Ni2.gpw')


