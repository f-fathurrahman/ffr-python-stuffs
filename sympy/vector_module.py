from sympy import *
init_printing(use_unicode=True)

from sympy.vector import CoordSys3D

N = CoordSys3D("N")
print(type(N))

# access orthonormal unit vectors: i, j, k
pprint(N.i)
print(latex(N.i))

pprint(N.j)
print(latex(N.j))

pprint(N.k)
print(latex(N.k))

# BaseVector
eksp = 3*N.i
print(type(eksp))

#
v = 2*N.i + N.j
pprint(v)
print(type(v))
print(latex(v))

v2 = v - 3*N.j + 4*N.k
pprint(v2)

# zero vector
from sympy.vector import Vector
print(Vector.zero)
print(latex(Vector.zero))

print(Vector.zero == 2*Vector.zero)


# some operations with vector
pprint( 2*N.i + 3/2*N.j )

# dot and cross product
v1 = 2*N.i + 3*N.j - N.k
v2 = N.i - 4*N.j + N.k

print("\nTesting dot product")
pprint(v1.dot(v2))
pprint(v2.dot(v1))
pprint(v1.dot(v1))
pprint(v2.dot(v2))

print("\nTesting cross product")
pprint(v1.cross(v2))
pprint(v2.cross(v1))
pprint(v1.cross(v1))

# Overloaded operator: & (dot product)
#                      ^ (cross product)
pprint( v1 & v2 )
pprint( v1 & v1 )
pprint( v2 & v2 )

pprint( v1 ^ v2 )







