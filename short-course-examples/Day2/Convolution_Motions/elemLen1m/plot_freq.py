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

import sys
filename = sys.argv[1]
# filename = "top_acc.txt"
data = np.loadtxt(filename)
times = data[:,0]
acc = data[:,1]
dt = times[1] - times[0]

FFT(acc, dt, 20)




