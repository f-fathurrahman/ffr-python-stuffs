def B(x, k, i, t):
    if k == 0:
       return 1.0 if t[i] <= x < t[i+1] else 0.0
    if t[i+k] == t[i]:
       c1 = 0.0
    else:
       c1 = (x - t[i])/(t[i+k] - t[i]) * B(x, k-1, i, t)
    if t[i+k+1] == t[i+1]:
       c2 = 0.0
    else:
       c2 = (t[i+k+1] - x)/(t[i+k+1] - t[i+1]) * B(x, k-1, i+1, t)
    return c1 + c2

def bspline(x, t, c, k):
    n = len(t) - k - 1
    assert (n >= k+1) and (len(c) >= n)
    return sum(c[i] * B(x, k, i, t) for i in range(n))


from scipy.interpolate import BSpline

# Here we construct a quadratic spline function on the base interval 2 <= x <= 4
# and compare with the naive way of evaluating the spline:
k = 3
t = [0, 1, 2, 3, 4, 5, 6, 7, 8]
c = [-1, 2, 0, -1,]
spl = BSpline(t, c, k)
print("scipy: ", spl(2.5))
print("Naive: ", bspline(2.5, t, c, k))

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
xx = np.linspace(1.5, 4.5, 50)
ax.plot(xx, [bspline(x, t, c ,k) for x in xx], 'r-', label='naive')
ax.plot(xx, spl(xx), 'b-', alpha=0.7, label='BSpline')
ax.grid(True)
ax.legend(loc='best')
plt.savefig("TEMP_test_bspline.pdf")