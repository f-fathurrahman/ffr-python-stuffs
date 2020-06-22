import ase.io
from ase.units import Bohr
from ase.optimize import LBFGS
from JDFTx import JDFTx

atoms = ase.io.read("H2O_centered.xyz")
atoms.set_pbc([False,False,False])

dual = 4.0
Etot_old = 0.0
for ecut in [10.0, 15.0, 20.0, 25.0, 30.0]:
    my_commands = {
        "elec-cutoff": "{} {}".format(ecut,ecut*dual),
        "electronic-minimize": "nIterations 300"
    }
    #atoms.calc = JDFTx(executable="jdftx-1.6.0 -c 1", commands=my_commands, pseudoSet="SG15")
    atoms.calc = JDFTx(executable="jdftx-1.6.0 -c 1", commands=my_commands)
    Etot = atoms.get_potential_energy()
    print("%8.1f %8.1f %18.10f  %18.10f" % (ecut, ecut*dual, Etot, abs(Etot-Etot_old)))
    Etot_old = Etot

