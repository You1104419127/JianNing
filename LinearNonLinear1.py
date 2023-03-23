import numpy as np
import matplotlib.pyplot as plt

m = 9.1094*10**(-31)

w = 1 * 10**(-9)

hbar = 1.054571817*10**(-34) 

V = 20

E = np.linspace(0,20,100)

y1 = np.tan( np.sqrt(w**2 * m * E / (2*hbar**2)) )

y2 = np.sqrt( (V - E) / E )

y3 = -np.sqrt(E / (V - E))

plt.plot(E, y1, color = 'red', label = '$y1$')
plt.plot(E, y2, color = 'blue', label = '$y2$')
plt.plot(E, y3, color = 'green', label = '$y3$')
plt.xlabel("$E$ (energy)")
plt.ylabel("y")
plt.legend()
plt.show()