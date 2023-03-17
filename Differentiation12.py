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
    
sigma = 10**(-4)

def Electric_field1(r): # for charge 1
       k = -(Potential1(r+sigma)-Potential1(r-sigma)) / (2*sigma)
       k = int(k)          # round the number into integer
       return(k)

def Electric_field2(r): # for charge 1
       k = -(Potential2(r+sigma)-Potential2(r-sigma)) / (2*sigma)
       k = int(k)          # round the number into integer
       return(k)


# Since each point is separated by 1 cm at a 1 m by 1 m matrix, or a 1 D array of size of 10*4, we need a
#    100 by 100 matrix.

potential1 = [i for i in range(10**4)]
potential2 = [i for i in range(10**4)]
distance1 = [i for i in range(10**4)]
distance2 = [i for i in range(10**4)]

# Place two charges in the middle: they are 10 cm (10 unit of space) apart.

# In order to plot this, we need two array: one for distance (r) and one for potential.

# Distance: Since we have two distance for a same point, one for charge 1 (index 5550), 
#    another for charge 2 (index 5560), it is better to use distance that between the 
#    point and the center of charges. Center of charges has index of 555:

distanceCC = []# list of distance with respect to center of charges
for i in range(10**4):   
    distanceCC.append(distance(100,5555,i)/100)  # it has unit of 1 cm, we need meter. 1 cm = 0.01 m

distanceCC = np.array(distanceCC) # convert list into array

# Calculate potential due to charge 1 (index 550):

for i in range(10**4):
    i = i + 1 
    r = distance(100,5551,i)  # the imaginary matrix in function "distance" are starting with index 1 not 0,
                            #    index 5550 (matrix starts from 0) corresponds index 5551 (matrix starts with 1)
    r = r * 0.01   # because in our "imaginary" matrix, each element is 1 cm far away to each other
                  #      ,so r is the multiple of 10cm, we need meter: 1cm = 0.01m
    potential1[i-1] = Potential1(r)

# Calculate potential due to charge 1 (index 560):

for i in range(10**4):
    i = i + 1 
    r = distance(100,5561,i)  
    r = r * 0.01
    potential2[i-1] = Potential2(r)

potential1[550] = 0
potential1[560] = 0
potential2[550] = 0
potential2[560] = 0

potential1 = np.array(potential1)

potential2 = np.array(potential2)

potential = potential1 + potential2     # array for total potential

plt.plot(distanceCC, potential)
plt.xlabel("distance (m)")
plt.xlim(0,0.3)
plt.ylabel("potential (volt)")
plt.title("distribution of electric potential of two charges")
plt.legend()
plt.show()



