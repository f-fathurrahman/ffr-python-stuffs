from ase import Atoms
from gpaw import GPAW, FermiDirac

from ase.optimize import QuasiNewton

d = 0.74  # bond length
a = 10.0
c = a/2

atoms = Atoms('H2', positions=([c - d / 2, c, c],[c + d / 2, c, c]), cell=(a, a, a))
            
calc = GPAW( xc="PBE", 
             eigensolver="dav",
             occupations=FermiDirac(0.0, fixmagmom=True), 
             txt="H2.out",
             verbose=1
            )

atoms.set_calculator(calc)

ene = atoms.get_potential_energy()
d0 = atoms.get_distance(0,1)

print("Initial energy = %18.10f eV" % ene)
print("d0 = %18.10f angstrom" % d0)

calc.write("H2.gpw")

relax = QuasiNewton( atoms, logfile="relax.qn.log" )
relax.run(fmax=0.05)

ene = atoms.get_potential_energy()
d0 = atoms.get_distance(0,1)

print("After relax = %18.10f eV" % ene)
print("d0 = %18.10f angstrom" % d0)


