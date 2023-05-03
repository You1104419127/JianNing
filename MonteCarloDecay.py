import numpy as np
import matplotlib.pyplot as plt

t = 1   # time on each step (1 second)

num_Bi_213 = 10**4  # initial number of atoms of Bi-213

num_Ti_209 = 0  # intitial number of atoms of Ti-209

num_Pb_209 = 0  # initial number of atoms of Pb-209

num_Bi_209 = 0  # initial number of atoms of Bi-209

N = 2*10**4  # total time

time = np.linspace(0,N,N+1) # generate an array of time with size of N+1 (include initial)

decision = [0,1]  # for decay of Bi-213 atom

k = 0   # useless variable

Bi_213 = [num_Bi_213]  # list to hold all number of atoms of Bi-213 in all times

Bi_209 = [num_Bi_209]  # list to hold all number of atoms of Bi-209 in all times

Ti_209 = [num_Ti_209]  # list to hold all number of atoms of Ti-209 in all times

Pb_209 = [num_Pb_209]  # list to hold all number of atoms of Pb-209 in all times

# probability formula: p(t) = 1 - 2^(-t/tau)

# since the time I am taking on each step is 1 second, the half-life of these isotopes
#   are in unit of minutes; 1 min = 60 s :

# The function of probability for an atom decays:
def probability(tau):   # input tau has unit of minute
    p = 1 - 2**(-t/(tau*60))
    return p
 

for i in range(N):
    if num_Pb_209 > 0:  # to avoid calculation with negative number of atoms
        d_Pb_209 = probability(3.3) * num_Pb_209  # number of atoms which decays from Pb-209
        num_Pb_209 -= d_Pb_209  # remaining number of Pb-209
        num_Bi_209 += d_Pb_209  # Pb-209 decays and becomes Bi-209
    else:
        k = k + 1

    if num_Ti_209 > 0:
        d_Ti_209 = probability(2.2) * num_Ti_209 # number of atoms which decays from Ti-209
        num_Ti_209 -= d_Ti_209  # remaining number of Ti-209
        num_Pb_209 += d_Ti_209  # Ti-209 decays and becomes Pb-209
    else:
        k = k - 1
    
    addto = np.random.choice(decision, p = [0.9791, 0.0209])
    if addto == 0:
        if num_Bi_213 > 0:
            d_Bi_213 = probability(46) * num_Bi_213   # number of atoms which decays 
                              # from Bi-213 to Pb-209
            num_Bi_213 -= d_Bi_213  # remaining number of Bi-213
            num_Pb_209 += d_Bi_213  # Bi-213 decays and becomes Pb-209
        else:
            k = k + 1
    
    else:
        if num_Bi_213 > 0:
            d_Bi_213 = probability(46) * num_Bi_213   # number of atoms which decays 
                              # from Bi-213 to Ti-209
            num_Bi_213 -= d_Bi_213  # remaining number of Bi-213
            num_Ti_209 += d_Bi_213  # Bi-213 decays and becomes Ti-209
        else:
            k = k - 1
    
    Bi_213.append(num_Bi_213)
    Bi_209.append(num_Bi_209)
    Ti_209.append(num_Ti_209)
    Pb_209.append(num_Pb_209)

Bi_213 = np.array(Bi_213)
Bi_209 = np.array(Bi_209)
Ti_209 = np.array(Ti_209)
Pb_209 = np.array(Pb_209)

plt.plot(time,Bi_213,label='Bi-213')
plt.plot(time,Bi_209,label='Bi-209')
plt.plot(time,Ti_209,label='Ti-209')
plt.plot(time,Pb_209,label='Pb-209')
plt.xlabel('times (seconds)')
plt.ylabel('number of atoms')
plt.title('Decay of Bi-213 atoms model')
plt.legend()
plt.show()