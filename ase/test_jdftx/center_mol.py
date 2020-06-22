from ase.units import Bohr
import ase.io

atoms = ase.io.read("N2H4.xyz")
atoms.set_pbc([True,True,True])
A = 16.0*Bohr
atoms.set_cell([A,A,A])
atoms.center()
atoms.write("N2H4_centered.xyz")
atoms.write("N2H4_centered.xsf")