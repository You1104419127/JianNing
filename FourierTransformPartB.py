# Fourier transform Part b

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

N = 1000

# plot of sawtooth wave y_n = n

x = np.linspace(0,20, N)
f = signal.sawtooth(x)

plt.plot(x,f)
plt.xlabel("x")
plt.ylabel("amplitude")
plt.title("sawtooth wave function")
plt.legend()
plt.show()


# plot of Fourier transform of sawtooth wave:

F = np.fft.fft(f, n = N)
frequencies = np.fft.fftfreq(len(x))

plt.plot(frequencies, F)  
plt.xlabel("frequencies")
plt.ylabel("Magnitude")
plt.title("Fourier transform of f(x)")
plt.legend()
plt.show()


# plot of figure of inverse Fourier transform of F(x)


iF = np.fft.ifft(F,n = N) 

plt.plot(x, iF) 
plt.xlabel("x")
plt.ylabel("amplitude")
plt.title("Inverse Fourier transform of F(x)")
plt.legend()
plt.show()