import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
fig, ax = plt.subplots()
dots, = plt.plot([], [], '--', color='red', label='line')
dots2, = plt.plot([], [], 'o', color='blue', label='line')
edge=1
x0=0.1
y0=0.1 
c=0.3
d=0.33

plt.axis('equal')
 
ax.set_xlim(0, 0.5)
ax.set_ylim(0.2, 0.7)

def fractal(xi,yi,c,d,n):
  x, y = [], []
  x0,y0 = xi,yi
  for k in range(int (n)):
    xt = (x0)**2 - (y0)**2 + c
    yt = 2*x0*y0+d
    #xt,yt = 0,0
    x.append(xt)
    y.append(yt)
    x0,y0=xt,yt
  return x,y
def animate(i):
    dots.set_data(fractal(x0,y0,d,c,i))
    dots2.set_data(fractal(x0,y0,d,c,i))
ani = animation.FuncAnimation(fig,
                        animate,
                        frames=100,
                        interval=30)

 
ani.save('my_anim.gif')