from netgen.geom2d import SplineGeometry

geo = SplineGeometry()
geo.AddRectangle( (-1,-1), (1,1), bc="rectangle" )
geo.AddCircle( (0,0), 0.5, bc="circle" )
ngmesh = geo.GenerateMesh(maxh=0.1)
