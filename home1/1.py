import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize

x = np.array([0, 1, 2, 3, 4], dtype=np.float32)
y = np.array([1.9, 3.1, 3.9, 5.0, 6.2], dtype=np.float32)

def predict(a, xt):
    return a[0] + a[1] * xt

def MSE(a, x, y):
    total = 0
    for i in range(len(x)):
        total += (y[i] - predict(a, x[i]))**2
    return total

def loss(p):
    return MSE(p, x, y)

def optimize():
    p = minimize(loss, [0, 0]).x
    return p

p = optimize()
y_predicted = predict(p, x)

plt.plot(x, y, 'ro', label='Original data')
plt.plot(x, y_predicted, label='Fitted line')
plt.legend()
plt.show()
