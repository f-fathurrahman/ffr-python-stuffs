from ase import Atoms, Atom
from gpaw import GPAW, PW, FermiDirac
from ase.units import Bohr, Hartree

a = 16.0*Bohr
c = a/2

# Hydrogen atom:
atom = Atoms("Si", positions=[(c, c, c)],
                  magmoms=[0],
                  cell=(a, a, a))

# gpaw calculator:
ecutwfc = 15.0*Hartree
calc = GPAW( mode=PW(ecutwfc), 
             setups="hgh",
             xc="LDA",
             eigensolver="rmm-diis",
             occupations=FermiDirac(0.1),
             spinpol=False,
             txt="TEMP_Si.log" )
atom.set_calculator(calc)

e1 = atom.get_potential_energy()
calc.write("TEMP_Si.gpw")

print("===================================================")
print("Si atom energy      : %18.10f eV = %18.10f Hartree" % (e1,e1/Hartree))


