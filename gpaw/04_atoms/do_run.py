from gpaw import GPAW
from ase.atoms import Atoms

atoms = Atoms("C", positions=[[0.0,0.0,0.0]])
atoms.center(vacuum=4.0)
print(atoms)

calc = GPAW( txt="-", hund=True )

from ase.units import Hartree
atoms.set_calculator(calc)

Etot = atoms.get_potential_energy()

# convert from eV to Ha
print("Etot = %18.10f Ha\n" % (Etot/Hartree))