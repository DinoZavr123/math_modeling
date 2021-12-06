import matplotlib.pyplot as plt
n=11213
x=[6]
y=[3]
l=3
h=1
n=10
lastx=x[0]
lasty=y[0]
for i in range (n):
  x.append(lastx+l)
  y.append(lasty)
  lastx+=l
  x.append(lastx)
  y.append(lasty+h)
  lasty+=h
plt.plot(x,y)
plt.show()