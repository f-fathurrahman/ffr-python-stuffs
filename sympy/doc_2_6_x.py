from sympy import *
init_printing(use_unicode=True)

x, y, z = symbols("x y z")

#
# `simplify`
#

eksp = sin(x)**2 + cos(x)**2
print()
pprint(eksp)
pprint(simplify(eksp))

eksp = sin(x)**2 + cos(x)**2 + tan(x)
print()
pprint(eksp)
pprint(simplify(eksp))

eksp = gamma(x)/gamma(x-3)
print()
pprint(eksp)
pprint(simplify(eksp))

eksp = x**2 + 2*x + 1
print()
pprint(eksp)
pprint(simplify(eksp))

#
# Polynomial / Rational Function Simplification
#

# Using `expand`

eksp = (x + 1)**2
print()
pprint(eksp)
pprint(expand(eksp))

eksp = (x + 1)*(x - 2) - (x - 1)*x
print()
pprint(eksp)
pprint(expand(eksp))

# using `factor`

eksp = x**3 - x**2 + x - 1
print()
pprint(eksp)
pprint(factor(eksp))

eksp = x**2*z + 4*x*y*z + 4*y**2*z
print()
pprint(eksp)
pprint(factor_list(eksp))

# using `expand` and `factor` for expressions other than polynomials
eksp = (cos(x) + sin(x))**2

print()
pprint(eksp)

eksp = expand(eksp)
pprint(eksp)

eksp = factor(eksp)
pprint(eksp)

# using `collect`

eksp = x*y + x - 3 + 2*x**2 - z*x**2 + x**3
print()
pprint(eksp)
eksp = collect(eksp, x)
pprint(eksp)
# use coeff
pprint(eksp.coeff(x,2))


