import matplotlib as mpl

mpl.use("pgf")

pgf_with_rc_fonts = {
    "font.family" : "CMU Serif",
    "font.serif" : [],
    "font.sans-serif" : ["DejaVu Sans"],
}
mpl.rcParams.update(pgf_with_rc_fonts)

import matplotlib.pyplot as plt

plt.figure(figsize=(4.5,2.5))
plt.plot(range(5))
plt.text(0.5, 3., "serif")
plt.text(0.5, 2., "monospace", family="monospace")
plt.xlabel(u"μ is not $\\mu$")
plt.tight_layout(0.5)

plt.savefig("use_pgf.pdf")
