#Calculating integrals----1(a):
import numpy as np
N = 100  # N is a modifiable variable
h = 2/N
sum = 0

for k in range(1,N+1):        # k starts from 1 and end at N.
    x_k = -1 + h*k
    y_k = np.sqrt(1-x_k**2)
    product = h*y_k
    sum += product

print(sum)

#The answer is roughtly 1.56913 while is close to the true answer but not perfect of course.