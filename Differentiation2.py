import numpy as np

import matplotlib.pyplot as plt   # use to plot

import sys  # in order to get epsilon zero

# Copy necessary code from Differentiation1(1).py

def distance(n,C,T):
    side = 0
    D = 0
    R = 0
    distance = 0
    a = T % n
    b = C % n

    if a == 0:
        a = n
    if b == 0:
        b = n
    if a < b:
        side = "0"     # 0 means LEFT
        if T < C:
            D = (np.abs(T - C) - (np.abs(T - C) % n) ) / n
            R = np.abs(T - C) % n
            distance = np.sqrt(D**2 + R**2)
            return(distance)
        if T > C:
            D = (np.abs(T - C) - (np.abs(T - C) % n) ) / n
            D = D + 1
            R = np.abs(T - C) % n
            R = n - R
            distance = np.sqrt(D**2 + R**2)
            return(distance)
    elif a > b:
        side = "1"     # 1 means RIGHT
        if T > C:
            D = (np.abs(T - C) - (np.abs(T - C) % n) ) / n
            R = np.abs(T - C) % n
            distance = np.sqrt(D**2 + R**2)
            return(distance)
        if T < C:
            D = (np.abs(T - C) - (np.abs(T - C) % n) ) / n
            D = D + 1
            R = np.abs(T - C) % n
            R = n - R
            distance = np.sqrt(D**2 + R**2)
            return(distance)
    else:
        side = "2"     # 2 means same vertical line
        if T == C :
            distance = 0
            return(distance)
        else:
            R = 0
            D = (np.abs(T - C) - (np.abs(T - C) % n) ) / n
            distance = np.sqrt(D**2)
            return(distance)

def Potential1(r):  # for charge 1 with +1 Columb
    charge = 1
    try:              #   remember the distance for the charge itself is zero, we don't want to
                      #       divided a number by zero
        return(charge/(4*np.pi*sys.float_info.epsilon*r))
    except:
        return(0)

def Potential2(r):  # for charge 2 with -1 Columb
    charge = -1
    try:
        return(charge/(4*np.pi*sys.float_info.epsilon*r))
    except:
        return(0)
    
sigma = 10**(-6)

def Electric_field1(r): # for charge 1
       k = -(Potential1(r+sigma)-Potential1(r-sigma)) / (2*sigma)
       k = int(k)          # round the number into integer
       return(k)

def Electric_field2(r): # for charge 1
       k = -(Potential2(r+sigma)-Potential2(r-sigma)) / (2*sigma)
       k = int(k)          # round the number into integer
       return(k)


electric_field1 = [i for i in range(10**4)]
electric_field2 = [i for i in range(10**4)]

for i in range(10**4):
    i = i + 1 
    r = distance(100,5551,i)
    r = r * 0.01 
    electric_field1[i-1] = Electric_field1(r)

for i in range(100):
    i = i + 1 
    r = distance(10,5561,i) 
    r = r * 0.01 
    electric_field2[i-1] = Electric_field2(r)

electric_field1 = np.array(electric_field1)
electric_field2 = np.array(electric_field2)

electric_field = electric_field1 + electric_field2

distanceCC = []# list of distance with respect to center of charges
for i in range(10**4):   
    distanceCC.append(distance(100,5555,i)/100)  # it has unit of 1 cm, we need meter. 1 cm = 0.01 m

distanceCC = np.array(distanceCC) # convert list into array

plt.plot(distanceCC, electric_field)
plt.xlabel("distance")
plt.ylabel("electric potential")
plt.title("electric potential distribution")
plt.legend()
plt.show()