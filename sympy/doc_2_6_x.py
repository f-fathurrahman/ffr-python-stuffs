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
# use `coeff`
pprint(eksp.coeff(x,2))

# using `cancel`

eksp = (x**2 + 2*x + 1)/(x**2 + x)
print()
pprint(eksp)
pprint(cancel(eksp))

eksp = 1/x + (3*x/2 - 2)/(x - 4)
print()
pprint(eksp)
pprint(cancel(eksp))

eksp = (x*y**2 - 2*x*y*z + x*z**2 + y**2 - 2*y*z + z**2)/(x**2 - 1)
print()
pprint(eksp)
eksp1 = cancel(eksp)
pprint(eksp1)

# `factor` also can be used to do the same thing
eksp2 = factor(eksp)
print()
pprint(eksp2)

print()
# check that eksp1 and eksp2 is the same
pprint(expand(eksp1 - eksp2))


# `apart` performs partial fraction decomposition on a rational function
eksp = (4*x**3 + 21*x**2 + 10*x + 12)/(x**4 + 5*x**3 + 5*x**2 + 4*x)
print()
pprint(eksp)
print("\nDoing partial fraction decomposition")
pprint(apart(eksp))

#
eksp = sin(x)**4 - 2*cos(x)**2 * sin(x)**2 + cos(x)**4
print()
print("\nOriginal expression:")
pprint(eksp)
print("\nAfter trigsimp:")
pprint(trigsimp(eksp))


