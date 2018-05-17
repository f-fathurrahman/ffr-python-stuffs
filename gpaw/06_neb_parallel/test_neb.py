from ase.build import fcc100, add_adsorbate
from ase.calculators.emt import EMT
from ase.optimize import QuasiNewton
from ase.io import read, Trajectory
from ase.constraints import FixAtoms
from ase.neb import NEB
from ase.optimize import BFGS
from ase.parallel import rank, size

from gpaw import GPAW

# 2x2-Al(001) surface with 3 layers and an
# Au atom adsorbed in a hollow site:
slab = fcc100('Al', size=(2, 2, 3))
add_adsorbate(slab, 'Au', 1.7, 'hollow')
slab.center(axis=2, vacuum=4.0)

# Make sure the structure is correct:
#view(slab)

# Fix second and third layers:
mask = [atom.tag > 1 for atom in slab]
#print(mask)
slab.set_constraint(FixAtoms(mask=mask))

# Use EMT potential:
slab.set_calculator(EMT())

# Initial state:
qn = QuasiNewton(slab, trajectory='initial.traj')
qn.run(fmax=0.05)

# Final state:
slab[-1].x += slab.get_cell()[0, 0] / 2
qn = QuasiNewton(slab, trajectory='final.traj')
qn.run(fmax=0.05)

# -------------------------------------------------------------------

initial = read('initial.traj')
final = read('final.traj')

constraint = FixAtoms(mask=[atom.tag > 1 for atom in initial])

n = size // 3      # number of cpu's per image
j = 1 + rank // n  # my image number
assert 3 * n == size

images = [initial]

for i in range(3):

    ranks = range(i * n, (i + 1) * n)
    image = initial.copy()

    if rank in ranks:

        calc = GPAW(h=0.3,
                    kpts=(2, 2, 1),
                    txt='neb%d.txt' % j,
                    communicator=ranks)
        
        image.set_calculator(calc)
        
    image.set_constraint(constraint)
    images.append(image)
    
images.append(final)

neb = NEB(images, parallel=True, climb=True)
neb.interpolate()

qn = BFGS(neb, logfile='qn.log')

traj = Trajectory('neb%d.traj' % j, 'w', images[j],
                  master=(rank % n == 0))

qn.attach(traj)
qn.run(fmax=0.05)

