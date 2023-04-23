import numpy as np
import matplotlib.pyplot as plt

N = 1000

#(a): A single cycle of a square-wave with amplitude 1

x = np.linspace(0,11,N)

f = np.sin(x) # a simple function

 
plt.plot(x,f)  # plot the figure of f(X)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("amplitude")
plt.legend()
plt.show()

## To plot the Fourier transfor, we need a vector of frequency and a vector of the absolute value of
##     Fourier transform of the function.

F = np.fft.fft(f, n = N) # the Fourier transform of f(x)

frequencies = np.fft.fftfreq(len(x))

plt.plot(frequencies, F)  # plot of figure of Fourier transform of f(x)
plt.xlabel("frequencies")
plt.ylabel("Magnitude")
plt.title("Fourier transform of f(x)")
plt.legend()
plt.show()

iF = np.fft.ifft(F,n = N) # the inverse Fourier transform of F(x), it should be converted back to f(x)

plt.plot(x, iF)  # plot of figure of inverse Fourier transform of F(x)
plt.xlabel("x")
plt.ylabel("amplitude")
plt.title("Inverse Fourier transform of F(x)")
plt.legend()
plt.show()