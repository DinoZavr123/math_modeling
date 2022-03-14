import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

x=np.arange(0, 3, 0.01)




def diff_func(v, x):
  y, dy = v
  dydt = x
  dxdt = ((1-(x**2)**0.5))
  return dydt, dxdt



dy0 = 0
y0 = 1


v0 = y0, dy0


sol = odeint (diff_func, v0, x)

plt.plot(x, sol[:, 0], 'g')

plt.legend()
plt.show()