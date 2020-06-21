pseudopotentials = {"Na": "Na.pbe-spn-kjpaw_psl.0.2.UPF",
                    "Cl": "Cl.pbe-n-kjpaw_psl.0.3.0.UPF"}

from ase.build import bulk
from ase.calculators.espresso import Espresso
from ase.constraints import UnitCellFilter
from ase.optimize import LBFGS

rocksalt = bulk("NaCl", crystalstructure="rocksalt", a=6.0)
rocksalt.calc = Espresso(pseudopotentials=pseudopotentials,
                tstress=True, tprnfor=True, kpts=(3, 3, 3))

ucf = UnitCellFilter(rocksalt)
opt = LBFGS(ucf)
opt.run(fmax=0.005)

# cubic lattic constant
print((8*rocksalt.get_volume()/len(rocksalt))**(1.0/3.0))
