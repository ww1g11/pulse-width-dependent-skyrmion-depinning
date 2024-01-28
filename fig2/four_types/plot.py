# -*- coding: utf-8 -*-
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
defaut_font = mpl.rcParams['font.sans-serif']
plt.style.use('seaborn')
mpl.rcParams['font.sans-serif'] = defaut_font
import matplotlib.cm as cm

import os
import numpy as np

from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
#rcParams['font.sans-serif'] = 'Arial'
rcParams['savefig.dpi'] = 300
rcParams['font.size'] = 14

def plot():

    fig, axes = plt.subplots(2, 2, sharey=True, sharex=True, figsize=(5,2.7))

    data1 = np.loadtxt('ux_3_bias_6.txt')
    data2 = np.loadtxt('ux_3.5_bias_6.txt')
    data3 = np.loadtxt('ux_7_bias_6.txt')
    data4 = np.loadtxt('ux_7_bias_20.txt')

    n1, n2, n3, n4 = -1, -1, -1, -1
    xs1 = data1[:, 1]
    xs2 = data2[:, 1]
    xs3 = data3[:, 1]
    xs4 = data4[:, 1]
    N = len(xs1)
    for i in range(N):
        if xs1[i] > 160:
            n1 = i
            break
    for i in range(N):
        if xs2[i] > 160:
            n2 = i
            break
    for i in range(N):
        if xs3[i] > 160:
            n3 = i
            break
    for i in range(N):
        if xs4[i] > 160:
            n4 = i
            break

    c  = 'brown'
    
    axes[0,0].set_aspect(1)
    axes[0,1].set_aspect(1)
    axes[1,0].set_aspect(1)
    axes[1,1].set_aspect(1)
    axes[0,0].plot(xs1[:n1], data1[:n1, 2]+4, label="\u2460", color=c)
    c1 = plt.Circle((100,60-2), 4, color='black', alpha=0.4)
    axes[0,0].add_artist(c1)

    axes[0,1].plot(xs2[:n2], data2[:n2, 2]+4, label="\u2461", color=c)
    c2 = plt.Circle((100,60-2), 4, color='black', alpha=0.4)
    axes[0,1].add_artist(c2)

    c3 = plt.Circle((100,60-2), 4, color='black', alpha=0.4)
    axes[1,0].add_artist(c3)

    c4 = plt.Circle((100,60+6-20), 4, color='black', alpha=0.4)
    axes[1,1].add_artist(c4)

    axes[1,0].plot(xs3[:n3], data3[:n3, 2]+4, label="\u2462", color=c)
    axes[1,1].plot(xs4[:n4], data4[:n4, 2]+6, label="\u2463", color=c)
    axes[0,0].set_xlim([60, 138])
    axes[0,0].tick_params(bottom = False) 
    axes[0,1].set_ylim([38, 72])
    axes[0,1].set_xlim([60, 138])
    axes[1,0].set_xlim([60, 138])
    axes[1,1].set_xlim([60, 138])
    
    axes[1,0].set_xlabel(r'$x$ (nm)')
    axes[1,1].set_xlabel(r'$x$ (nm)')
    axes[0,0].set_ylabel(r'$y$ (nm)')
    axes[1,0].set_ylabel(r'$y$ (nm)')
    axes[0,0].legend(prop={'size':12})
    axes[0,1].legend(prop={'size':12})
    axes[1,0].legend(prop={'size':12})
    axes[1,1].legend(prop={'size':12})
    axes[0,0].grid(True)
    axes[0,1].grid(True)
    axes[1,1].grid(True)
    axes[1,0].grid(True)

    plt.tight_layout()
    plt.subplots_adjust(wspace=0.05)
    plt.savefig('pinning.svg')


if __name__ == '__main__':
    plot()
