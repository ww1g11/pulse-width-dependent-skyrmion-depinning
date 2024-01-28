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

    data3 = np.loadtxt("fem/time_T300.txt")
    data = np.loadtxt('current_density_pw.txt')
    b = 1.18

    fig = plt.figure(figsize=(4,3))
    plt.plot(data[:,0], data[:, 1]*b, 's', label='Experiments', markersize=5.6)
    plt.plot(data3[:,1], data3[:, 0], 'o--', label=r'$u$ vs. $\left< \tau(0) \right >$', markersize=5, fillstyle='none')
    plt.xlim([0, 300])
    plt.ylabel('$u_c$ (m/s)')
    plt.xlabel('Pulse width (ns)')
    plt.legend()
    plt.tight_layout()
    plt.savefig('fig7.pdf')


plot_all()
