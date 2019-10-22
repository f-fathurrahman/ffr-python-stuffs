from ase import Atoms
from gpaw import GPAW, FermiDirac
from gpaw import MixerDif, Davidson, PW

a = 10.0  # Size of unit cell (Angstrom)

atoms = Atoms("Ni2",
             positions=[(0.0,0.0,0.0),
                        (2.0,0.0,0.0)],
             cell=(a, a, a),
             magmoms=[1.7, 1.7],
             pbc=False)
atoms.center(vacuum=4.0)
atoms.write("Ni2.xsf")

# gpaw calculator:
calc = GPAW( mode=PW(),
             xc="PBE",
             eigensolver=Davidson(3),
             occupations=FermiDirac(0.01),
             mixer=MixerDif(0.5, 5, 100),             
             txt="-"
)

atoms.set_calculator(calc)

e1 = atoms.get_potential_energy()
calc.write("Ni2.gpw")

