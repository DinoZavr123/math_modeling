from math import sqrt
a=float(input("a"))
b=float(input("b"))
c=float(input("c"))
d=b**2-4*c*a
if d<0:
  print ("Нет кореней")
elif d>0:
  k1=(-b+sqrt(d))/2*a
  k2=(-b-sqrt(d))/2*a
  print (k1)
  print (k2)
else:
  x=(-b)/2*a
  print (x)
