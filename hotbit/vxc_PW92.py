def vxc_PW92(n):
    """ Exchange-correlation potential (functional derivative of exc). """
    eps = 1E-9*n  # ???????
    SMALL = 1E-90
    if n < SMALL:
        return 0.0
    else:
        return exc_PW92(n) + n*exc_PW92(n,der=1)
