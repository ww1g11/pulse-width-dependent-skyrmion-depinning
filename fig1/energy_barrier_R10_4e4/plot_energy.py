import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
plt.style.use('seaborn')

from scipy.optimize import curve_fit

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


def exp_model(x, A, b, c):
    return (A*x**2)*np.exp(-b*x**2)

def plot_energy_fitting():

    data = np.loadtxt('energy.txt')

    fig = plt.figure(figsize=(4,1.5))
    xs = data[:, 0] -  data[0, 0] 
    ys = data[:, 1] -  data[0, 1] 
    rs = (xs**2 + ys**2)**0.5
    meV = 1.60217662e-19*1e-3
    energy = (data[:, 2]- data[-1, 2])/meV

    Ld = 60
    plt.plot(rs/Ld, energy, label='Simulation')
    plt.ylabel(r'$\Delta E$ (meV)')
    plt.xlabel(r'$R/L_D$')

    params, covariance = curve_fit(exp_model, rs/Ld, energy, p0=(200, 16, 0))

    A, b, c = params
    print(params)
    plt.plot(rs/Ld, exp_model(rs/Ld, A, b, c), color='r', linestyle='--', linewidth=1, label='Fitting')
    plt.legend(fontsize=10)
    ax = plt.gca()
    ax.xaxis.set_label_coords(0.96, -0.07)
    labels = [item for item in ax.get_xticklabels()]
    print(labels)
    locs = [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2]
    labels = [str(i) for i in locs]
    plt.xticks(locs, labels)
    plt.xlim([-0.05, 1.43])


    plt.tight_layout()
    plt.subplots_adjust(left=0.14, bottom=0.15, right=0.99, top=0.96)

    plt.savefig("fig1a.svg")

plot_energy_fitting()
