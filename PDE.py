import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# necessary packages to use discrete sin transform:
from numpy import empty,arange,exp,real,imag,pi
from numpy.fft import rfft,irfft



# Question 1:

M = 9.109*10**(-31)
L = 10**(-8)
x0 = L/2
sigma = 1*10**(-10)
kappa = 5*10**(10)
N = 1000

real_coe = []
imaginary_coe = []

# define the wave function (time-independent) where time = 0 :

def rPsi(x):  # real part of psi(x,0)
    if x == 0 or x == L:
        return(0)
    else:
        return np.exp(-(x-x0)**2 / (2*sigma**2))
    
def iPsi(x):  # imaginary part of psi(x,0)
    if x == 0 or x == L:
        return(0)
    else:
        return np.exp(kappa*x*1j) # 1j  is imaginary number i in python


X = np.linspace(0,L,N)  # divided into N pieces
rpsi = []   # list of real part of psi(x_n, 0)
ipsi = []   # list of imaginary part of psi(x_n, 0)


for i in range(N):
    x = X[i]
    rpsi.append(rPsi(x))
    ipsi.append(iPsi(x))

rpsi = np.array(rpsi)  # convert a list into an array
ipsi = np.array(ipsi) 

# define a function of discrete sin transform:
def dst(psi):
    N1 = len(psi)
    psi2 = empty(2*N1,float)
    psi2[0] = psi2[N1] = 0.0
    psi2[1:N1] = psi[1:]
    psi2[:N1:-1] = -psi[1:]
    a = -imag(rfft(psi2))[:N1]
    a[0] = 0.0

    return a

a_k = dst(rpsi)   # real parts of coefficients b_k (s)
n_k = dst(ipsi)  # imaginary parts of coefficients b_k (s)

print(a_k)
print( )
print( )
print( )
print(n_k)


# Question 2:

t = 10**(-16)
hbar = 1.0546 * 10**(-34)

def sin(x):
    return np.sin(x)

def cos(x):
    return np.cos(x)

pi = np.pi

# define a function of real part of the wavefunction psi(x,t) at a single piece
#                                                              (we have N piece):

def Real_wavefunction(n):
    sum = 0
    for k in range(1,N):
        sum += (a_k[k] * cos(t*(pi**2*hbar*k**2)/(2*M*L**2)) - n_k[k] * 
                sin(t*(pi**2*hbar*k**2)/(2*M*L**2))) * sin((pi*k*n)/N)
    
    return (1/N)*sum

RWF = []   # list for real wave fucntion

for n in range(N): # find all N pieces of wave function (real part)
    RWF.append(Real_wavefunction(n))

RWF = np.array(RWF)

# define a function of inverse sin transform:

def idst(RWF):
    N2 = len(RWF)
    c = empty(N2+1,complex)
    c[0] = c[N2] = 0.0
    c[1:N2] = -1j*RWF[1:]
    y = irfft(c)[:N2]
    y[0] = 0.0

    return y

RealPartWaveFunction = idst(RWF)


plt.plot(X,RealPartWaveFunction,label='real part of wave function')
plt.xlabel('x')
plt.ylabel(r'$\Psi(x_n,10^{-16})$')
plt.ylim(-0.1,0.1)
plt.legend()
plt.show()





# Question 3: 

fig,ax = plt.subplots()

scat = ax.scatter(0,0)  # define scatter's position

def animate(k):   # kk should be a time variable and we don't need to define
    scat.set_offsets((X[k],RealPartWaveFunction[k]))  
    return scat,

ani = animation.FuncAnimation(fig, animate, frames = N-1, interval = 10**(-16))

plt.show()





## Question 4:

## If I did everything correctly previously at (a), (b), (c), although the figure of wave function
##    looks weird. I can see that the oscillation runs obviously at the beginning and suddenly
##    jump to a high place (Amplitude has a big change). Then the oscillation becoms stable
##    later until the particle stops moving. The conclusion will be the particle is most likely
##    to be found out at the beginning since high amplitude tells us that the proability 
##    is significant.
