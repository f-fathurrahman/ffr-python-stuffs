from ngsolve import *
from netgen.geom2d import unit_square

ngsglobals.msg_level = 1

mesh = Mesh(unit_square.GenerateMesh(maxh=0.05))

# Define a function
#myfunc = x*(1 - x)
#myfunc = x + y
#myfunc = x*(1 - y**2)
myfunc = (x - 0.5)**2 + (y - 0.5)**2

# Visualize the function on the mesh
#Draw(myfunc, mesh, "MyFirstFunc")

mip = mesh(0.2, 0.2)
print(mip.pnt)
print(myfunc(mip))

# Calculate on several points
pts = [(0.1*i, 0.1) for i in range(10)]
vals = [myfunc(mesh(*p)) for p in pts]
for p,v in zip(pts, vals):
    print("point = (%18.10f,%18.10f), func val = %18.10f" % (p[0], p[1], v))

print(Integrate(myfunc, mesh)) # the result is number

diff_myfunc = myfunc.Diff(y)
print(diff_myfunc)
#Draw(diff_myfunc, mesh, "Derivative")


# Parameters in functions
k = Parameter(1.0)
f = sin(k*y)
#Draw(f, mesh, "f")

import math
# Using different value of k
k.Set(4*math.pi)
#Draw(f, mesh, "f")

print(f)
# differentiate w.r.t to parameter k
print(f.Diff(k))

print( Integrate( (f.Diff(k) - y*cos(k*y))**2, mesh ), " (should be close to zero)" )


# Interpolate a function

# We can set a GridFunction using a CoefficientFunction
fes = H1(mesh, order=2)
u = GridFunction(fes)
#u.Set(myfunc)
u.Set(myfunc.Diff(y))
#Draw(u)


# Vector valued CoefficientFunction
#vecfun = CoefficientFunction( (-y, sin(x)) )
vecfun = CoefficientFunction( (x, sin(x)) )
#Draw(vecfun, mesh, "vecfun")

# Gradient
u.Set(myfunc)
gradu = grad(u)
#Draw(gradu, mesh, "grad_firstfunc")

myfunc_compiled = myfunc.Compile()

print(myfunc)
print(myfunc_compiled)

#

f0 = myfunc
f1 = f0*y
f2 = f1*f1 + f1*f0 + f0*f0
f3 = f2*f2*f2*f0**2 + f0*f2**2 + f0**2 + f1**2 + f2**2
final = f3 + f3 + f3
finalc = final.Compile()

import time

t1 = time.time()
Integrate(finalc, mesh, order=10)
print("Elapsed (compiled) = %.5e" % (time.time() - t1))

t1 = time.time()
Integrate(final, mesh, order=10)
print("Elapsed = %.5e" % (time.time() - t1))
