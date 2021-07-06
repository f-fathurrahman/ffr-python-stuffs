# Solve Poisson equation:
# -∇^2 = f
# in the unit square
# with u = 0 on bottom and right parts of the boundary
# \frac{∂u}{∂n} = 0 for remaining boundary parts

from ngsolve import *
from netgen.geom2d import unit_square

ngsglobals.msg_level = 0 # suppress messages from netgen

# Unstructured mesh
#mesh = Mesh(unit_square.GenerateMesh(maxh=0.2)) # maximal mesh-size of 0.2
mesh = Mesh(unit_square.GenerateMesh(maxh=0.02)) # maximal mesh-size of 0.2
print("mesh.nv = ", mesh.nv)
print("mesh.ne = ", mesh.ne)

# Finite element space
#fes = H1(mesh, order=2, dirichlet="bottom|right") # Lagrange basis
fes = H1(mesh, order=2, dirichlet="bottom|left|top|right") # Lagrange basis
print("fes.ndof = ", fes.ndof)

# Test function and trial function are symbolic objects (for bilinear forms)
u = fes.TrialFunction()
v = fes.TestFunction()

# alternative
# u, v = fes.TnT() # trial and test function

# GridFunction represent functions in the finite element space and contains memory
# to hold coefficient vectors
gfu = GridFunction(fes)


# Define and assemble linear and bilinear forms
a = BilinearForm(fes, symmetric=True)
#a = a + grad(u)*grad(v)*dx # this expression is not supported
a += grad(u)*grad(v)*dx # this expression is not supported
a.Assemble()

f = LinearForm(fes)
#f += x*v*dx
#f += sin(x)*y*v*dx
f += y*v*dx
f.Assemble()

# Linear form vector
print(type(f.vec))
#print(f.vec)

# Stiffness matrix:
print(type(a.mat))
#print(a.mat)

# Solve the system
gfu.vec.data = a.mat.Inverse(freedofs=fes.FreeDofs()) * f.vec
# The argument fes.freeDofs() indicates that only remainig free dofs should
# participate in the linear solve

#print(gfu.vec)
Draw(gfu)

