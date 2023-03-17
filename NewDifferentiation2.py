import numpy as np
from matplotlib import pyplot as plt

x_01 = 0    # x-coordinate of charge 1
x_02 = 1     # x-coordinate of charge 2
y_01 = 0     # y-coordinate of charge 1
y_02 = 0     # y-coordinate of charge 2
sigma = 10**(-2)    # infinitesimal
eps0 = 8.85*10**(12)

def Potential1(x,y):   # potential due to charge 1
    charge = 1
    try:            # because there are 2 distance is 0 (the charges themselves)
        distance = np.sqrt((x-x_01)**2 + (y-y_01)**2)   # distance between point and charge 1; 
                                                        #   x and y are the coordinates of point.
        return(charge/(4*np.pi*eps0*distance))
    except:
        return(0)

def Potential2(x,y):   # potential due to charge 2
    charge = -1
    distance = np.sqrt((x-x_02)**2 + (y-y_02)**2)  # distance between point and charge 2
    try:
        return(charge/(4*np.pi*eps0*distance))
    except:
        return(0)

def ParDeri_Poten1x(x,y):  # partial derivative of potential due to charge 1 with respect to x
    return( ( Potential1(x+sigma,y)-Potential1(x,y) ) / sigma )

def ParDeri_Poten1y(x,y):  # partial derivative of potential due to charge 1 with respect to y
    return( ( Potential1(x,y+sigma)-Potential1(x,y) ) / sigma )

def ParDeri_Poten2x(x,y):  # partial derivative of potential due to charge 2 with respect to x
    return( ( Potential2(x+sigma,y)-Potential2(x,y) ) / sigma )

def ParDeri_Poten2y(x,y):  # partial derivative of potential due to charge 2 with respect to y
    return( ( Potential2(x,y+sigma)-Potential2(x,y) ) / sigma )

def Electric_field1(x,y):  # electric field at point (x,y) due to charge 1
    a = []
    a.append(-ParDeri_Poten1x(x,y))
    a.append(-ParDeri_Poten1y(x,y))
    a = np.array(a)    # a is an array (vector), first element is - ∂φ/∂x , second element is - ∂φ/∂y 
                       #    where φ is potential.
    return(a)

def Electric_field2(x,y):  # electric field at point (x,y) due to charge 2
    b = []
    b.append(-ParDeri_Poten2x(x,y))
    b.append(-ParDeri_Poten2y(x,y))
    b = np.array(b)  
    return(b) 

def Electric_field(x,y):   # net electric field at point (x,y)
    return(Electric_field1(x,y) + Electric_field2(x,y))   # superposition theorem, E_net = E_1 + E_2

electric_field = []

# create all points with their x,y values:

x = -5
while x <= 4:
    y = -5
    while y <= 4:
        k = Electric_field(x,y)
        plt.plot(k)
        electric_field.append(k)
        y += 1
    x += 1

#$$$plt.show()

print(electric_field)


