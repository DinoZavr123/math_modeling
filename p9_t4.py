import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


t = np.arange(1, 200, 1)
 

def radio_function(v, t):
    dmdt =  (b-k*v)/m
    return dmdt
v_0=0
v=4
b=8000
m=15000
k=100
 

solve_Bi = odeint(radio_function, v_0, t)

# Построение решения в виде графика функции
plt.plot(t, solve_Bi[:,0],color='r', label='Скорость')
plt.xlabel('Время тяги')
plt.ylabel('Скорость')
plt.legend()

plt.show()