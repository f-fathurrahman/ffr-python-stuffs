from sympy import *

init_printing(use_unicode=True)

m1, m2 = symbols("m_1 m_2")
v1i, v2i = symbols("v_1i v_2i")
v1f, v2f = symbols("v_1f v_2f")

Eq1 = Equality( m1*v1i + m2*v2i, m1*v1f + m2*v2f )

Eq2 = Equality( m1*v1i**2/2 + m2*v2i**2/2, m1*v1f**2/2 + m2*v2f**2/2 )

v1f_tmp = solve(Eq2, v1f)[0]  # directly access the expr for v1f
pprint(v1f_tmp)

Eq1_s = Eq1.subs(v1f, v1f_tmp)
pprint(Eq1_s)

v2f_soln = solve(Eq1_s, v2f)[0]
pprint(v2f_soln)

# use Eq1 to find v1f
Eq1_s = Eq1.subs(v2f, v2f_soln)
v1f_soln = solve(Eq1_s, v1f)[0]
pprint(v1f_soln)

# if we start from solving Eq1, we will obtain trivial solution:
# v1f = v1i
# v2f = v2i