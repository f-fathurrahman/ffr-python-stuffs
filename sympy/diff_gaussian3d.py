from __future__ import print_function
from sympy import *

init_printing(use_unicode=True)

x, y, z, sigma = symbols("x y z sigma")

#c1 = 2*sigma**2
#cc1 = sqrt(2*pi*sigma**2)**3

c1, cc1 = symbols("c1 cc1")

r2 = x**2 + y**2 + z**2

f = exp(-r2/c1)/cc1

pprint(f)

print("Diff x:")
nabla_x = diff(f,x).subs( x**2 + y**2 + z**2, r2 )
pprint( nabla_x )

print("Diff y:")
nabla_y = diff(f,y).subs( x**2 + y**2 + z**2, r2 )
pprint( nabla_y )

print("Diff z:")
nabla_z = diff(f,z).subs( x**2 + y**2 + z**2, r2 )
pprint( nabla_z )

