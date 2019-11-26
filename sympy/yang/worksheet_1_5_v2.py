from sympy import *

init_printing(use_unicode=True)

m1, m2 = symbols("m_1 m_2")
v1i, v2i = symbols("v_1i v_2i")
v1f, v2f = symbols("v_1f v_2f")


# Eq1 == 0
# Eq2 == 0
Eq1 = m1*v1i + m2*v2i - (m1*v1f + m2*v2f)
Eq2 = m1*v1i**2/2 + m2*v2i**2/2 - (m1*v1f**2/2 + m2*v2f**2/2)

solns = nonlinsolve( [Eq1, Eq2], [v1f, v2f] )

# solns.args[1] is the nontrivial solution

# need to simplify the first solution
pprint( simplify(solns.args[1][0]) )

pprint(solns.args[1][1])