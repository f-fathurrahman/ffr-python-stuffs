from gpaw.eigensolvers.davidson import Davidson
from gpaw import GPAW, PoissonSolver, PW
import ase.io
from ase.units import Hartree, Bohr

system = ase.io.read("H.xyz")
system.center(vacuum=8.0*Bohr)
calc = GPAW(txt='-',
            nbands=2,
            #mode=PW(450.0),
            eigensolver=Davidson(2),
            xc='oldLDA',
            )

system.set_calculator(calc)
system.get_potential_energy()

system.set_calculator(calc)

Etot = system.get_potential_energy()
print("Cutoff = %18.10f Ha\n" % (450.0/Hartree))
print("Etot = %18.10f Ha\n" % (Etot/Hartree))
