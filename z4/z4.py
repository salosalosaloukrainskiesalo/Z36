import numpy as np
import matplotlib.pyplot as plt

h = [1, 2, 2, 3, 2, 4, 3, 4, 4, 5, 4, 5, 6, 6, 5, 6, 4]
k = [1, 0, 2, 1, 2, 0, 3, 2, 2, 1, 4, 3, 0, 2, 3, 2, 4]
l = [1, 0, 0, 1, 2, 0, 1, 0, 2, 1, 0, 1, 0, 0, 3, 2, 4]

#1.997336, 0.940389099

d = [
    3.263461615,
    2.825628567,
    1.997336,
    1.702419687,
    1.629779083,
    1.411640559,
    1.294946464,
    1.261728807,
    1.151709961,
    1.086055665,
    0.997516006,
    0.953697745,
    0.940389099,
    0.892019557,
    0.860403589,
    0.850427893,
    0.814172095
    ]

dd = [
    0.002457084,
    0.001764884,
    0.004187029,
    0.003999371,
    0.000381528,
    0.001150987,
    0.006745059,
    0.000157822,
    3.62746e-05,
    -5.23961e-05,
    -0.000870961,
    -0.001043536,
    -0.000659915,
    -0.010374003,
    -0.001624615,
    -0.00380832
    ]


def f(x, h, k, l):
    return x/np.sqrt(h**2 + k**2 + l**2)

x = np.linspace(0, 10, 1000)

a_true = 5.644536209999153
da = []
plt.figure(figsize=(10, 6))
a = []
for hi, ki, li, di in zip(h, k, l, d):
    y = f(x, hi, ki, li)
    
    line, = plt.plot(x, y)
    color = line.get_color()
    plt.axhline(di, color=color)
    t = di * np.sqrt(hi**2 + ki**2 + li**2)
    a.append(t)

for ddi in dd:    
    t = ddi * np.sqrt(hi**2 + ki**2 + li**2)
    da.append(t)

plt.axvline(a_true, color='black', linestyle='--')
plt.axhline(2.029479395)  
plt.scatter(x, y)
plt.xlabel('a (Å)')
plt.ylabel('d (Å)')
plt.xlim(0, 6)
plt.ylim(0, 4)
plt.show()


print(a)
print(da)
print(np.mean(a))
print(np.std(a))