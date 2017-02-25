import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.0, 1.0 + 0.01, 0.01)
s = np.cos(4*np.pi*t) + 2
plt.plot(t, s, marker='o')
plt.xlabel(r'\textbf{time} (s)')
plt.ylabel('\\textit{Velocity (\u00B0/sec)}', fontsize=16)
plt.grid(True)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.title(r"\TeX\ is Number "
          r"$\displaystyle\sum_{n=1}^\infty\frac{-e^{i\pi}}{2^n}$!",
          fontsize=16, color='black')
plt.subplots_adjust(top=0.8)
plt.savefig('tex_demo_v1.pdf')
