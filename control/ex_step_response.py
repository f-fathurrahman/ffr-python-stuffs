from control import tf, step_response
import numpy as np
import matplotlib.pyplot as plt

responses = []

plt.clf()
for zeta in [0.0, 0.5, 0.8, 1.0, 1.2]:
    K = 1.0
    omega = 1.0
    #zeta = 1.0
    num = [K*omega**2]
    denum = [1.0, 2*zeta*omega, omega**2]
    sistem = tf(num, denum)
    resp = step_response(sistem, T=np.linspace(0,10.0,500))
    plt.plot(resp[0], resp[1], label='zeta='+str(zeta))

plt.grid()
plt.legend()
plt.savefig("TEMP_ex_step_response.pdf")