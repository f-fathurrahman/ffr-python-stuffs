# about dyadics

from sympy.vector import CoordSys3D
from sympy import init_printing, pprint, latex

init_printing(use_unicode=True)

N = CoordSys3D("N")

# dyadics is formed by juxtaposition of pairs of vectors via
# outer products
#
# Operator | has been overloaded for outer

ij = N.i.outer(N.j)
pprint(ij)
print(latex(ij))

pprint( N.i | N.k )

dyad = N.i.outer(N.k)
pprint(dyad*3)

pprint(dyad - dyad)

pprint( dyad + 2*(N.j|N.i) )

# dot product
d = 3 * N.i.outer(N.j)
pprint( d.dot(d) )
pprint( d.dot(N.j|N.j) )





