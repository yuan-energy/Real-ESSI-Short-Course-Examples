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





in_filename = 'ormsby_acc.dat'
# in_filename = 'ricker_acc.txt'
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
dt = times[1] - times[0]

in_time = in_data[:,0]
in_acc = in_data[:,1]

acc2 = data2[:,1]
acc3 = data3[:,1]
acc4 = data4[:,1]
acc5 = data5[:,1]

[f_in_time, f_in_acc] = FFT( in_acc, in_time[1]-in_time[0] , 20, plot=False)
[f_times, f_acc2] = FFT( acc2, dt, 20, plot=False)
[f_times, f_acc3] = FFT( acc3, dt, 20, plot=False)
[f_times, f_acc4] = FFT( acc4, dt, 20, plot=False)
[f_times, f_acc5] = FFT( acc5, dt, 20, plot=False)

[f_wave_times, f_wave_acc] = FFT( wave_acc, dt, 20, plot=False)


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

ax.semilogx(f_in_time, f_in_acc, 'k-' , linewidth=3, label="input")
# ax.semilogx(f_times, f_acc2, 'b-' , linewidth=3, label="element size = 1m")
ax.semilogx(f_times, f_acc3, 'r-' , linewidth=3, label="element size = 5m")
ax.semilogx(f_times, f_acc4, 'g-' , linewidth=3, label="element size = 10m")
ax.semilogx(f_times, f_acc5, 'b-' , linewidth=3, label="element size = 20m")

# ax.semilogx(f_wave_times, f_wave_acc, 'g-' , linewidth=3, label="wave field")

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.7, box.height])

plt.xlim([1,100])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.ylabel(' Acceleration [m/s^2] ')
plt.xlabel(' Frequency [Hz] ')
ax.grid()
plt.savefig("top_acc_feq_all.pdf")
plt.show()