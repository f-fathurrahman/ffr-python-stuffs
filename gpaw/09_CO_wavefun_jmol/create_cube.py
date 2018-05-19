from ase.io import write
from gpaw import restart

basename = "CO"

atoms, calc = restart(basename + ".gpw")

nbands = calc.get_number_of_bands()

for iband in range(nbands):
    wf = calc.get_pseudo_wave_function( band=iband )
    fname = "{0}_{1}.cube".format(basename,iband)
    print("Writing wavefun #", iband, " to file ", fname)
    write(fname, atoms, data=wf)



