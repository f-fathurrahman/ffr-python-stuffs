pseudopotentials = {"H": "H.pbe-kjpaw_psl.0.1.UPF",
                    "O": "O.pbe-n-kjpaw_psl.0.1.UPF"}

import ase.io
from ase.calculators.espresso import Espresso
from ase.optimize import LBFGS

input_data = {
    'system': {
        'ecutwfc': 30.0,
        'ecutrho': 120.0
    },
    'disk_io': 'none',
    'pseudo_dir': '/home/efefer/pseudo/PSLIB'
}

calc = Espresso(pseudopotentials=pseudopotentials,
                tstress=True, tprnfor=True,
                input_data=input_data)

atoms = ase.io.read("H2O_centered.xyz")
atoms.calc = Espresso(pseudopotentials=pseudopotentials,
                tstress=True, tprnfor=True)

opt = LBFGS(atoms)
opt.run(fmax=0.005)
