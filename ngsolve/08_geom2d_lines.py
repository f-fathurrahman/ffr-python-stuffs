from netgen.geom2d import SplineGeometry

geo = SplineGeometry()

#pnts = [ (0,0), (1,0),
#         (1,0.5), (1,1),
#         (0.5,1), (0,1) ]

pnts = [ (0,0,0.01), # define a local mesh refinement for one point
         (1,0),
         (1,0.5), (1,1),
         (0.5,1), (0,1) ]


p1,p2,p3,p4,p5,p6 = [geo.AppendPoint(*pnt) for pnt in pnts]

curves = [
    [ ["line",p1,p2], "bottom" ],
    [ ["line",p2,p3], "right" ],
    [ ["spline3",p3,p4,p5], "curve" ],
    [ ["line",p5,p6], "top" ],
    [ ["line",p6,p1], "left" ]
]
[geo.Append(c,bc=bc) for c,bc in curves]

ngmesh = geo.GenerateMesh(maxh=0.1)
