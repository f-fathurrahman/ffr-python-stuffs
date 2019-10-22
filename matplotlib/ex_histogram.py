import numpy as np
import matplotlib.pyplot as plt

Npoints = 100000
Nbins = 20

x = np.random.randn(Npoints)
y = 0.4*x + np.random.randn(Npoints) + 5.0

figs, axs = plt.subplots(1,2, sharey=True, tight_layout=True)
axs[0].hist(x, bins=Nbins)
axs[1].hist(y, bins=Nbins)

plt.savefig("TEMP_ex_histogram.png", dpi=150)