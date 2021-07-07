from ngsolve import *
from netgen.geom2d import unit_square

ngsglobals.msg_level = 1

mesh = Mesh(unit_square.GenerateMesh(maxh=0.2))
print(mesh.GetBoundaries())

fes = H1(mesh, order=2, dirichlet="left|right")
print(fes.ndof)

fes2 = H1(mesh, order=2)
print(fes2.ndof)

print("free dofs of fes2 without \"diriclet\" flag: \n", fes2.FreeDofs())
print("free dofs of fes without \"diriclet\" flag: \n", fes.FreeDofs())

g = sin(y) # on Γ_D
# interpolate g on the boundary of the domain and extend it to zero on the elements
# not having an intersection with Γ_D
gfu = GridFunction(fes)
gfu.Set(g, BND)
Draw(gfu)

# The keyword BND tells Set that g need only be interpolated on those parts of the boundary
# that are marked dirichlet.
# Thus, gfu now contains the  extension u_D.

u = fes.TrialFunction()
v = fes.TestFunction()

a = BilinearForm(fes, symmetric=True)
a += grad(u)*grad(v)*dx
a.Assemble()

f = LinearForm(fes)
f += 1*v*dx
f.Assemble()

r = f.vec.CreateVector()
r.data = f.vec - a.mat * gfu.vec

gfu.vec.data += a.mat.Inverse(freedofs=fes.FreeDofs())*r
#Draw(gfu)


# Automatic
gfu.Set(g, BND)
#c = Preconditioner(a, "local") # Jacobi preconditioner
c = Preconditioner(a, "direct") # sparse direct solver
c.Update()
solvers.BVP(bf=a, lf=f, gf=gfu, pre=c)  # solvers = ngsolve.solvers
Draw(gfu)


