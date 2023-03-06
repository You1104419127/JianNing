#Calculating derivatives---2.(b):
def f(x):
    y = x*(x-1)
    return(y)

def deri(sigma,x):
    k = (f(x+sigma)-f(x))/sigma
    return(k)

Sigma = [10**(-2),10**(-4),10**(-6),10**(-8),10**(-10),10**(-12),10**(-14)] #list for sigma
derivatives = []    #list for derivatives
x = 1
for sigma in Sigma:
    print(deri(sigma,x))
    derivatives.append(deri(sigma,x))

import numpy as np
import matplotlib.pyplot as plt

x = np.array(Sigma)  #we need array in plot not list.
y = np.array(derivatives)
plt.plot(x,y)
plt.xlabel("sigma(s)")
plt.ylabel("derivative(s)")
plt.title("sigma VS derivative")
plt.legend()
plt.show()

#From the figure, we can see that as sigma decreasing, the derivative is decresing but at the most left hand
# side, the line of function seems go vertically down. I guess: the probably due to the limited bit storage
# of python like 16-bits? When the number goes to small, it may has trouble.