import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
fig, ax = plt.subplots()
line, = plt.plot([], [], '--', color='red', label='line')
edge = 40
plt.axis('equal')
 
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
 
x, y = [], []

def star():
    t=np.arange(-10,10,0.01)
    x = 12*np.cos(t)+ 8*np.cos(1.5*t)
    y = 12*np.sin(t)-8*np.sin(1.5*t)
    star, = plt.plot(x,y, '--', color='red', label='line')
    t = np.pi /3
    X = x*np.cos(t) - y*np.sin(t)
    Y = y*np.cos(t) + x*np.sin(t)
    star, = plt.plot(X,Y, '--', color='purple', label='line')

star()
plt.show()
