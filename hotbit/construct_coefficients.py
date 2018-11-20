def construct_coefficients(l, eps):
    c = 137.036
    c2 = np.ones(N)
    if scalarrel == False:
        c0 = -2*( 0.5*l*(l+1) + rgrid**2*(veff-eps) )
        c1 = -np.ones(N)
    else:
        print('SHOULD NOT PASS HERE !!!')
        # from Paolo Giannozzi: Notes on pseudopotential generation
        #ScR_mass = array([1 + 0.5*(eps-V)/c**2 for V in self.veff])
        #c0 = -l*(l+1) - 2*ScR_mass*self.rgrid**2*(self.veff-eps) - self.dveff*self.rgrid/(2*ScR_mass*c**2)
        #c1 = self.rgrid*self.dveff/(2*ScR_mass*c**2) - 1
    return c0, c1, c2
