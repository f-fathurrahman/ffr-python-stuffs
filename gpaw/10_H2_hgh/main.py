from ase import Atoms, Atom
from gpaw import GPAW, PW, FermiDirac
from ase.units import Bohr, Hartree

a = 16.0*Bohr
c = a/2

# Hydrogen atom:
atom = Atoms("H", positions=[(c, c, c)],
                  magmoms=[0],
                  cell=(a, a, a))

# gpaw calculator:
ecutwfc = 15.0*Hartree
calc = GPAW( mode=PW(ecutwfc), 
             setups="hgh",
             xc="LDA",
             eigensolver="rmm-diis",
             occupations=FermiDirac(0.0, fixmagmom=True),
             spinpol=False,
             txt="H.out" )
atom.set_calculator(calc)

e1 = atom.get_potential_energy()
calc.write("H.gpw")


# Hydrogen molecule:
d = 0.74  # Experimental bond length
molecule = Atoms("H2",
                 positions=([c - d / 2, c, c],
                            [c + d / 2, c, c]),
                 cell=(a, a, a))

calc.set(txt="H2.out")
calc.set(hund=False)  # No hund rule for molecules

molecule.set_calculator(calc)
e2 = molecule.get_potential_energy()
calc.write("H2.gpw")

e_at = 2*e1 - e2
print("H atom energy      : %18.10f eV = %18.10f" % (e1,e1/Hartree))
print("H2 molecule energy : %18.10f eV = %18.10f" % (e2,e2/Hartree))
print("Atomization energy : %18.10f eV = %18.10f" % (e_at, e_at/Hartree))

