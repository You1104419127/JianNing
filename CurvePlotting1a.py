import numpy as np
from matplotlib import pyplot as plt
# (2b):
theta = np.arange(0, 10*np.pi, 0.1)
r = theta**2
x = r*np.cos(theta)
y = r*np.sin(theta)
plt.figure(figsize=(8,5))
ax = plt.axes()
ax.set(xlabel='x', ylabel='y',title='Galilean spiral')
plt.plot(x,y)
plt.show()