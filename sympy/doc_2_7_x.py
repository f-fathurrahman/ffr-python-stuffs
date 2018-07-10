from sympy import *

init_printing(use_unicode=True)

x, y, z = symbols("x y z")

# derivatives

eksp = diff(cos(x), x)
pprint(eksp)

eksp = diff(exp(x**2), x)
pprint(eksp)

# multiple derivatives
eksp = diff(x**4, x, x, x)
pprint(eksp)

# alternative way
eksp = diff(x**4, x, 3)
pprint(eksp)

# multivariable derivatives
eksp = exp(x*y*z)
pprint( diff(eksp, x, y, y, z, z, z, z) )
pprint( diff(eksp, x, y, 2, z, 4) )
pprint( diff(eksp, x, y, y, z, 4) )

# `diff` also can be called as a method
pprint( eksp.diff(x, y, y, z, 4) )

# `Derivative` class can be used as unevaluated derivative
deriv = Derivative(eksp, x, y, y, z, 4)
pprint(deriv)
# to evaluate it, use the `doit` method
pprint(deriv.doit())


#
# Integration
#

# indefinite integral
eksp = integrate(cos(x), x)
pprint(eksp)
# Note that SymPy does not include constant of integration

# Definite integral
eksp = integrate(exp(-x), (x,0,oo))
pprint(eksp)

# multiple integrals
eksp = integrate( exp(-x**2 - y**2), (x,-oo,oo), (y,-oo,oo) )
pprint(eksp)


eksp = integrate( x**2 * exp(-x**2), (x,-oo,oo) )
pprint(eksp)


# If integrate is unable to compute an integral, it returns an
# unevaluated Integral object
eksp = integrate(x**x, x)
pprint(eksp)

# unevaluated integral
eksp = Integral( log(x)**2, x )
pprint(eksp)
pprint(eksp.doit())

# other examples

eksp = Integral((x**4 + x**2*exp(x) - x**2 - 2*x*exp(x) - 2*x -
                exp(x))*exp(x)/((x - 1)**2*(x + 1)**2*(exp(x) + 1)), x)
pprint(eksp)
pprint(eksp.doit())

eksp = Integral(sin(x**2), x)
pprint(eksp)
pprint(eksp.doit())

eksp = Integral(x**y*exp(-x), (x, 0, oo))
pprint(eksp)
pprint(eksp.doit())


#
# Limit
#

# `limit` or `Limit`

eksp = limit( sin(x)/x, x, 0 )
pprint(eksp)

# `limit` should be used whenever the point of evaluation is a singularity
eksp = x**2/exp(x)
pprint( eksp.subs(x, oo) )
pprint( limit(eksp, x, oo) )

eksp = Limit( (cos(x) - 1)/x, x, 0 )
pprint(eksp)
pprint(eksp.doit())

# One-sided limit
eksp = Limit( 1/x, x, 0, "+" )
pprint(eksp)
pprint(eksp.doit())

eksp = Limit( 1/x, x, 0, "-" )
pprint(eksp)
pprint(eksp.doit())

#
# Series expansion
#

# use `series`

eksp = exp(sin(x))
pprint(eksp.series(x, 0, 4))
pprint(eksp.series(x, pi, 4))
pprint(eksp.series(x, -pi, 4))

# O automatically absorbs higher order term
eksp = x + x**3 + x**6 + O(x**4)
pprint(eksp)

eksp = x*O(1)
pprint(eksp)

# `removeO` can be used to remove O
pprint( exp(sin(x)).series(x,0,4).removeO() )

# O notation supports arbitrary limit points other than 0:
eksp = exp(x - 6).series(x, x0=6)
pprint(eksp)



