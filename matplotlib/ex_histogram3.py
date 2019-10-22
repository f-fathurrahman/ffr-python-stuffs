import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use("classic")

Npoints = 100000
Nbins = 20

sigma = 2.5
mu = -1.5

#x = np.random.randn(Npoints)
x = sigma*np.random.randn(Npoints) + mu

count, bins, ignored = plt.hist(x, bins=Nbins, density=True)

y_normal = 1/(sigma * np.sqrt(2 * np.pi))*np.exp( - (bins - mu)**2 / (2 * sigma**2) )
plt.plot( bins, y_normal, linewidth=1, color="red", marker="o")



TOL = 1e-2
print("Verify mean = ", abs(mu - np.mean(x)) < TOL)
print("Verify variance = ", abs(sigma - np.std(x, ddof=1)) < TOL)

plt.grid()
plt.savefig("TEMP_ex_histogram3.png", dpi=150)