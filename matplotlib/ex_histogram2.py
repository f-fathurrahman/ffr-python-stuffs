import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use("seaborn")

mu, sigma = 0, 0.1 # mean and standard deviation
s = np.random.normal(mu, sigma, 1000)

Nbins = 30
count, bins, ignored = plt.hist(s, Nbins, density=True) # normalized histogram

y_normal = 1/(sigma * np.sqrt(2 * np.pi))*np.exp( - (bins - mu)**2 / (2 * sigma**2) )
plt.plot( bins, y_normal, linewidth=2, color="r")

plt.savefig("TEMP_ex_histogram2.png", dpi=150)