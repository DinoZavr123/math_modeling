import numpy as np
from numpy import absolute as nabs
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def collision (x1, vx1 , x2 ,vx2, radius, mass1,mass2):
  r12 = np.sqrt ((x1-x2)**2)
  if r12 <= 2*radius:
    VX1 = vx1 * (mass1-mass2) / (mass1+ mass2)  + (2) * mass2 * vx2 / (mass1 + mass2)
    VX2 = vx2 * (mass2-mass1) / (mass1+mass2)  + (2) * mass1* vx1/ (mass1+mass2)
    px1, PX1 = mass1 * vx1, mass1 * VX1
    px2, PX2 = mass2 * vx2, mass2 * VX2
    print("До столкновения:")
    print(f"\tИмпульс: p1 = {px1}, p2 = {px2}, p_sum = {px1 + px2}")
    print(f"\tМасса: m1 = {mass1}, m2 = {mass2}")
    print(f"\tСкорость: vx1 = {vx1}, vx2 = {vx2}")
    print("После столкновения:")
    print(f"\tИмпульс: P1 = {PX1}, P2 = {PX2}, P_sum = {PX1 + PX2}")
    print(f"\tМасса: m1 = {mass1}, m2 = {mass2}")
    print(f"\tСкорость: VX1 = {VX1}, VX2 = {VX2}")
    print("Закон сохранения импульса:")
    print("\t", ("Выполняется" if (px1 + px2 == PX1 + PX2) else "Не выполняется"), sep=' ')
  else:
      VX1, VX2 = vx1, vx2
  return VX1, VX2

def move_func(s,t):
  x1,v_x1,x2,v_x2=s

  dx1dt =v_x1
  dv_x1dt = 0

  dx2dt = v_x2
  dv_x2dt = 0
  return dx1dt, dv_x1dt, dx2dt,dv_x2dt

T = 3
N = 300
mass1 = 1
mass2 = 1
radius = 0.5
  
x10=1
x20=5
v10=4
v20=-2

x1=[x10]
x2=[x20]
tau = np.linspace(0, T, N)
for k in range(N-1):

    t = [tau[k], tau[k+1]]
    s0 = x10, v10, x20, v20

    sol = odeint(move_func, s0, t)

    x10 = sol[1, 0]
    x20 = sol[1, 2]
    x1.append(x10)
    x2.append(x20)

    v10 = sol[1, 1]
    v20 = sol[1, 3]
    res = collision(x10, v10, x20, v20, radius, mass1, mass2)
    v10 = res[0]
    v20 = res[1]
fig, ax = plt.subplots()

ball_1, = plt.plot([], [], 'o', color='r', ms=25)
ball_2, = plt.plot([], [], 'o', color='b', ms=25)

def animate(i):
    ball_1.set_data((x1[i], 0))
    ball_2.set_data((x2[i], 0))

ani = FuncAnimation(fig,
                    animate,
                    frames=N,
                    interval=30)
ax.set_xlim(-5, 10)
ax.set_ylim(-1, 1)
ani.save("anim.gif")
plt.show()