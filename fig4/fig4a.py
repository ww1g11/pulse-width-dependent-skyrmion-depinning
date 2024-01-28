import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve
import matplotlib.cm as cm

from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = 'Arial'
rcParams['savefig.dpi'] = 300
rcParams['font.size'] = 14

u = 0.06
beta = 0.08
eta = 1.2

xs = np.linspace(0, 3.0, 1001)
ys = 4*np.exp(-2*xs**2)*(1-xs**2)*(1-5*xs**2+2*xs**4)

fig = plt.figure(figsize=(4,3))

data = np.loadtxt('./u_c_R10_4e4/uc.txt')

plt.plot(data[:, 0]*1e9, data[:, 1], 's-', label='Simulation', color='C2')
plt.hlines(y=4.76, xmin=0, xmax=20, linestyles="--", color='C3', label='Analytical')

plt.legend()
plt.ylim([0,15])

plt.xlabel("Pulse width (ns)")
plt.ylabel("$u_c$ (m/s)")
plt.tight_layout()
fig.savefig("fig4a.svg")