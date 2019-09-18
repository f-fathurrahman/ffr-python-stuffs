from gpaw import GPAW

# Restart from ground state and fix potential:
calc = GPAW("Si_gs.gpw",
            nbands=16,
            fixdensity=True,
            symmetry="off",
            kpts={"path": "GXWKL", "npoints": 60},
            convergence={"bands": 8},
            txt="LOG_Si_bands.txt")
calc.get_potential_energy()

bs = calc.band_structure() # band structure info, such as energies, path, etc
bs.plot(filename="bandstructure.png", emax=10.0)

calc.write("Si_bands.gpw")
