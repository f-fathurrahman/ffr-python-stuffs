from sympy import *

init_printing(use_unicode=True)

x, y = symbols("x y")

eksp = x + 2*y + 3*x
print(eksp)

eksp = (2*x + 3)*x - 2*x**2
print(eksp)

pprint(expand(eksp))

eksp =(2*x+1)**2 * (3*y - 1)
pprint( eksp )
pprint( expand(eksp) )
pprint( collect(expand(eksp),x) )
pprint( factor(expand(eksp) ) )

