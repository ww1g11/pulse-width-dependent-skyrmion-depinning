import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve
import matplotlib.cm as cm

from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = 'Arial'
rcParams['savefig.dpi'] = 300
rcParams['font.size'] = 18

u = 0.06
beta = 0.08
eta = 1.2

xs = np.linspace(-3.0, 3.0, 1001)
ys = np.linspace(-3.0, 3.0, 1001)
X, Y = np.meshgrid(xs, ys)
Z = (X**2 + Y**2)*np.exp(-X**2 - Y**2) + u*Y - beta*eta*u*X

def func(z):
    X = z[0]
    Y = z[1]
    dx = u-2*np.exp((-X**2-Y**2))*Y*(-1+X**2+Y**2)
    dy = 2*np.exp(-X**2 - Y**2)*X*(-1+X**2+Y**2) + u*beta*eta
    return [dx, dy]

def compute_dx_dy(X, Y):
    dx = u-2*np.exp((-X**2-Y**2))*Y*(-1+X**2+Y**2)
    dy = 2*np.exp(-X**2 - Y**2)*X*(-1+X**2+Y**2) + u*beta*eta
    return dx, dy


#fig, ax = plt.subplots()
fig = plt.figure(figsize=(4,4))
cs = plt.contour(X, Y, Z, levels =[-0.15, -0.08, -0.005, 0.1, 0.20, 0.32, 0.4], linewidths=1.4, linestyles='solid')

specific_points = [(0, 0), (0, 0), (0, 0), (0, 0),(0.5, -0.2),(0, 1),(0, 2),(1, 1),(0, 1)] 
arrow_size = 1e-3
point_index = 0
for i in range(len(cs.collections)):
    #p = cs.collections[i].get_paths()[0]
    for p in cs.collections[i].get_paths():
        color = cs.collections[i].get_edgecolor()
        v = p.vertices
        x = v[:,0]
        y = v[:,1]

        xp, yp = specific_points[point_index]
        id = np.argmin((x - xp)**2+(y-yp)**2)
        x0 = x[id]
        y0 = y[id]
        dx, dy = compute_dx_dy(x0, y0)

        print(i, point_index, specific_points[point_index], (x0, y0), (dx, dy))
        plt.annotate('', xy=(x0, y0), xytext=(x0+dx*arrow_size, y0+dy*arrow_size), arrowprops=dict(arrowstyle='<-', color=color))
        point_index += 1

print(cs.levels)
plt.clabel(cs, inline=True, fontsize=10, levels=cs.levels[1:3])
plt.clabel(cs, inline=True, fontsize=10, levels=cs.levels[0:1], manual=[(-1.5, -3)])

root = fsolve(func, [1, 1])
print(root)
plt.scatter(root[0], root[1], color='k', s=12, marker='o')

root = fsolve(func, [0, 0])
print(root)
plt.scatter(root[0], root[1], color='k', s=12, marker='o')

ax = plt.gca()
ratio = 1.0
x_left, x_right = ax.get_xlim()
y_low, y_high = ax.get_ylim()
ax.set_aspect(abs((x_right-x_left)/(y_low-y_high))*ratio)

plt.xlabel("$x$ (nm)")
plt.ylabel("$y$ (nm)")
plt.tight_layout()
fig.savefig("fig3a.svg")