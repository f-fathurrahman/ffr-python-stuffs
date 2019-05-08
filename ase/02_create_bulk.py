import ase.build

C_diamond = ase.build.bulk(name="C", crystalstructure="diamond", a=4.0, cubic=True)
C_diamond.write("TEMP_C_diamond.xsf")

ase.io.write("TEMP_C_diamond.eps", C_diamond, show_unit_cell=1,
              rotation="0y,0x", scale=30)
