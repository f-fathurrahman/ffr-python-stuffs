def radialgrid_integrate(f, rgrid, use_dV=False):
    """
    Integrate function f (given with N grid points).
    int_rmin^rmax f*dr (use_dv=False) or int_rmin^rmax*f dV (use_dV=True)
    """
    N = len(rgrid)
    dr = rgrid[1:N] - rgrid[0:N-1]
    r0 = rgrid[0:N-1] + dr/2
    # first dV is sphere (treat separately), others are shells
    dV = 4*np.pi*r0**2 * dr
    dV *= (4*np.pi*rmax**3/3)/sum(dV)
    if use_dV:
        return ( (f[0:N-1]+f[1:N])*dV).sum()*0.5
    else:
        return ( (f[0:N-1]+f[1:N])*dr).sum()*0.5
