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
    data1 = np.loadtxt('time_T100.txt')
    data2 = np.loadtxt('time_T200.txt')
    data3 = np.loadtxt('time_T300.txt')

    fig = plt.figure(figsize=(5,3))
    plt.plot(data1[:,0], data1[:, 1], 'o-', label='T=100K', markersize=5.6)
    plt.plot(data2[:,0], data2[:, 1], 's-', label='T=200K', markersize=5.6)
    plt.plot(data3[:,0], data3[:, 1], '^-', label='T=300K', markersize=5.6)
    plt.xlabel('u (m/s)')
    plt.ylabel('MFPT (ns)')
    plt.legend()
    plt.tight_layout()
    plt.savefig('fig6b.svg')

with plt.style.context('seaborn-deep'):
    plot_all()
