import numpy as np

#
# theta''(t) + b*theta'(t) + c*sin(theta(t)) = 0
#
# omega(t) = theta'(t)
#
# theta'(t) = omega(t)
# omega'(t) = -b*omega(t) - c*sin(theta(t))

def pend(y, t, b, c):
    theta, omega = y
    dydt = [omega, -b*omega - c*np.sin(theta)]
    return dydt

b = 0.25
c = 5.0


# intitial conditions
y0 = [np.pi - 0.1, 0.0]

# 
t = np.linspace(0, 10, 101)

from scipy.integrate import odeint
sol = odeint(pend, y0, t, args=(b, c))




