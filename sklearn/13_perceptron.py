import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import Perceptron

iris = load_iris()
X = iris.data[:,(2,3)] # petal length, petal width
y = (iris.target == 0).astype(np.int)

model = Perceptron()
model.fit(X, y)
print(model)

y_pred = model.predict([[2.0, 0.5]])
print(y_pred)

y_pred = model.predict([[3.0, 1.5]])
print(y_pred)