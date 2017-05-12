import numpy as np
import math
from numpy import linalg
from matplotlib import pylab as plt

f = lambda x: np.sin(x/5.0)*np.exp(x/10.0) + 5.0 * np.exp(-x/2.0)


A = np.array([[1, 1], [15, 1]])
b = np.array([f(1), f(15)])

x = np.linalg.solve(A,b)
print x
print (np.dot(A,x) == b)

plt.plot(f(15))

x = 225
print x*15