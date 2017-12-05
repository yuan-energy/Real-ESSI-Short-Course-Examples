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
	if(plot):
		fig, ax = plt.subplots()
		ax.plot(xfreq, xfftHalf,'-k')
		if(maxf is not None):
			plt.xlim(0, maxf)
		plt.ylabel('Fourier transform |FFT(x)|')
		plt.xlabel('Frequency |Hz|')
		plt.grid()
		plt.show()
	return xfreq, xfftHalf
# *************************
# *************************


import numpy as np 
from numpy import pi
import matplotlib.pyplot as plt

f1 = 1 
f2 = 2 
f3 = 3
f4 = 4
ts = 1  
time_len = 10 
time_step = 0.01
Nstep = time_len / time_step + 1
times = np.linspace(0,time_len, Nstep)

# A=( pi * f4**2 / ( f4 - f3 ) * (np.sinc(pi * f4 * (times - ts)))**2 -\
#     pi * f3**2 / ( f4 - f3 ) * (np.sinc(pi * f3 * (times - ts)))**2 )\
#   -(pi * f2**2 / ( f2 - f1 ) * (np.sinc(pi * f2 * (times - ts)))**2  \
#    -pi * f1**2 / ( f2 - f1 ) * (np.sinc(pi * f1 * (times - ts)))**2 )


f1 = 2.0
f2 = 3.0
f3 = 4.0
f4 = 5.0
# A = 0.01
ts = 3.0001
A = (np.pi*f4*f4/(f4-f3)*(np.sin(np.pi*f4*(times-ts))/(np.pi*f4*(times-ts)))*(np.sin(np.pi*f4*(times-ts))/(np.pi*f4*(times-ts)))
				- np.pi*f3*f3/(f4-f3)*(np.sin(np.pi*f3*(times-ts))/(np.pi*f3*(times-ts)))*(np.sin(np.pi*f3*(times-ts))/(np.pi*f3*(times-ts)))
				- np.pi*f2*f2/(f2-f1)*(np.sin(np.pi*f2*(times-ts))/(np.pi*f2*(times-ts)))*(np.sin(np.pi*f2*(times-ts))/(np.pi*f2*(times-ts)))
				+ np.pi*f1*f1/(f2-f1)*(np.sin(np.pi*f1*(times-ts))/(np.pi*f1*(times-ts)))*(np.sin(np.pi*f1*(times-ts))/(np.pi*f1*(times-ts))))



# scale = 0.01
# scale = 1
acc = A / np.amax(A)
plt.plot(times, acc)
plt.show()


# # ***************************************
# # ***************************************
# T =  time_step
# N = len(times)

# yf = scipy.fftpack.fft(acc)
# xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

# yf_pl = 2.0/N * np.abs(yf[:N//2]) 

# plt.plot(xf, yf_pl)
# plt.xlim(0, 20)
# plt.show()
# # ***************************************
# # ***************************************

FFT(acc, time_step, 20)

dt = times[1]-times[0]
Nstep = len(times)



vel = np.zeros(Nstep)
for i in range(1,Nstep):
	vel[i] = vel[i-1] + dt * acc[i-1] 


dis = np.zeros(Nstep)
for i in range(1,Nstep):
	dis[i] = dis[i-1] + dt * vel[i-1] + 0.5 * acc[i-1] * dt * dt 

plt.plot(times, vel)
plt.show()
plt.plot(times, dis)
plt.show()



with open("ormsby_acc.dat",'w') as f:
	for i in range(len(times)):
		f.write(str(times[i]) + " \t " + str(acc[i]) + " \n")

with open("ormsby_vel.dat",'w') as f:
	for i in range(len(times)):
		f.write(str(times[i]) + " \t " + str(vel[i]) + " \n")

with open("ormsby_dis.dat",'w') as f:
	for i in range(len(times)):
		f.write(str(times[i]) + " \t " + str(dis[i]) + " \n")

