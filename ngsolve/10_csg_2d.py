from netgen.geom2d import CSG2d, Circle, Rectangle

circle = Circle(center=(0,0), radius=1.0, mat="mat1", bc="bc_circle")
rect = Rectangle(pmin=(-0.5,0), pmax=(1.5,1.5), mat="mat2", bc="bc_rect")

domain1 = circle - rect # difference
domain2 = circle*rect # intersection
domain2.Mat("mat3").Maxh(0.1) # change domain name and mesh
domain3 = rect - circle

geo = CSG2d()
geo.Add(domain1)
geo.Add(domain2)
geo.Add(domain3)

m = geo.GenerateMesh(maxh=0.3)

# use NGSolve just for visualization
#from ngsolve.webgui import Draw
#from ngsolve import Mesh, VOL
#mesh = Mesh(m)
#mesh.Curve(3)
#cf = mesh.RegionCF(VOL, dict(mat1=0, mat2=4, mat3=7))
#Draw(cf, mesh)
