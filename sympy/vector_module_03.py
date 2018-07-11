from sympy import init_printing, pprint
init_printing(use_unicode=True)

# about `Points`

from sympy.vector import CoordSys3D

N = CoordSys3D("N")
pprint(N.origin)
print(type(N.origin))

# we can instantiate new points in space using locate_new method of `Point`
from sympy.abc import a, b, c

P = N.origin.locate_new("P", a*N.i + b*N.j + c*N.k)
Q = P.locate_new("Q", -b*N.j)

pprint(P)
pprint(Q)

# position vector
# v = P - Q
v = P.position_wrt(Q)
pprint(v)

v = Q.position_wrt(N.origin)
pprint(v)

v = P.position_wrt(N.origin)
pprint(v)

# We can obtain X, Y, Z coordinats of a Point wrt a CoordSys3D in the form
# of a tuple using `express_coordinates` method
pprint( P.express_coordinates(N) )
pprint( Q.express_coordinates(N) )


