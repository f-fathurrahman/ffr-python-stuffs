configuration = {}
valence = []
confinement = None
xc = "PW92"
convergence = {"density":1E-7,"energies":1E-7}
scalarrel = False
rmax = 100.0
nodegpts = 500
mix =0.2
itmax = 200
timing = False
verbose = False
txt = None
restart = None
write = None

# element data
data = copy( atoms_data[symbol] )

Z = data["Z"]
if valence == []:
    valence = copy( atoms_data[symbol]["valence_orbitals"] )

print("Symbol = ", symbol)
print("Valence = ", valence)

# more specific
occu = copy( atoms_data[symbol]["configuration"] )
nel_neutral = Z

assert sum(occu.values()) == nel_neutral

occu.update( configuration )
print("Occupations = ", occu)

nel = sum(occu.values())
print("nel = ", nel)

charge = nel_neutral - nel
print("charge = ", charge)


"""
if self.confinement==None:
    self.confinement_potential=ConfinementPotential("none")
else:
    self.confinement_potential=ConfinementPotential(**self.confinement)
"""


conf=None
nucl=None
exc=None


# technical stuff
maxl = 9
maxn = 9
plotr = {}
unlg = {}
Rnlg = {}
unl_fct = {}
Rnl_fct = {}
veff_fct = None
total_energy = 0.0

maxnodes = max( [n-l-1 for n,l,nl in list_states(maxn,maxl,occu)] )

rmin, rmax, N=( 1E-2/Z, rmax, (maxnodes+1)*nodegpts )

if scalarrel:
    print("Using scalar relativistic corrections.")

print("max %i nodes, %i grid points" %(maxnodes,N))
print("rmin = ", rmin, " rmax = ", rmax)

xgrid = np.linspace(0,np.log(rmax/rmin),N)
rgrid = rmin*np.exp(xgrid)

#grid = RadialGrid(rgrid)
