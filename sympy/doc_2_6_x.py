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
# trigonometric functions 
#

# `trigsimp`

eksp = sin(x)**4 - 2*cos(x)**2 * sin(x)**2 + cos(x)**4
print()
print("\nOriginal expression:")
pprint(eksp)
print("\nAfter trigsimp:")
pprint(trigsimp(eksp))


eksp = sin(x)*tan(x)/sec(x)
print()
print("\nOriginal expression:")
pprint(eksp)
print("\nAfter trigsimp:")
pprint(trigsimp(eksp))


eksp = cosh(x)**2 + sinh(x)**2
print()
print("\nOriginal expression:")
pprint(eksp)
print("\nAfter trigsimp:")
pprint(trigsimp(eksp))


eksp = sinh(x)/tanh(x)
print()
print("\nOriginal expression:")
pprint(eksp)
print("\nAfter trigsimp:")
pprint(trigsimp(eksp))

# `expand_trig`: apply the sum or double angle identities

eksp = sin(x + y)
print()
print("\nOriginal expression:")
pprint(eksp)
print("\nAfter expand_trig:")
pprint(expand_trig(eksp))

eksp = tan(2*x)
print()
print("\nOriginal expression:")
pprint(eksp)
print("\nAfter expand_trig:")
pprint(expand_trig(eksp))

eksp = sin(2*x)
print()
print("\nOriginal expression:")
pprint(eksp)
print("\nAfter expand_trig:")
pprint(expand_trig(eksp))

# trigsimp can be used to reverse these expansions

#
# Expression involving powers
#

# Introduce new symbol with assumption
x, y = symbols("x y", positive=True)
a, b = symbols("a b", real=True)
z, t, c = symbols("z t c")

# sqrt(x) is just a shortcut to x**Rational(1,2)
eq = sqrt(x) == x**Rational(1/2)
print()
pprint(eq)

# `powsimp`
eksp = x**a * x**b
print()
pprint(eksp)
pprint(powsimp(eksp))

eksp = x**a * y**a
pprint(eksp)
pprint(powsimp(eksp))

#
eksp = t**c * z**c
pprint(eksp)
pprint(powsimp(eksp))
# force it to do the simplification
pprint(powsimp(eksp,force=True))


eksp = (z*t)**2
pprint(eksp)

eksp = sqrt(x*y)
pprint(eksp)


# `expand_power_exp` and `expand_power_base`
# TODO


# `powdenest`
# TODO

#
# Exponentials and logarithm
#

# `expand_log`
# TODO

# `logcombine`
# TODO



#
# Special functions
#

# TODO


# `rewrite`
eksp = tan(x)
print()
print("\nRewriting tan(x) as sin(x)")
pprint(eksp.rewrite(sin))

# `expand_func`: expand special functions in terms of some identities

pprint(expand_func(gamma(x+3)))

pprint(expand_func(besselj(3,x)))

# `hyperexpand`
# TODO

# `combsimb`
# TODO


# Continued fractions
# TODO




