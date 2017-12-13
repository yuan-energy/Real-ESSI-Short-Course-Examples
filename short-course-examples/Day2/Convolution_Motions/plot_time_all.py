# *************************
# *************************
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import math

import sys
# filename = sys.argv[1]

in_filename = './element1m/motion/ormsby_acc.dat'
filename1 = 'element1m/test_motion_node_6_x_acce.txt'
filename2 = 'element5m/test_motion_node_6_x_acce.txt'
filename3 = 'element20m/test_motion_node_6_x_acce.txt'

in_data = np.loadtxt(in_filename)

data1 = np.loadtxt(filename1)
data2 = np.loadtxt(filename2)
data3 = np.loadtxt(filename3)

times = data1[:,0]

in_time = in_data[:,0]
in_acc = in_data[:,1]

acc1 = data1[:,1]
acc2 = data2[:,1]
acc3 = data3[:,1]

# #############################
import matplotlib.pylab as pylab
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (12, 8),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)
# #############################

fig = plt.figure()
ax = plt.subplot(111)

ax.plot(in_time, in_acc, 'k-' , linewidth=3, label="input")
ax.plot(times, acc1, 'r-' , linewidth=3, label="element size = 1m")
ax.plot(times, acc2, 'g-' , linewidth=3, label="element size = 5m")
ax.plot(times, acc3, 'b-' , linewidth=3, label="element size = 20m")

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.75, box.height])

ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.ylabel(' Acceleration [m/s^2] ')
plt.xlabel(' Times [s] ')
ax.grid()
plt.savefig("top_acc_time_all.pdf")
plt.show()


# dt = times[1] - times[0]

# FFT(acc, dt, 20)




