# *************************
# *************************
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import math

import sys
# filename = sys.argv[1]

in_filename = 'ormsby_acc.dat'
filename2 = 'elemLen1m/top_acc.txt'
filename3 = 'elemLen5m/top_acc.txt'
filename4 = 'elemLen10m/top_acc.txt'
filename5 = 'elemLen20m/top_acc.txt'

in_data = np.loadtxt(in_filename)

data2 = np.loadtxt(filename2)
data3 = np.loadtxt(filename3)
data4 = np.loadtxt(filename4)
data5 = np.loadtxt(filename5)

wave_data = np.loadtxt('convolution/top_at_depth_0_acc.txt')
wave_time = wave_data[:,0]
wave_acc = wave_data[:,1]

times = data2[:,0]

in_time = in_data[:,0]
in_acc = in_data[:,1]

acc2 = data2[:,1]
acc3 = data3[:,1]
acc4 = data4[:,1]
acc5 = data5[:,1]

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

ax.plot(in_time, in_acc, 'r-' , linewidth=3, label="input")
ax.plot(times, acc2, 'k-' , linewidth=3, label="element size = 1m")
ax.plot(times, acc4, 'k--' , linewidth=3, label="element size = 10m")
ax.plot(times, acc5, 'b-' , linewidth=3, label="element size = 20m")


ax.plot(wave_time, wave_acc, 'g-' , linewidth=3, label="wave field")

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.75, box.height])

ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.ylabel(' Acceleration [m/s^2] ')
plt.xlabel(' Times [s] ')
ax.grid()
plt.savefig("top_acc_time_all_wave.pdf")
plt.show()


# dt = times[1] - times[0]

# FFT(acc, dt, 20)




