# from doc v 1.1.1, section 2.2.3:
# The power of symbolic computation

from sympy import *

init_printing(use_unicode=True)

x, t, z, nu = symbols("x t z nu")

# Calculate derivative
expr = diff( sin(x)*exp(x), x )
pprint(expr)

# Calculate integral
expr = integrate( exp(x)*sin(x) + exp(x)*cos(x), x )
pprint(expr)

# Another integral
expr = Integral( sin(x**2), (x, -oo, oo) )
pprint(expr)
pprint(expr.doit())

# Calculate limit
expr = Limit( sin(x)/x, x, 0 )
pprint(expr)
pprint(expr.doit())

# Defining an equation
eq = Eq( x**2 - 2, 0 )
sols = solve( eq, x )
pprint(eq)
pprint(sols)

# solve differential equation
# y'' - y = e**t
y = Function("y")
eq = Eq( y(t).diff(t,t) - y(t), exp(t) )
sols = dsolve( eq , y(t) )
pprint(eq)
pprint(sols)


# Find eigenvalues of a matrix
m = Matrix( [[1,2], [2, 2]] )
pprint(m)
pprint(m.eigenvals())
pprint(m.eigenvects())

# special functions: rewrite Bessel function in terms of spherical Bessel function
eq = besselj(nu, z).rewrite(jn)
pprint(eq)

# printing using LaTeX
print(latex(Integral(cos(x)**2*exp(x), (x,0,pi))))


