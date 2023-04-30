import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

L = 101  # width of the square

N = 10**6  # million steps

i = 50
j = 50  # mid point

i_list = [i]
j_list = [j]

possible_direction = [-1,1]

i_or_j = [0,1]  # go left-right or up-down

a = 0  # next change on i
b = 0  # next change on j

for n in range (N):
    I = i   # store original position
    J = j
    if np.random.choice(i_or_j) == 0:   
        a = np.random.choice(possible_direction) # uniformly distribution on chosing -1 or 1
        i += a   # update new position of i
        if i < 0 or i > 100:  # get out of the square
            i = I  # fail to have a new position and get back to its original position
        else:
            i = i
        i_list.append(i)  # collect positions into i_list
        j_list.append(j)  # same for j although j did not change
    else:   
        b = np.random.choice(possible_direction)
        j += b   # update new position of j
        if j < 0 or j > 100:  # same for j
            j = J
        else:
            j = j
        j_list.append(j)
        i_list.append(i)

i_array = np.array(i_list)
j_array = np.array(j_list)

fig,ax = plt.subplots()

plt.xlim(0,100)
plt.ylim(0,100)

scat = ax.scatter(1,0)  # define scatter's position

def animate(k):   # k should be a time variable and we don't need to define
    scat.set_offsets((i_array[k],j_array[k]))
    return scat,

ani = animation.FuncAnimation(fig, animate, frames=N)

plt.show()


## it need a long time to reach to one of sides of the square.