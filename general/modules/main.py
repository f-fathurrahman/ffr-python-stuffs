from __future__ import print_function
import numpy as np

#import sys
#sys.path.append('./')

execfile('global_vars.py')
execfile('print_Npoints.py')

def modify_Npoints():
    global Npoints
    Npoints = 5

def init_VHartree():
    global VHartree
    global Npoints
    VHartree = np.zeros(Npoints)
    VHartree[:] = 1.1

modify_Npoints()
init_VHartree()
print_Npoints()
print(VHartree)

print('Program ended normally')


