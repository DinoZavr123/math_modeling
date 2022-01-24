import numpy as np	
from scipy.integrate import odeint	
import matplotlib.pyplot as plt	
t = np.arange(0, 10, 1)	
def radio_function(m, t):
	
    dmdt =  k * m
	
    return dmdt

m_0 = 1
	
k = 1.07 # Постоянная распада для Висмута 210
solve_Bi = odeint(radio_function, m_0, t)

# Построение решения в виде графика функции
plt.plot(t, solve_Bi[:,0], label='Деление')
plt.legend()
plt.show()
