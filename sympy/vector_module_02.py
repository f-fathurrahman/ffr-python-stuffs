from sympy import *
init_printing(use_unicode=True)
print()

from sympy.vector import CoordSys3D

N = CoordSys3D("N")

from sympy.abc import a, b, c

v = (a*b + a*c + b**2 + b*c)*N.i + (a**2 + 2*a*b + b**2)*N.j
pprint(v)
print()
print(latex(v))
print()
pprint(v.factor())

v = (sin(a)**2 + cos(a)**2)*N.i - (2*cos(b)**2 - 1)*N.k
print()
pprint(v)
print()
pprint(trigsimp(v))
print()
pprint(v.simplify())

print()
print(diff(v, b))

eksp = Derivative(v, b)
pprint(eksp)
pprint(eksp.doit())

v1 = a*N.i + sin(a)*N.j - N.k
eksp = Integral(v1, a)
pprint(eksp)
pprint(eksp.doit())



