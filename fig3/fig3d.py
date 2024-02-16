from cProfile import label
from tkinter import font
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve
import matplotlib.cm as cm

from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = 'Arial'
rcParams['savefig.dpi'] = 300
rcParams['font.size'] = 18

def compute_ys(xs, u=0.06):
    
    ys = xs**2*np.exp(-xs**2)+u*xs

    return ys

xs = np.linspace(-3.0, 3.0, 1001)

#fig, ax = plt.subplots()
fig = plt.figure(figsize=(4,3))

plt.plot(xs, compute_ys(xs, u=0), label="$u=0$ m/s")
plt.plot(xs, compute_ys(xs, u=0.2), label="$u=0.2$ m/s")
plt.plot(xs, compute_ys(xs, u=0.5), label="$u=0.5$ m/s")

plt.grid(alpha=0.7)
plt.xlim([-3,3])
#plt.ylim([-1,4])
plt.legend(fontsize=12, handletextpad=0.4, frameon=True)

plt.xlabel(r"$y'$ (nm)")
plt.ylabel("$H$ (nm$^2$/ns)")
plt.tight_layout()
fig.savefig("fig3d.svg")