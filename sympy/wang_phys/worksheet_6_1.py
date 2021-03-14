from sympy import *

init_printing(use_latex=True)

x2, z1 = symbols("x2 z1", real=True)
λ = symbols("lambda", real=True, positive=True)
L = symbols("L", real=True)

r2vec = Matrix([x2, 0, 0]) # column matrix or vector
r1vec = Matrix([0, 0, z1])
r12vec = r1vec - r2vec

e12 = r12vec.normalized()
r12 = abs(r12vec.norm())

Ez = integrate( λ*e12[2]/r12**2, (x2, 0, L) )
pprint("Ez = ")
print(Ez)
#pprint(Ez.subs({z1: 0.1, L: 2.0}))


# SymPy had difficulties dealing with this
# We substitute numerical values instead.
L = 2.0
Ex = integrate( λ*e12[0]/r12**2, (x2, 0, 2.0) )
pprint("Ex = ")
pprint(Ex.subs({z1: 0.1}))
