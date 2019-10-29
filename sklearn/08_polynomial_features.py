import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

def f(x):
    return x*np.sin(x)


x_plot = np.linspace(0.0, 10.0, 100)

# select subpoints
x = np.linspace(0.0, 10.0, 100)
rng = np.random.RandomState(0)
rng.shuffle(x)
# 20 first points
x = np.sort(x[:20])

y = f(x) # evaluate y (for target)

# made x and x_plot column vectors
X = x[:,np.newaxis]
X_plot = x_plot[:,np.newaxis]

print(X.shape)
print(X_plot.shape)

colors = ["teal", "yellowgreen", "gold"]
lw = 2
plt.plot(x_plot, f(x_plot), color="cornflowerblue", linewidth=lw, label="ground truth")
plt.scatter(x, y, color="navy", s=30, marker="o", label="training points")

for count, degree in enumerate([3, 4, 5]):
    model = make_pipeline( PolynomialFeatures(degree), Ridge() )
    model.fit(X, y)
    y_plot = model.predict(X_plot)
    plt.plot(x_plot, y_plot, color=colors[count], linewidth=lw, label="degree %d" % degree)

plt.legend(loc="lower left")

plt.savefig("08_polynomial_features.pdf")



