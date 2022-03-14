import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

x=np.arange(0, 5, 0.01)




def diff_func(v, x):
  y, dy = v
  dydt = x
  dxdt = ((x**2)-((3*(y**2))/(x**0.5)))/y
  return dydt , dxdt



dy0 = 1
y0 = 0


v0 = y0, dy0


sol = odeint (diff_func, v0, x)

plt.plot(x, sol[:, 0], 'g')

plt.legend()
plt.show()