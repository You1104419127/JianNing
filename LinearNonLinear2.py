import numpy as np
import matplotlib.pyplot as plt

def Bisectiony1y2(a,b,y1,y2,acc):
    # a: left-end-point of chosen interval
    # b: right-end-point of chosen interval
    # y1: function of y1
    # y2: function for even numbered states
    # acc: accuracy
    c = (a+b)/2   # find the mid-point of the interval
    abdp = np.sqrt( (y1(c) - y2(c))**2 ) # previous absolute value of the difference between 2 functions.
    abd = abdp  # absolute value of the difference between 2 functions; get into a WHILE loop
    while abd > acc :  # a loop to keep processing until the difference between
                                             #  2 functions is less than required accuracy

        # now we should reduce the range of interval to make this loop converge:
        # instead of [a,b], we can try [a,c] or [c,b] instead of [a,b]. One of them must work.

        # try [a,c] first:
        
        A = a  # store the initial value of a
        B = b  # store the initial value of b
        C = c  # store the initial value of c


        a = c  # always try interval [c,b] first; update a

        c = (a+b)/2   # update c
        abd = np.sqrt( (y1(c) - y2(c))**2 ) # update abd

        if abd < abdp:   # if we got smaller difference, then [c,b] can be a new interval
            A = a   # update A
            C = c   # update C
            abdp = abd  # update abdp
            # end and get back to the condition of WHILE loop, check if the WHILE still need to run.

        else: # if we got bigger difference, then interval [c,b] cannot be a new interval

            b = c   # we then use interval [a,c]; update b
            a = A   # reset a

            c = (a+b)/2   # update c
            B = b   # update B
            C = c   # update C
            abd = np.sqrt( (y1(c) - y2(c))**2 ) # update abd
            abdp = abd  # update abdp
    
    # this WHILE loop run and run again until abd <= acc
    return(c)  # return the value of E where y1 = y3

def Bisectiony1y3(a,b,y1,y3,acc):
    # a: left-end-point of chosen interval
    # b: right-end-point of chosen interval
    # y1: function of y1
    # y3: function for odd numbered states
    # acc: accuracy
    c = (a+b)/2   # find the mid-point of the interval
    abdp = np.sqrt( (y1(c) - y3(c))**2 ) # previous absolute value of the difference between 2 functions.
    abd = abdp  # get into a WHILE loop
    while abd > acc :  # a loop to keep processing until the difference between
                                             #  2 functions is less than required accuracy

        # now we should reduce the range of interval to make this loop converge:
        # instead of [a,b], we can try [a,c] or [c,b] instead of [a,b]. One of them must work.

        # try [a,c] first:
        
        A = a  # store the initial value of a
        B = b  # store the initial value of b
        C = c  # store the initial value of c


        a = c  # always try interval [c,b] first; update a

        c = (a+b)/2   # update c
        abd = np.sqrt( (y1(c) - y3(c))**2 ) # update abd

        if abd < abdp:   # if we got smaller difference, then [c,b] can be a new interval
            A = a   # update A
            C = c   # update C
            abdp = abd  # update abdp
            # end and get back to the condition of WHILE loop, check if the WHILE still need to run.

        else: # if we got bigger difference, then interval [c,b] cannot be a new interval

            b = c   # we then use interval [a,c]; update b
            a = A   # reset a; because I updated a to be c before

            c = (a+b)/2   # update c
            B = b   # update B
            C = c   # update C
            abd = np.sqrt( (y1(c) - y3(c))**2 ) # update abd
            abdp = abd  # update abdp
    
    # this WHILE loop run and run again until abd <= acc
    return(c)  # return the value of E where y1 = y3

m = 9.1094*10**(-31)

w = 1 * 10**(-9)

hbar = 1.054571817*10**(-34) 

acc = 10**(-3)

V = 20

def y1(E):
    return( np.tan( np.sqrt(w**2 * m * E / (2*hbar**2)) ) )

def y2(E):
    return( np.sqrt( (V - E) / E ) )

def y3(E):
    return( -np.sqrt(E / (V - E)) )

print("first 6 energy level for even numbered states are")
print(" ")
# Bisectiony1y2(a,b,y1,y2,acc)
print(Bisectiony1y2(2.75,2.80,y1=y1,y2=y2,acc=acc))
print(Bisectiony1y2(2.85,2.90,y1=y1,y2=y2,acc=acc))
print(Bisectiony1y2(5.4,5.6,y1=y1,y2=y2,acc=acc))
print(Bisectiony1y2(5.6,5.8,y1=y1,y2=y2,acc=acc))
print(Bisectiony1y2(6.4,6.5,y1=y1,y2=y2,acc=acc))
print(Bisectiony1y2(6.8,7.0,y1=y1,y2=y2,acc=acc))
print(" ")
print(" ")
print("first 6 energy level for odd numbered states are")
# Bisectiony1y3(a,b,y1,y3,acc)
print(" ")
print(0,"we know 0 must be an answer")
print(Bisectiony1y3(0.2,0.4,y1=y1,y3=y3,acc=acc))
print(Bisectiony1y3(0.6,0.8,y1=y1,y3=y3,acc=acc))
print(Bisectiony1y3(0.8,1.0,y1=y1,y3=y3,acc=acc))
print(Bisectiony1y3(1.6,1.8,y1=y1,y3=y3,acc=acc))
print(Bisectiony1y3(1.8,2.0,y1=y1,y3=y3,acc=acc))
