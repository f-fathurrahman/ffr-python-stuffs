def list_states(maxn, maxl, occu):
    """ List all potential states {(n,l,'nl')}. """
    states = []
    for l in range(maxl+1):
        for n in range(1,maxn+1):
            nl = orbit_transform((n,l),string=True)
            if nl in occu:
                states.append((n,l,nl))
    return states
