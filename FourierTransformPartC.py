# Fourier transform part C:

N = 1000

import numpy as np
import matplotlib.pyplot as plt


# plot of the modulated sine wave function:

n = np.linspace(0,10**3,N)

y = np.sin(np.pi * n/N) * np.sin(20*np.pi * n / N)

plt.plot(n,y)
plt.xlabel("n")
plt.ylabel("amplitude")
plt.title("The modulated sine wave fucntion")
plt.legend()
plt.show()


# plot of the Fourier transform of the modulated sine wave function y(n):

Y = np.fft.fft(y, n = N)

frequencies = np.fft.fftfreq(len(n))

plt.plot(frequencies,Y)
plt.xlabel("frequencies")
plt.ylabel("Magnitude")
plt.title("Fourier transform of y(n)")
plt.legend()
plt.show()


# plot of figure of inverse Fourier transform of Y(n)


iY = np.fft.ifft(Y, n = N) 

plt.plot(n, iY) 
plt.xlabel("n")
plt.ylabel("amplitude")
plt.title("Inverse Fourier transform of Y(n)")
plt.legend()
plt.show()
