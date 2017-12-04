# -*- coding: utf-8 -*-
# @Author: hexiang
# @Date:   2017-11-11 17:16:26
# @Last Modified by:   hexiang6666
# @Last Modified time: 2017-12-03 02:42:20


#### This is script to plot the motion response of the surface center of ESSI box ######### 

import h5py
import scipy as sp
import time
import pickle

import matplotlib.pyplot as plt

from obspy import read

import sys

from scipy.fftpack import fft


sp.set_printoptions(threshold='nan')


st_x= read('./3D_motion/E_015_015_000.x', debug_headers=True);

st_y= read('./3D_motion/E_015_015_000.y', debug_headers=True);

st_z= read('./3D_motion/E_015_015_000.z', debug_headers=True);


Time_step = st_x[0].stats.delta; 

No_time_step = st_x[0].data.shape[0]; 

print Time_step; 

Time = [Time_step*x for x in xrange(0, No_time_step)]; 

l= range(0,int(No_time_step)); 

frequency = sp.array(l, dtype=int)*1.0/(No_time_step*Time_step)

dis_x = sp.zeros((No_time_step,1));

acc_x = sp.zeros((No_time_step,1)); 

dis_y = sp.zeros((No_time_step,1));

acc_y = sp.zeros((No_time_step,1)); 

dis_z = sp.zeros((No_time_step,1));

acc_z = sp.zeros((No_time_step,1)); 



vel_x = st_x[0].data; 

vel_y = st_y[0].data; 

vel_z = st_z[0].data; 


vel_y = vel_y*(-1.0);

vel_z = vel_z*(-1.0);


for x in xrange(1,No_time_step):
	
	dis_x[x,0] = dis_x[x-1,0] + vel_x[x]*Time_step; 

	acc_x[x,0] = (vel_x[x] - vel_x[x-1])/Time_step; 

	dis_y[x,0] = dis_y[x-1,0] + vel_y[x]*Time_step; 

	acc_y[x,0] = (vel_y[x] - vel_y[x-1])/Time_step; 

	dis_z[x,0] = dis_z[x-1,0] + vel_z[x]*Time_step; 

	acc_z[x,0] = (vel_z[x] - vel_z[x-1])/Time_step; 


acc_fft_x = abs(fft(acc_x[:,0]))*2/No_time_step ; 

acc_fft_y = abs(fft(acc_y[:,0]))*2/No_time_step ;

acc_fft_z = abs(fft(acc_z[:,0]))*2/No_time_step ;

dis_fft_x = abs(fft(dis_x[:,0]))*2/No_time_step ; 

dis_fft_y = abs(fft(dis_y[:,0]))*2/No_time_step ; 

dis_fft_z = abs(fft(dis_z[:,0]))*2/No_time_step ; 



fig, (ax1,ax2) = plt.subplots(2,1)

ax1.plot(Time, dis_x, '-r', label= 'X' );

ax1.plot(Time, dis_y, '-k', label= 'Y' );

ax1.plot(Time, dis_z, '-b', label= 'Z' );

ax1.legend()

ax1.set(xlabel = '', ylabel = 'Displacement [m]')
 

ax2.plot(Time, acc_x, '-r', label= 'X' );

ax2.plot(Time, acc_y, '-k', label= 'Y' );

ax2.plot(Time, acc_z, '-b', label= 'Z' );

ax2.legend()

ax2.set(xlabel = 'Time [s]', ylabel = 'Acceleration [$m/s^2$]')

plt.savefig('motion.pdf'); 

# plt.show(); 



fig1, (ax3,ax4) = plt.subplots(2,1)

ax3.plot(frequency[1:], dis_fft_x[1:], '-r', label= 'X' );

ax3.plot(frequency[1:], dis_fft_y[1:], '-k', label= 'Y' );

ax3.plot(frequency[1:], dis_fft_z[1:], '-b', label= 'Z' );

ax3.set_xlim([0,15])

ax3.legend()

ax3.set(xlabel = '', ylabel = 'FFT Displacement [m]')
 

ax4.plot(frequency, acc_fft_x, '-r', label= 'X' );

ax4.plot(frequency, acc_fft_y, '-k', label= 'Y' );

ax4.plot(frequency, acc_fft_z, '-b', label= 'Z' );

ax4.set_xlim([0,15])

ax4.legend()

ax4.set(xlabel = 'Frequency [Hz]', ylabel = 'FFT Acceleration [$m/s^2$]')

plt.savefig('motion_fft.pdf'); 

# plt.show(); 


### For printing 

# print "Displecement x direction: \n", dis_x;

# print "Displecement y direction: \n", dis_y;

# print "Displecement z direction: \n", dis_z;

# print "Acceleration x direction: \n", acc_x;

# print "Acceleration y direction: \n", acc_y;

# print "Acceleration z direction: \n", acc_z;




