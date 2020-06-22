import ase.io
from ase.units import Bohr
from ase.optimize import LBFGS
from JDFTx import JDFTx

atoms = ase.io.read("H2O_centered.xyz")
atoms.set_pbc([False,False,False])

my_commands = {
    "elec-cutoff": "15 80",
    "electronic-minimize": "nIterations 300"
}
atoms.calc = JDFTx(executable="jdftx-1.5.0 -c 1", commands=my_commands)

print( atoms.get_forces() )

