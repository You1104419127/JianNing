import numpy as np
from matplotlib import pyplot as plt
# (3c):
theta = np.arange(0, 2*np.pi, 0.1)
x = 2*np.cos(theta) + np.cos(2*theta)
y = 2*np.sin(theta) - np.sin(2*theta)
plt.figure(figsize=(8,5))
ax = plt.axes()
ax.set(xlabel='x', ylabel='y',title='deltoid curve')
plt.plot(x,y)
plt.show()