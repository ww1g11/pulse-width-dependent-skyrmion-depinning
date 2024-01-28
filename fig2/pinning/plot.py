import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt

import numpy as np

from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = 'Arial'
rcParams['savefig.dpi'] = 300
rcParams['font.size'] = 14

def plot():
    fig = plt.figure(figsize=(5,3))
    ax = plt.gca()

    #ax.set_aspect(1)
    us = [2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]

    data = np.loadtxt('pinning.txt')
    data_reduce = data[:-4, :]
    m,n = data_reduce.shape
    one = data_reduce == 1
    two = data_reduce == 2
    three = data_reduce == 3
    four = data_reduce == 4
    data_reduce[one] = 1
    data_reduce[two] = 4
    data_reduce[three] = 2
    data_reduce[four] = 3  

    plt.imshow(data_reduce, origin='lower', cmap='Set3', alpha=0.95, extent=(0,30,us[0],us[m-1]), aspect='auto')
    plt.xlabel('Impact parameter $b$ (nm)')
    plt.ylabel('$u$ (m/s)')

    plt.tight_layout()
    plt.savefig('pinning.svg')


if __name__ == '__main__':

    plot()
