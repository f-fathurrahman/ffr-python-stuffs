import ase.io

atoms = ase.io.read("H2O.xyz")
atoms.set_pbc([True,True,True])
atoms.set_cell([16.0, 16.0, 16.0])
atoms.center()
atoms.write("H2O_centered.xyz")