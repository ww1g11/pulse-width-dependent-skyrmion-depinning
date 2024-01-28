import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
#plt.style.use('seaborn')
import matplotlib.gridspec as gridspec
import matplotlib.cm as cm
mpl.rcParams['font.size'] = 14
import numpy as np
import os

from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = 'Arial'
rcParams['savefig.dpi'] = 300
rcParams['font.size'] = 13

def plot_P():
    data = np.loadtxt('100K/all_p.txt')

    fig = plt.figure(figsize=(4,3))
    ax = fig.add_subplot(1, 1, 1)

    plt.xlabel('Pulse duration (ns)')
    plt.ylabel(r'u (m/s)')
    im = ax.imshow(data, interpolation='bilinear', origin='lower',aspect='auto',
                cmap='tab20c', extent=[0, 20, 0, 6], vmax=1, vmin=0) #viridis
    plt.contour(data, [0.5], cmap='Pastel1',  origin='lower', extent=[0, 20, 0, 6], linestyles='dashed')
    fig.colorbar(im, ax=ax)

    plt.tight_layout()
    plt.tight_layout()
    fig.savefig("fig5a.svg")


plot_P()