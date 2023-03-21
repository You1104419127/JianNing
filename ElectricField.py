import numpy as np

import matplotlib.pyplot as plt

x_1 = 0    # x coordinate of charge 1
y_1 = 0    # y coordinate of charge 1
x_2 = 1    # x coordinate of charge 2
y_2 = 0    # y coordinate of charge 2
eps0 = 8.85*(10**(-12))   # value of epsilon zero
sigma = 10*(-4)   # infinitesimal

def distance1(x,y):    # function that calculates distance between point and charge 1.
    r = np.sqrt( (x-x_1)**2 + (y-y_1)**2 )
    return(r)

def distance2(x,y):    # function that calculates distance between point and charge 2.
    r = np.sqrt( (x-x_2)**2 + (y-y_2)**2 )
    return(r)

def Potential1(x,y):   # function that calculates potential at point (x,y) due to charge 1.
    charge = 1
    try:     # for some distance = 0, it just the charge itslef
        p = (charge/(4*np.pi*eps0)) * (1/distance1(x,y))
    except:
        p = 0
    return(p)

def Potential2(x,y):   # function that calculates potential at point (x,y) due to charge 2.
    charge = -1
    try:
        p = (charge/(4*np.pi*eps0)) * (1/distance2(x,y))
    except:
        p = 0
    
    return(p)
    
def ParDeri_x1(x,y):  # partial derivative of potential with respect to x for charge 1.
    par = ( Potential1(x+sigma,y) - Potential1(x-sigma,y) ) / sigma
    return(par)

def ParDeri_x2(x,y):  # partial derivative of potential with respect to x for charge 2.
    par = ( Potential2(x+sigma,y) - Potential2(x-sigma,y) ) / sigma
    return(par)

def ParDeri_y1(x,y):  # partial derivative of potential with respect to y for charge 1.
    par = ( Potential1(x,y+sigma) - Potential1(x,y-sigma) ) / sigma
    return(par)

def ParDeri_y2(x,y):  # partial derivative of potential with respect to y for charge 2.
    par = ( Potential2(x,y+sigma) - Potential2(x,y-sigma) ) / sigma
    return(par)

#  electric field E = -∇φ = - ∂φ/∂x Î - ∂φ/∂y ĵ

def Electric_field1(x,y): # electric field at a point (x,y) due to charge 1.
    a = []
    a.append(-ParDeri_x1(x,y))
    a.append(-ParDeri_y1(x,y))
    a = np.array(a)
    return(a)

def Electric_field2(x,y): # electric field at a point (x,y) due to charge 2.
    b = []
    b.append(-ParDeri_x2(x,y))  
    b.append(-ParDeri_y2(x,y))
    b = np.array(b)
    return(b)

electric_field1 = []   # electric field due to charge 1.
electric_field2 = []   # electric field due to charge 2.
x = -5
while x < 5:
    y = -5
    while y < 5:
        electric_field1.append(Electric_field1(x,y))
        electric_field2.append(Electric_field2(x,y))
        y = y + 1
    x = x + 1

electric_field1 = np.array(electric_field1)
electric_field2 = np.array(electric_field2)

electric_field = electric_field1 + electric_field2   # superposition theorem

#$$$print(electric_field)  # now we have an array that contain 10,000 arrays (vectors; 1st element is x-value, 2nd
                       #   element is y-value)

x = -5
K = 0
while x < 5:
    y = -5
    while y < 5:
        origin = np.array([[x,x],[y,y]])  # orgin with respect to target point
        vector_array = Electric_field1(x,y) # show electric field due to charge 1.
        vector_list = vector_array.tolist()
        V = np.array([vector_list])
        plt.quiver(*origin, V[:,0], V[:,1])  
        y = y + 1
        K = K + 1
    x = x + 1
plt.show()

x = -5
K = 0
while x < 5:
    y = -5
    while y < 5:
        origin = np.array([[x,x],[y,y]])  # orgin with respect to target point
        vector_array = Electric_field2(x,y)   # show electric field due to charge 2.
        vector_list = vector_array.tolist()
        V = np.array([vector_list])
        plt.quiver(*origin, V[:,0], V[:,1])  
        y = y + 1
        K = K + 1
    x = x + 1
plt.show()

x = -5
K = 0
empty = 0   # used to specify the charges' location. This is not important.
while x < 5:
    y = -5
    while y < 5:
      if y == 0:

        if x == 0:
          empty += 1
        elif x == 1:
          empty += 1
        else:
           origin = np.array([[x,x],[y,y]])  # orgin with respect to target point
           vector_array = np.array( Electric_field2(x,y) + Electric_field1(x,y) )   # show electric field due to charges.
           vector_list = vector_array.tolist()
           V = np.array([vector_list])
           plt.quiver(*origin, V[:,0], V[:,1])  
      else:
           origin = np.array([[x,x],[y,y]])  # origin with respect to target point
           vector_array = Electric_field2(x,y) + Electric_field1(x,y)  # show electric field due to charges.
           vector_list = vector_array.tolist()
           V = np.array([vector_list])
           plt.quiver(*origin, V[:,0], V[:,1])

      y = y + 1
      K = K + 1
    x = x + 1
plt.show()

print(electric_field1)
print( )
print( )
print(electric_field2) 
print( )
print( )
print(electric_field)   # x-coordinates are positive and dominated, they are much greater than y-coordinates.
print(electric_field1[0])
print(electric_field2[0])  

