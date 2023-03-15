# I have 2 charges, 1 charge with 1 Columb, 1 charge with -1 Columb. They are 10 cm apart.
#   I need to create a matrix (a 2D plane) first then place these 2 charges at the center:
import numpy as np

import sys  # in order to get epsilon zero

plate = []

for i in range(10):
    for j in range(10):
        plate.append(0)

plate = np.array(plate)  #convert list into array

plate[54] = 1
plate[55] = -1

distance_plate1 = plate   # get copies of plate
distance_plate2 = plate

#---------------------------------------------------------------------------------------------------

### Some parts are just for me to self-check, you can play them just simply delete the comment mark "#" that
###     have "$$$"

# I did an experiment on investigating the formula of distance on a 4 by 4 matrix, conclusions:
#  First of all, every point has an arranged index order starting from 1 to 16; Let
#
#  T: index of target point (it's correspond number)
#  C: index of point of charge
#  n: dimension of the matrix (square matrix, such as n = 10 in 10 by 10 matrix)
#  D: divisor
#  R: reminder
#
#  The formula we gonna use are:  |T - C| / n = D ... R      in particular:
#                                  D = [ |T - C| - (|T - C| % n) ] / n      just to avoid fration.
#                                  R = |T - C| % n  (modulus = % in python, returns "reminder")
#  
#  Step 1: we need to know if the target point locates at the "LEFT" side or "RIGHT" side of the point 
#      of charge, to that, we need to imagine there is a vertical line cross throught a point of charge 
#      (it's y-value, assuming the matrix is a x-y plane), we calculate the modulus of T and C: 
#              they are at the same y-axis if T%n = C%n 
#              T on the "LEFT" if T % n < C % n
#              T on the "RIGHT" if T % n > C % n
#  Step 2: we need to know if T > C or T < C: 
#       if T on the "LEFT" and T < C:
#             D = vertical distance between charge and target point(in absolute value)
#             R = horizontal distance between charge and target point(in absolute value)
#
#       if T on the "LEFT" and T > C:
#             D + 1 = vertical distance between charge and target point(in absolute value)
#             n - R = horizontal distance between charge and target point(in absolute value)
#
#       if T on the "RIGHT" and T > C:
#             D = vertical distance between charge and target point(in absolute value)
#             R = horizontal distance between charge and target point(in absolute value)
#
#       if T on the "RIGHT" and T < C:
#             D + 1 = vertical distance between charge and target point(in absolute value)
#             n - R = horizontal distance between charge and target point(in absolute value)
#
#       if T at the same vertical line as C:
#             D   =   vertical distance between charge and target point(in absolute value)
#             R = 0 = horizontal distance between charge and target point(in absolute value)
#
#  Finally, the distance between charge and target point will be sqrt(D^2 + R^2)

#-----------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------------

# Define a function to calculate the distances between target point and charge:

def distance(n,C,T):
    side = 0
    D = 0
    R = 0
    distance = 0
    a = T % n
    b = C % n
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

#-----------------------------------------------------------------

#$$$ Test it with a 5 by 5 matrix, C = 16, T = 2, we are looking forward to see output = sqrt(10) = 3.162277
#$$$print(distance(5,16,2))

#---------------------------------------------------------------------------------------

# Now get into our problem:

#-----------------------------------------------------------------------------------------

# This region calculates the distance of all points with charge 1 (with +1 Columb) and distance of all points
#     with charge 2 (with -1 Column):
#     Charge 1 has index C = 54; Charge 2 has index C = 55.


# For charge 1:

#$$$for i in range(100):
#$$$    i = i + 1         # We want the index starts from 1 to 100 not 0 to 99 as default.
                      # Since "plate" matrix defined its elements with indexes from 0 to 99, this is 
                      #     inconsistent with "imaginary" matrix defined in the function, it has elements 
                      #     from 1 to 100.
                      #     Thus "C" is 55 in distance() not 54
#$$$    distance_plate1[i-1] = distance(10,55,i)  # the computer like to read the first index as 0, so we need to
#                                                    minus 1 to get back to (0 to 99)

#$$$distance_plate1 = np.reshape(distance_plate1,(10,10))  # reshape it into a 10 by 10 matrix

#$$$print(distance_plate1)       # it might looks weird because all integers in the matrix but it is reasonable.
#                                    Since a lot of decimal numbers will be generated, the matrix cannot
#                                    perfectly fit them all ! Thus the computer round them into integers.
#$$$print(distance(10,55,46))   # it equals to sqrt(2) the code is correct.


# For charge 2:

#$$$for i in range(100):
#$$$    i = i + 1         # We want the index starts from 1 to 100 not 0 to 99 as default.
                          # Since "plate" matrix defined its elements with indexes from 0 to 99, this is 
                          #     inconsistent with "imaginary" matrix defined in the function, it has elements 
                          #     from 1 to 100.
                          #     Thus "C" is 56 in distance() not 55
#$$$    distance_plate2[i-1] = distance(10,56,i)  

#$$$distance_plate2 = np.reshape(distance_plate2,(10,10)) 

#$$$print(distance_plate2)      
#$$$print(distance(10,56,47))   # it equals to sqrt(2) the code is correct.

#-------------------------------------------------------------------------------------------------------



# We solved distances between all points and charge now, the next step is to get the potentials
#    when only one charge is placed and also its electric field. Then we can sum 2 electric fields
#    due to different charges to get the actual electric field.

# This should be good because of superposition theorem.


# Define 2 functions that take distance as argument and return the potential:

def Potential1(r):  # for charge 1 with +1 Columb
    return(1/(4*np.pi*sys.float_info.epsilon*r))

def Potential2(r):  # for charge 2 with -1 Columb
    return(-1/(4*np.pi*sys.float_info.epsilon*r))

# Define functions that take distance as argument and return negative of derivative of potential
#     using central difference theorem:

def Electric_field1(r): # for charge 1
    k = -(Potential1(r+0.5)-Potential1(r-0.5))
    return(k)

def Electric_field2(r):   # for charge 2
    k = -(Potential2(r+0.5)-Potential2(r-0.5))
    return(k)

# Do for charge 1, remove charge 2: 
potential1 = plate
electric_field1 = plate

# copy code for distance corresponds to charge 1:

for i in range(100):
    i = i + 1 
    r = distance(10,55,i)  # I explained why it is 55 not 54 in the past
    r = r * 0.1   # because in our "imaginary" matrix, each element is 10 cm far away to each other
                  #      ,so r is the multiple of 10cm, we need meter: 10cm = 0.1m 
    electric_field1[i-1] = Electric_field1(r)

# Do for charge 2, remove charge 1:
potential2 = plate
electric_field2 = plate

# copy code for distance corresponds to charge 2:

for i in range(100):
    i = i + 1        
    r = distance(10,56,i)  # I explained why it is 56 not 55 in the past
    electric_field2[i-1] = Electric_field2(r)

electric_field = electric_field1 + electric_field2   # Add them up:

electric_field[54] = 0  # the potential of the charge itself is not defined so zero here I think, thus
                         #   its electric field is also zero.
electric_field[55] = 0

electric_field = np.reshape(electric_field,(10,10)) # reshape it into a 10 by 10 matrix

print(electric_field)