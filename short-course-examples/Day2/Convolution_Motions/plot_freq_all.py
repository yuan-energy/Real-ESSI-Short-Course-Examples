# *************************
# *************************
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import math
def FFT(x,dt,maxf,plot=True):
	# Number of samplepoints
	N = x.size;
	# Total Time 
	T = N*dt;
	# sample dpacing is dt
	# sampling frequency
	Fs = 1/dt;
	xfft  = scipy.fftpack.fft(x);
	xfreq = np.linspace(0.0, Fs/2, N/2);
	xfftHalf = 2.0/N * np.abs(xfft[:N//2]);
	xfftHalf[0] = xfftHalf[0]/2;
	# #############################
	import matplotlib.pylab as pylab
	params = {'legend.fontsize': 'x-large',
	          'figure.figsize': (10, 8),
	         'axes.labelsize': 'x-large',
	         'axes.titlesize':'x-large',
	         'xtick.labelsize':'x-large',
	         'ytick.labelsize':'x-large'}
	pylab.rcParams.update(params)
	# #############################
	if(plot):
		fig, ax = plt.subplots()
		ax.plot(xfreq, xfftHalf,'-k',linewidth=3)
		if(maxf is not None):
			plt.xlim(0, maxf)
		plt.ylabel(' Acceleration [m/s^2] ')
		plt.xlabel(' Frequency [Hz] ')
		plt.grid()
		plt.savefig("top_acc_freq.pdf")
		plt.show()
	return xfreq, xfftHalf
# *************************
# *************************





in_filename = './element1m/motion/ormsby_acc.dat'
filename1 = 'element1m/test_motion_node_6_x_acce.txt'
filename2 = 'element5m/test_motion_node_6_x_acce.txt'
filename3 = 'element20m/test_motion_node_6_x_acce.txt'

in_data = np.loadtxt(in_filename)

data1 = np.loadtxt(filename1)
data2 = np.loadtxt(filename2)
data3 = np.loadtxt(filename3)

times = data1[:,0]
dt = times[1] - times[0]

in_time = in_data[:,0]
in_acc = in_data[:,1]

acc1 = data1[:,1]
acc2 = data2[:,1]
acc3 = data3[:,1]

[f_in_time, f_in_acc] = FFT( in_acc, in_time[1]-in_time[0] , 20, plot=False)
[f_times, f_acc1] = FFT( acc1, dt, 20, plot=False)
[f_times, f_acc2] = FFT( acc2, dt, 20, plot=False)
[f_times, f_acc3] = FFT( acc3, dt, 20, plot=False)


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

ax.semilogx(f_in_time, f_in_acc, 'k-' , linewidth=2, label="input")
ax.semilogx(f_times, f_acc1, 'r-' , linewidth=2, label="element size = 1m")
ax.semilogx(f_times, f_acc2, 'g-' , linewidth=2, label="element size = 5m")
ax.semilogx(f_times, f_acc3, 'b-' , linewidth=2, label="element size = 20m")

# ax.semilogx(f_wave_times, f_wave_acc, 'g-' , linewidth=3, label="wave field")

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.7, box.height])

plt.xlim([1,10])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.ylabel(' Acceleration [m/s^2] ')
plt.xlabel(' Frequency [Hz] ')
# *****************************
d = np.linspace(1,10,10) 
plt.xticks(d)
# *****************************
ax.grid()
plt.savefig("top_acc_feq_all.pdf")
plt.show()

