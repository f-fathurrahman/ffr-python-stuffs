from ase.build import bulk
from gpaw import GPAW, PW, FermiDirac

# Perform standard ground state calculation (with plane wave basis)
si = bulk("Si", "diamond", 5.43)
calc = GPAW(mode=PW(200),
            xc="PBE",
            kpts=(8, 8, 8),
            random=True,  # random guess (needed if many empty bands required)
            occupations=FermiDirac(0.01),
            txt="LOG_Si_gs.txt")
si.calc = calc
si.get_potential_energy()
calc.write("Si_gs.gpw")

