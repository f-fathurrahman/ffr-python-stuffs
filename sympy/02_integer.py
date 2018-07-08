from sympy import *

a = Integer(12345678901234)/Integer(123451)
pprint(a)
print(type(a))
print(a.evalf()) # nilai numerik

b = Integer(4561)/Integer(3451)
pprint(a + b)
