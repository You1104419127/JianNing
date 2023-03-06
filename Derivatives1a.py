#Calculating derivatives---1.(a): derivative of the function f(x)=x(x-1)
def f(x):
    y = x*(x-1)
    return(y)

def deri(sigma,x):
    k = (f(x+sigma)-f(x))/sigma
    return(k)

sigma = 10**(-2)
x = 1
print(deri(sigma,x))

#The computational answer is roughtly 1.01
#By hand,the analytical answer is 1 when x=1
#of cause they are not "perfectly" equal to each other. Nothing is perfect and because of the sigma value
# that we chose---sigma = 10^-2, it should approch to zero (infinitely small), so the smaller sigma, the 
# better result. Try sigma = 10^-5 below:

sigma = 10**(-5)
print(deri(sigma,x))

#as we can see, it is closer to 1 now with smaller sigma.