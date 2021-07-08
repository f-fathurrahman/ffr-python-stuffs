from netgen.geom2d import SplineGeometry

geo = SplineGeometry()
geo.AddRectangle(
    p1=(-1,-1), p2=(1,1), bc="rectangle",
    leftdomain=1, rightdomain=0
)
geo.AddCircle( c=(0,0), r=0.1, bc="circle", leftdomain=2, rightdomain=1 )
geo.SetMaterial(1, "outer")
geo.SetMaterial(2, "inner")
geo.SetDomainMaxH(2, 0.02)
ngmesh = geo.GenerateMesh(maxh=0.2)
