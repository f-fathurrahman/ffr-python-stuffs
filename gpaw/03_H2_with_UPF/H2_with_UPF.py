from gpaw.eigensolvers.davidson import Davidson
from gpaw import GPAW, PoissonSolver, PW
from gpaw.upf import UPFSetupData
import ase.io

upfsetups = {'H': UPFSetupData('H.pz-hgh.UPF')}

system = ase.io.read("H2.xyz")
system.center(vacuum=3.5)
calc = GPAW(txt='-',
            nbands=2,
            setups=upfsetups,
            #mode=PW(350.0),
            eigensolver=Davidson(2),
            xc='oldLDA',
            )

system.set_calculator(calc)
system.get_potential_energy()

from ase.units import Hartree
system.set_calculator(calc)

Etot = system.get_potential_energy()
#print("Cutoff = %18.10f Ha\n" % (450.0/Hartree))
print("Etot = %18.10f Ha\n" % (Etot/Hartree))