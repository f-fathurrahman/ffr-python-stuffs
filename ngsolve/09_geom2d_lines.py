from netgen.geom2d import SplineGeometry

geo = SplineGeometry()

#pnts = [ (0,0), (1,0),
#         (1,0.5), (1,1),
#         (0.5,1), (0,1) ]

pnts = [ (0,0), # define a local mesh refinement for one point
         (1,0),
         (1,0.5), (1,1),
         (0.5,1), (0,1) ]

p1 = geo.AppendPoint(0,0)
p2 = geo.AppendPoint(1,0)
p3 = geo.AppendPoint(1,0.5)
p4 = geo.AppendPoint(1,1)
p5 = geo.AppendPoint(0.5,1)
p6 = geo.AppendPoint(0,1)

#geo.Append( ["line", p1, p2], maxh=0.02 )
#geo.Append( ["line", p2, p3] )
#geo.Append( ["line", p3, p6] )
#geo.Append( ["line", p6, p1] )

geo.Append( ["line", p1, p2] )
geo.Append( ["line", p2, p4] )
geo.Append( ["line", p4, p6] )
geo.Append( ["line", p6, p1] )

#ngmesh = geo.GenerateMesh(maxh=0.2)
ngmesh = geo.GenerateMesh(maxh=0.2, quad_dominated=True)