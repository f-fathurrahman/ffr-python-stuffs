from sympy import *

init_printing(use_unicode=True)

x, y = symbols("x y")

expr = x + 2*y + 3*x
print(expr)

expr = (2*x + 3)*x - 2*x**2
print(expr)

pprint(expand(expr))

expr =(2*x+1)**2 * (3*y - 1)
pprint( expr )
pprint( expand(expr) )
pprint( collect(expand(expr),x) )
pprint( factor(expand(expr) ) )

