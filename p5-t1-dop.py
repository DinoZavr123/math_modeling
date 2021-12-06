import matplotlib.pyplot as plt
import numpy as np
import math
from math  import sqrt
N=100
a=1
A=0.5
B=1
t0=0
t1=25 
b=0.25
t=np.linspace(t0,t1,N)
o=math.pi/8
x=[]
y=[]
for i in range (N):
  x.append(A*np.sin(a*t[i]+o))
  y.append(B*np.sin(b*t[i]))
plt.plot(x,y)
plt.axis('equal')
plt.show()