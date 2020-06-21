import ase.io
from ase.units import Bohr
from ase.optimize import LBFGS
from JDFTx import JDFTx

atoms = ase.io.read("H2O_centered.xyz")
atoms.set_pbc([False,False,False])

atoms.calc = JDFTx(executable="jdftx-1.5.0 -c 1")

opt = LBFGS(atoms)
opt.run(fmax=0.005)

