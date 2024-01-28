import matplotlib as mpl
mpl.use("Agg")
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.cm as cm

import numpy as np

from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = 'Arial'
rcParams['savefig.dpi'] = 300
rcParams['font.size'] = 14


def custom_legend(legend):
    frame = legend.get_frame()
    frame.set_facecolor('0.90')

    # Set the fontsize
    for label in legend.get_texts():
        label.set_fontsize(11)

    for label in legend.get_lines():
        label.set_linewidth(1.5)  # the legend line width

def analytical(beta):
    D_G = 1.2
    return 1/np.sqrt(1+D_G**2*beta**2)

def plot_uc():


    data = np.loadtxt('uc.txt')

    betas = np.linspace(0, 6, 100)

    fig = plt.figure(figsize=(4, 3))
 
    plt.plot(data[:, 0], data[:, 1]/data[0, 1], 's', label='Simulation', color='C2')
    plt.plot(betas, analytical(betas), '-', label='Analytical', color='C4')

    plt.xlabel(r'$\beta$')
    plt.ylabel(r'$u_c(\beta)/u_c(0)$')

    plt.legend()

    plt.tight_layout()
    fig.savefig("fig4b.svg")


plot_uc()
