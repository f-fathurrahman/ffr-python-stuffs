def calculate_veff():
    """ Calculate effective potential. """
    for i in range(N):
        vxc[i] = vxc_PW92(dens[i])
    #
    return nucl + VHartree + vxc + conf
