#Calculating integrals----2(b):
import numpy as np
def integral(N):       #now I use function because we can control N
  h = 2/N
  sum = 0

  for k in range(1,N+1):        # k starts from 1 and end at N.
    x_k = -1 + h*k
    y_k = np.sqrt(1-x_k**2)
    product = h*y_k
    sum += product
  
  return(sum)

print(integral(10**(5)))

# Within one second, the best of my computer it can do is when N=10^5, and the value is roughtly 1.570796
