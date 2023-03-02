import numpy as np
from matplotlib import pyplot as plt
# (3c):
theta = np.arange(0, 24*np.pi, 0.1)
r = np.e**(np.cos(theta)) - 2*np.cos(4*theta) + (np.sin(theta/12))**2
x = r*np.cos(theta)
y = r*np.sin(theta)
plt.figure(figsize=(8,5))
ax = plt.axes()
ax.set(xlabel='x', ylabel='y',title='Fey’s function')
plt.plot(x,y)
plt.show()
