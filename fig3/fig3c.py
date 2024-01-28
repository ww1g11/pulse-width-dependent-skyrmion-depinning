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

xs = np.linspace(0, 3.0, 1001)
ys = 4*np.exp(-2*xs**2)*(1-xs**2)*(1-5*xs**2+2*xs**4)

#fig, ax = plt.subplots()
fig = plt.figure(figsize=(4,3))

plt.hlines(y=0, xmin=0, xmax=3, linewidth=1, linestyles='--',color='k')

plt.plot(xs, ys)
plt.grid(alpha=0.7)
plt.xlim([0,3])
plt.ylim([-1,4])

plt.xlabel("$r$ (nm)")
plt.ylabel("$q_0$ (1/s)")
plt.tight_layout()
fig.savefig("fig3c.svg")