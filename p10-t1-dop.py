import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t=np.arange(-1, 1, 0.01)




def diff_func(v, x):
  x,y, z = v
  dxdt= 3*x-y+z
  dydt = x+y+z
  dzdt=4*x-y+4*z
  return dydt, dzdt,dxdt


x0=-71
y0 = 1
z0 = -3


v0 = x0, y0, z0


sol = odeint (diff_func, v0, t)

plt.plot(t, sol[:, 0], 'g')
plt.legend()
plt.show()