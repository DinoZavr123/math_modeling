import matplotlib.pyplot as plt
import numpy as np
import math 
b=0.02
N=1000
phi0=0.01
phi1=8*math.pi
phi= np.linspace(phi0,phi1,N)
r=np.exp(b*phi)
x=[]
y=[]
for i in range (N):
  x.append(r[i]*np.cos(phi[i]))
  y.append(r[i]*np.sin(phi[i]))
plt.plot(x,y)
plt.axis('equal')
plt.show()