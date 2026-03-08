import numpy as np
import matplotlib.pyplot as plt


x1_1 = 0.1158
y1_1 = 0.00688
x2_1 = -0.133
y2_1 = 0

x1_2 = 0.10018
y1_2 = -0.05847
x2_2 = -0.11518
y2_2 = 0.0665

x1_3 = 0.07919
y1_3 = 0.08477
x2_3 = -0.10188
y2_3 = -0.08549

dx1_1 = 0.000939724
dy1_1 = 0.015053466
dx2_1 = 0.000289017
dy2_1 = 0.005041747

dx1_2 = 0.005840376
dy1_2 = 0.010026642
dx2_2 = 0.000384914
dy2_2 = 0.000526701

dx1_3 = 0.022581568
dy1_3 = 0.005328821
dx2_3 = 0.000436281
dy2_3 = 0.000485006



plt.figure(figsize=(8, 6))
plt.plot(x1_1, y1_1, 'ro', label='Point 1')
plt.plot(x2_1, y2_1, 'bo', label='Point 2')
plt.plot(x1_2, y1_2, 'ro', label='Point 3')
plt.plot(x2_2, y2_2, 'bo', label='Point 4')
plt.plot(x1_3, y1_3, 'ro', label='Point 5')
plt.plot(x2_3, y2_3, 'bo', label='Point 6')
plt.plot([x1_1, x2_1], [y1_1, y2_1], 'k-')
plt.plot([x1_2, x2_2], [y1_2, y2_2], 'k-')
plt.plot([x1_3, x2_3], [y1_3, y2_3], 'k-')
plt.show()

def linear_coef(x1, y1, x2, y2):
    a = (y2 - y1) / (x2 - x1)
    b = y1 - a * x1
    return a, b

def dab(x1,x2,y1,y2, dx1, dy1, dx2, dy2, a):
    da = 1/(x2-x1)*np.sqrt(dy1**2 + dy2**2 + (dx2*(y2-y1)/(x2-x1))**2 + (dx1*(y2-y1)/(x2-x1))**2) 
    db = np.sqrt((dy1)**2 + (da*x1)**2 + (a*dx2)**2)
    return da, db

def same_point(a1, b1, a2, b2):
    x = (b2-b1) / (a1 - a2)
    y = a1 * x + b1
    return x, y

def point_error(x1,x2,y1,y2, dx1, dy1, dx2, dy2):
    a, b = linear_coef(x1, y1, x2, y2)
    dx, dy = dab(x1,x2,y1,y2, dx1, dy1, dx2, dy2, a)
    return dx, dy
 


a1, b1 = linear_coef(x1_1, y1_1, x2_1, y2_1)
da1, db1 = point_error(x1_1,x2_1,y1_1,y2_1, dx1_1, dy1_1, dx2_1, dy2_1)
a2, b2 = linear_coef(x1_2, y1_2, x2_2, y2_2)
da2, db2 = point_error(x1_2,x2_2,y1_2,y2_2, dx1_2, dy1_2, dx2_2, dy2_2)
a3, b3 = linear_coef(x1_3, y1_3, x2_3, y2_3)
da3, db3 = point_error(x1_3,x2_3,y1_3,y2_3, dx1_3, dy1_3, dx2_3, dy2_3)

x1, y1 = same_point(a1, b1, a2, b2)
dx11, dy11 = point_error(a1, a2, b2, b1, da1, db1, da2, db2)
x2, y2 = same_point(a1, b1, a3, b3)
dx22, dy22 = point_error(a1, a3, b3, b1, da1, db1, da3, db3)
x3, y3 = same_point(a2, b2, a3, b3)
dx33, dy33 = point_error(a2, a3, b3, b2, da2, db2, da3, db3)

avg_x = (x1 + x2 + x3) / 3
avg_y = (y1 + y2 + y3) / 3

dx_avg = np.sqrt(dx11**2 + dx22**2 + dx33**2) / 3
dy_avg = np.sqrt(dy11**2 + dy22**2 + dy33**2) / 3
dx_std = np.std([x1, x2, x3])
dy_std = np.std([y1, y2, y3])


print(f"Average Point: ({avg_x} $\\pm$ {dx_avg} $\\pm$ {dx_std}, {avg_y} $\\pm$ {dy_avg} $\\pm$ {dy_std})")




