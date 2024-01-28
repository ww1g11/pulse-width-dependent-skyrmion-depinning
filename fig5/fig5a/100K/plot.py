import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
#plt.style.use('seaborn')
import matplotlib.gridspec as gridspec
import matplotlib.cm as cm
mpl.rcParams['font.size'] = 14
import numpy as np
import os

font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 16,
        }

def custom_legend(legend):
    frame = legend.get_frame()
    frame.set_facecolor('0.90')

    # Set the fontsize
    for label in legend.get_texts():
        label.set_fontsize(11)

    for label in legend.get_lines():
        label.set_linewidth(1.5)  # the legend line width

def plot(u=0):
    data = np.load('xy_%g.npy'%u)
    xy = data[0,:,:]
    #xs, ys = solve(ts, u)

    fig = plt.figure(figsize=(5,3.2))
    ts = np.linspace(0, 1e-9, 10, endpoint=True)
    plt.plot(xy[:,0]*1e9, '-', label='X', markersize=5)
    plt.plot(xy[:,1]*1e9, '-', label='Y', markersize=5.6)

    plt.legend()
    plt.xlabel('Time (ns)')
    plt.ylabel(r'Position (nm)')
    plt.tight_layout()
    plt.savefig('u_%g.jpg'%(u), dpi=300)
    return 0

def compute_P_new(u, Rc=2*11.98):
    data = np.load('xy_%g.npy'%u)
    print(data.shape)
    N = data.shape[0]
    Ps = np.zeros(50)
    R = (data[:,:,0]**2 + data[:,:,1]**2)**0.5*1e9
    p = R > Rc
    return sum(p)/N

def compute_all_P():
    all_p = []
    us = [0.2*i for i in range(31)]
    for u in us:
        p = compute_P_new(u)
        all_p.append(p)
    np.savetxt('all_p.txt', all_p)

    fig = plt.figure(figsize=(5,4))
    ax = fig.add_subplot(1, 1, 1)

    plt.xlabel('Pulse Width (ns)')
    plt.ylabel(r'u (m/s)')
    im = ax.imshow(all_p, interpolation='bilinear', origin='lower',aspect='auto',
                cmap='tab20c', extent=[0, 20, 0, 6], vmax=1, vmin=0)
    plt.contour(all_p, [0.8], cmap='Pastel1',  origin='lower', extent=[0, 20, 0, 6], linestyles='dashed')
    fig.colorbar(im, ax=ax)


    plt.tight_layout()
    plt.savefig('u_p.jpg', dpi=300)



with plt.style.context('seaborn-deep'):
    plot()
    compute_all_P()
    pass
