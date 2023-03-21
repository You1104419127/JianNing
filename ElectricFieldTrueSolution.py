import numpy as np

import matplotlib.pyplot as plt

x_1 = -1    # x coordinate of charge 1
y_1 = -1    # y coordinate of charge 1
x_2 = 0    # x coordinate of charge 2
y_2 = -1    # y coordinate of charge 2
eps0 = 8.85*(10**(-12))   # value of epsilon zero
charge1 = 1
charge2 = -1
k1 = charge1/(4*np.pi*eps0)   # constant coefficient for charge 1.
k2 = charge2/(4*np.pi*eps0)   # constant coefficient for charge 2.

def distance1(x,y):    # function that calculates distance between point and charge 1.
    r = np.sqrt( (x-x_1)**2 + (y-y_1)**2 ) * 0.1  # r was in unit of 10 cm since 
                           #   100 points in a 1 m by 1 m plate
    return(r)

def distance2(x,y):    # function that calculates distance between point and charge 2.
    r = np.sqrt( (x-x_2)**2 + (y-y_2)**2 ) * 0.1
    return(r)



#### check my email to see the derivation of partial derivatives:



def Potential1(x,y):   # function that calculates potential at point (x,y) due to charge 1.
    charge = 1
    try:     # for some distance = 0, it just the charge itslef
        p = k1 * (distance1(x,y))**(-1)
    except:
        p = 0
    return(p)

def Potential2(x,y):   # function that calculates potential at point (x,y) due to charge 2.
    charge = -1
    try:
        p = k2 * (distance2(x,y))**(-1)
    except:
        p = 0
    
    return(p)
    
def NParDeri_x1(x,y):  # negative partial derivative of potential with respect to x for charge 1.
    if x == x_1:  # avoiding to find the information about the charges themseles
      if y == y_1:
        par = 0
      else:
        par = k1 * (x-x_1) *  ( (x-x_1)**2 + (y-y_1)**2 )**(-3/2)
    else:
      par = k1 * (x-x_1) *  ( (x-x_1)**2 + (y-y_1)**2 )**(-3/2)
    return(par)

def NParDeri_x2(x,y):  # negative partial derivative of potential with respect to x for charge 2.
    if x == x_2:
      if y == y_2:
        par = 0
      else:
        par = k2 * (x-x_2) *  ( (x-x_2)**2 + (y-y_2)**2 )**(-3/2)
    else:
      par = k2 * (x-x_2) *  ( (x-x_2)**2 + (y-y_2)**2 )**(-3/2)
    return(par)

def NParDeri_y1(x,y):  # negative partial derivative of potential with respect to y for charge 1.
    if x == x_1:
      if y == y_1:
        par = 0
      else:
        par = k1 * (y-y_1) *  ( (x-x_1)**2 + (y-y_1)**2 )**(-3/2)
    else:
      par = k1 * (y-y_1) *  ( (x-x_1)**2 + (y-y_1)**2 )**(-3/2)
    return(par)

def NParDeri_y2(x,y):  # negative partial derivative of potential with respect to y for charge 2.
    if x == x_2:
      if y == y_2:
        par = 0
      else:
        par = k2 * (y-y_2) *  ( (x-x_2)**2 + (y-y_2)**2 )**(-3/2)
    else:
      par = k2 * (y-y_2) *  ( (x-x_2)**2 + (y-y_2)**2 )**(-3/2)
    return(par)

#  electric field E = -∇φ = - ∂φ/∂x Î - ∂φ/∂y ĵ

def Electric_field1(x,y): # electric field at a point (x,y) due to charge 1.
    a = []
    a.append(NParDeri_x1(x,y))
    a.append(NParDeri_y1(x,y))
    a = np.array(a)
    return(a)

def Electric_field2(x,y): # electric field at a point (x,y) due to charge 2.
    b = []
    b.append(NParDeri_x2(x,y))  
    b.append(NParDeri_y2(x,y))
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
plt.xlim(-6,5) 
plt.ylim(-6,5)
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
plt.xlim(-6,5) 
plt.ylim(-6,5)
plt.show()

x = -5
K = 0
empty = 0   # used to specify the charges' location. This is not important.
while x < 5:
    y = -5
    while y < 5:
      if y == y_1:

        if x == x_1:
          empty += 1
        else:
           origin = np.array([[x,x],[y,y]])  # orgin with respect to target point
           vector_array = Electric_field2(x,y) + Electric_field1(x,y)   # show electric field due to charges.
           vector_list = vector_array.tolist()
           V = np.array([vector_list])
           plt.quiver(*origin, V[:,0], V[:,1])
      elif y == y_2:

        if x == x_2:
          empty += 1
        else:
           origin = np.array([[x,x],[y,y]])  # orgin with respect to target point
           vector_array = Electric_field2(x,y) + Electric_field1(x,y)   # show electric field due to charges.
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
plt.xlim(-6,5) 
plt.ylim(-6,5)
plt.show()
