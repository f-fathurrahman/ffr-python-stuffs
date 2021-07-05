from ngsolve import *
from netgen.geom2d import unit_square
import matplotlib.pyplot as plt

mesh = Mesh(unit_square.GenerateMesh(maxh=0.2))

myfunc = x*(1-x)
Draw(myfunc, mesh, "firstfun")

# MappedIntegrationPoints
mip = mesh(0.2, 0.2)
print("mip = ", mip)
res = myfunc(mip)
print("res = ", res)

pts = [(0.1*i, 0.2) for i in range(10)]
vals = [myfunc(mesh(*p)) for p in pts]
for p, v in zip(pts, vals):
    print("point=(%3.2f,%3.2f), value=%6.5f" % (p[0], p[1], v))

# Test Matplotlib
#px = [0.01*i for i in range(100)]
#vals = [myfunc(mesh(p,0.5)) for p in px]
#plt.clf()
#plt.plot(px, vals)
#plt.xlabel("x")
#plt.grid(True)
#plt.savefig("IMG_myfun1.pdf")

print(myfunc)
res = Integrate(myfunc, mesh)
print(res)

myfunc_compiled = myfunc.Compile()
res = Integrate(myfunc_compiled, mesh)
print(res)