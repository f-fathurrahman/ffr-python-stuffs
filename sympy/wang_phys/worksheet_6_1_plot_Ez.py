import numpy as np
import matplotlib.pyplot as plt

def calc_Ez(z1, λ, L=1.0):
    t1 = L*λ*abs(z1)
    t2 = z1**2 * np.sqrt(L**2 + z1**2)
    return t1/t2

z = np.linspace(0.1, 2.0, 1000)
plt.clf()
plt.plot(z, calc_Ez(z, 1.0), label="λ=1.0")
plt.plot(z, calc_Ez(z, 2.0), label="λ=2.0")
plt.plot(z, calc_Ez(z, 3.0), label="λ=3.0")
plt.legend()
plt.ylabel("Ez")
plt.xlabel("z")
plt.grid(True)
plt.tight_layout()
plt.savefig("IMG_worksheet_6_1_plot_Ez.png", dpi=150)

z = 0.5
print(calc_Ez(z, 1.0))
print(calc_Ez(z, 2.0))
print(calc_Ez(z, 3.0))

print(calc_Ez(z, 2.0)/calc_Ez(z, 1.0))
print(calc_Ez(z, 3.0)/calc_Ez(z, 1.0))


z = np.linspace(0.1, 2.0, 1000)
plt.clf()
plt.plot(z, calc_Ez(z, 1.0, L=0.1), label="L=0.1")
plt.plot(z, calc_Ez(z, 1.0, L=1.0), label="L=1.0")
plt.plot(z, calc_Ez(z, 1.0, L=10.0), label="L=10.0")
plt.legend()
plt.ylabel("Ez")
plt.xlabel("z")
plt.grid(True)
plt.tight_layout()
plt.savefig("IMG_worksheet_6_1_plot_Ez_L.png", dpi=150)

print()
print("effect of L")
z = 0.5
λ = 1.0
E1 = calc_Ez(z, λ, L=0.1)
print(E1)
E2 = calc_Ez(z, λ, L=0.2)
print(E2)
print(E2/E1)

print()
E1 = calc_Ez(z, λ, L=1.0)
print(E1)
E2 = calc_Ez(z, λ, L=2.0)
print(E2)
print(E2/E1)

print()
E1 = calc_Ez(z, λ, L=10.0)
print(E1)
E2 = calc_Ez(z, λ, L=20.0)
print(E2)
print(E2/E1)