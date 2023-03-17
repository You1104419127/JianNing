import numpy as np
from matplotlib import pyplot as plt
import sys  # in order to get epsilon zer0

# In the end, my function is phi(r) = q/(4*pi*epsilon*r) make a plot of r vs phi(r)

# In this 1 m by 1 m square plane, each point is separated by 1 unit of 10 cm, we have 100 points.
x_01 = 0    # x-coordinate of charge 1
x_02 = 1     # x-coordinate of charge 2
y_01 = 0     # y-coordinate of charge 1
y_02 = 0     # y-coordinate of charge 2

# We can use superposition theorem to sum two potentials to get the potential at a point due to 2 charges.
# However, for a same point, there are 2 distances, so it is better to use the distance of center of charges.

x_CM = 0.5   # x-coordinate of center of charges
y_CM = 0     # y-coordinate of center of charges

def distance1(x,y):    # distance between point and charge 1; x and y are the coordinates of point.
    distance = np.sqrt((x-x_01)**2 + (y-y_01)**2)
    return(distance)

def Potential1(distance):   # potential due to charge 1
    charge = 1
    return(charge/(4*np.pi*sys.float_info.epsilon*distance))

def distance2(x,y):    # distance between point and charge 2
    distance = np.sqrt((x-x_02)**2 + (y-y_02)**2) 
    return(distance)

def Potential2(distance):   # potential due to charge 2
    charge = -1
    return(charge/(4*np.pi*sys.float_info.epsilon*distance))

def distanceCM(x,y):    # distances between points and center of charges.
    distance = np.sqrt((x-x_CM)**2 + (y-y_CM)**2)
    return(distance)

plate = []

# create all points with their x,y values:

i = -5
while i <= 4:
    j = -5
    while j <= 4:
        plate.append(np.array((i,j)))
        j += 1
    i += 1

# now plate is a list that contains 100 nested arrays, each nested array contains the x,y value of each point
#    for example: plate[2][0] calls x-coordinate of third point. plate[2][1] calls y-coordinate of third point. 

dCM = []  # list for all distances between points and center of charges
dC1 = []   # list for distance associates with charge 1
dC2 = []   # list for distance associates with charge 2
potential1 = []  # list for all potentials due to charge 1.
potential2 = []  # list for all potentials due to charge 2.
for i in range(100):   # use FOR loop to find all distance
    d1 = distance1(plate[i][0], plate[i][1])
    d2 = distance2(plate[i][0], plate[i][1])
    dC1.append(d1)
    dC2.append(d2)
    dCM.append(distanceCM(plate[i][0], plate[i][1]))
    potential1.append(Potential1(d1))
    potential2.append(Potential2(d2))

potential1 = np.array(potential1)
potential2 = np.array(potential2)
dCM = np.array(dCM)    # these are radius

potential = potential1 + potential2

print(potential)

plt.plot(dC1, potential1, label = "charge 1 only")
plt.plot(dC2,potential2, label = "charge 2 only")
plt.scatter(dCM, potential, label = "potential due to 2 charges")
plt.xlabel("distance (10 centi-meters)")
plt.ylabel("potential (volt)")
plt.title("potential distribution due to two charges")
plt.legend()
plt.show()

