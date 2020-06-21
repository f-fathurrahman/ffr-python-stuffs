from ase.build import bulk
from ase.constraints import UnitCellFilter
from ase.optimize import LBFGS
from JDFTx import JDFTx

atoms = bulk("NaCl", crystalstructure="rocksalt", a=6.0)
atoms.calc = JDFTx(executable="jdftx-1.5.0")

opt = LBFGS(atoms)
opt.run(fmax=0.005)

