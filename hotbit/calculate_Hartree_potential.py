def calculate_Hartree_potential():
    """
    Calculate Hartree potential.

    Everything is very sensitive to the way this is calculated.
    If you can think of how to improve this, please tell me!

    """
    #dV = self.grid.get_dvolumes()
    N = len(rgrid)
    dr = rgrid[1:N] - rgrid[0:N-1]
    r0 = rgrid[0:N-1] + dr/2
    dV = 4*np.pi*r0**2 * dr
    dV *= (4*np.pi*rmax**3/3)/sum(dV)
    #
    n0 = 0.5*( dens[1:] + dens[:-1] )
    n0 *= nel/sum(n0*dV)

    lo, hi = np.zeros(N), np.zeros(N)
    lo[0] = 0.0
    for i in range(1,N):
        lo[i] = lo[i-1] + dV[i-1]*n0[i-1]

    hi[-1] = 0.0
    for i in range(N-2,-1,-1):
        hi[i] = hi[i+1] + n0[i]*dV[i]/r0[i]

    for i in range(N):
        VHartree[i] = lo[i]/rgrid[i] + hi[i]
