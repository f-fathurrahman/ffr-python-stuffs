from sympy import *

init_printing(use_unicode=True)

x, y, z = symbols("x y z")
f, g = symbols("f g", cls=Function)

# use differentiate_finite
eksp = differentiate_finite( f(x)*g(x) )
pprint(eksp)

eksp = differentiate_finite( f(x)*g(x), evaluate=True )
pprint(eksp)

dfdx = f(x).diff(x)
pprint(dfdx)
pprint(dfdx.as_finite_difference())

# use arbitrary order
h = symbols("h")
#
d2fdx2 = f(x).diff(x,2)
pprint(d2fdx2)
# use arbitrary step
pprint(d2fdx2.as_finite_difference([-3*h, -h, 2*h]))
#
pprint(d2fdx2.as_finite_difference()) # default
#
pprint(d2fdx2.as_finite_difference([-h,0,h]))

# for evaluating weights
pprint( finite_diff_weights(2, [-3, -1, 2], 0) )

