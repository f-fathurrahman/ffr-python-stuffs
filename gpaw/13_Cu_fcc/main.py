from gpaw import GPAW, FermiDirac
from gpaw import Mixer, Davidson, PW
import numpy as np
from ase.build import bulk

atoms = bulk("Cu", "fcc", a=3.6, cubic=True)

a = 10.0  # Size of unit cell (Angstrom)

#atoms.set_initial_magnetic_moments(0.5*np.ones(len(atoms)))

atoms.write("Cu_fcc.xsf")

# gpaw calculator:
calc = GPAW(mode=PW(),
            xc="PBE",
            #kpts=(6, 6, 6),
            kpts={"density": 3.5},
            occupations=FermiDirac(0.01),
            spinpol=False,
            txt="-"
)

atoms.set_calculator(calc)

e1 = atoms.get_potential_energy()
calc.write("Cu.gpw")
