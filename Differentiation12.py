import numpy as np

import matplotlib.pyplot as plt

import sys  # in order to get epsilon zero

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
    
potential1 = [i for i in range(10**4)]

for i in range(10**4):
    r = distance(100,5540,i)  
    r = r * 0.01      # 1 cm = 0.01 m
    potential1[i] = Potential1(r)

potential2 = [i for i in range(10**4)]

for i in range(10**4):    
    r = distance(100,5550,i) 
    r = r * 0.01
    potential2[i] = Potential2(r)

potential1 = np.array(potential1)

potential2 = np.array(potential2)

potential = potential1 + potential2   # superposition theorem

potential = np.reshape(potential,(100,100))

ax = plt.axes(projection='3d')

ax = plt.axes(projection='3d')

x = np.linspace(-50,49,100)  # create x-coordinates of points

y = np.linspace(-50,49,100)  # create y-coordinates of points

z = potential

ax.contour3D(x, y, z, 100)

plt.show()
