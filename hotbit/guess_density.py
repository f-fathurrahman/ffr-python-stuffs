def guess_density(Z, rgrid):
    """ Guess initial density. """
    r2 = 0.02*Z # radius at which density has dropped to half; improve this!
    dens = np.exp( -rgrid/(r2/np.log(2)) )
    dens = dens/radialgrid_integrate( dens, rgrid,use_dV=True)*nel
    #pl.plot(self.rgrid,dens)
    return dens
