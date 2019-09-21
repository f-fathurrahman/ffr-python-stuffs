from gpaw.cluster import *
from gpaw import GPAW, PW

d = 0.74
a = 6.0
atoms = Cluster(symbols="H2", positions=[(0, 0, 0), (0, 0, d)])

# set the amount of vacuum at least to 4 Å
# and ensure a grid spacing of h=0.2
atoms.minimal_box(4., h=.2)
atoms.set_pbc(True)
atoms.write("H2.xsf")

"""
atoms.calc = GPAW(xc="PBE", txt="-")
atoms.get_potential_energy()
"""