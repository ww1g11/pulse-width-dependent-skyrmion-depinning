import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
#plt.style.use('seaborn')
import matplotlib.cm as cm
mpl.rcParams['font.size'] = 14
import numpy as np
import os
from scipy.integrate import dblquad
from scipy.integrate import quad

from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = 'Arial'
rcParams['savefig.dpi'] = 300
rcParams['font.size'] = 14



def plot_all():
    data = np.loadtxt('../fig5a/100K/all_p.txt')
    print(data.shape)

    u0 = data[0]
    u2 = data[10]
    u4 = data[20]
    u6 = data[30]
    ts = np.linspace(0, 20e-9, 101)*1e9

    fig = plt.figure(figsize=(4,3))
    plt.plot(ts, u0,'-', label='u=0 m/s', markersize=5.6)
    plt.plot(ts, u2,'-', label='u=2 m/s', markersize=5.6)
    plt.plot(ts, u4,'-', label='u=4 m/s', markersize=5.6)
    plt.plot(ts, u6,'-', label='u=6 m/s', markersize=5.6)
    plt.legend()
    plt.xlabel('Pulse duration (ns)')
    plt.ylabel('Probability')
    plt.tight_layout()
    plt.savefig('fig5b.svg')


with plt.style.context('seaborn-deep'):
    plot_all()

