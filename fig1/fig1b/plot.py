import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.cm as cm
#plt.style.use('seaborn')

import numpy as np

from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = 'Arial'
rcParams['savefig.dpi'] = 300
rcParams['font.size'] = 14

def plot(name, nx=400, ny=128, R=3, type=1):
    fig = plt.figure(figsize=(5,2))
    ax = plt.gca()
    plt.xlim(0,nx)
    plt.ylim(0,ny)

    pos = np.loadtxt('pos_r50.txt')
    for p  in pos:
        c1 = plt.Circle((p[0], p[1]), R, color='lightgray', alpha=0.99)
        ax.add_artist(c1)
    
    data = np.loadtxt('XY/%s.txt'%name)
    time = data[:,0]
    X = data[:,1]/2.0
    Y = data[:,2]/2.0
    n = -1
    for i in range(len(time)):
        if X[i]>373:
            n = i
            break
    print(name, "  ", n)

    n1 = 46
    line = plt.Line2D(X[:n1], Y[:n1], dashes=(1.6,1.6), color='blue', linewidth=1.8)
    ax.add_artist(line)

    line = plt.Line2D(X[n1:n], Y[n1:n], dashes=(1,1), color='green', linewidth=1.8)
    ax.add_artist(line)

    R = 6
    c1 = plt.Circle((X[0], Y[0]), R, color='red', alpha=0.99, fill=False)
    ax.add_artist(c1)

    c1 = plt.Circle(((X[n1-1]+X[n1])/2, (Y[n1-1]+Y[n1])/2), R, color='blue', alpha=0.99, fill=False, linestyle='--')
    ax.add_artist(c1)

    c1 = plt.Circle((X[n-1], Y[n-1]), R, color='green', alpha=0.99, fill=False, linestyle='--')
    ax.add_artist(c1)

    plt.xticks([0, 400])
    plt.yticks([0, 140])
    plt.xlabel("$X$ (nm)", labelpad=-10)
    plt.ylabel("$Y$ (nm)", labelpad=-10)

    ax.set_aspect('equal')
    ax.set_facecolor('linen')
    plt.savefig('%s.svg'%name)


if __name__ == '__main__':
    plot(name='ux_12_R_3_Ku_30000_p_50_y_98', type=3) #pinning, can move
