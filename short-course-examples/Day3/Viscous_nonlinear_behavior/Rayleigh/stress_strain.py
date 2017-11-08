#This script read the HDF5 output file, subtract stress and strain of some nodes
#Then output these into a dat file for further analysis
#Written by: Han Yang
#Date: Mar 2016

import h5py
import scipy as sp
import time
import matplotlib.pyplot as plt
import sys
from matplotlib import rc
from matplotlib.ticker import FormatStrFormatter
import linecache
import numpy as np


majorFormatter = FormatStrFormatter('%.2f')

#Prescribed Parameters
start_step = 000
dt = 0.01
num_el_ele = 250
num_total_ele = 300
plastified_ele = 250

#Open the HDF5 output of the full model
filename = sys.argv[1]
h5file = h5py.File(filename,'r')

Time = h5file["time"][:]
steps = len(Time) - start_step
#print steps

Element_Outputs = h5file['/Model/Elements/Element_Outputs'][:,:]
Gauss_Outputs = h5file['/Model/Elements/Gauss_Outputs'][:,:]
Generalized_Displacements = h5file['/Model/Nodes/Generalized_Displacements'][:,:]
Energy_Total = h5file['/Energy/Energy_Brick/Energy_Total'][:,:]
Energy_Element = h5file['/Energy/Energy_Brick/Energy_Element'][:,:]

time = sp.zeros(shape=(steps), dtype=sp.double)
shear_stress = sp.zeros(shape=(steps), dtype=sp.double)
shear_strain = sp.zeros(shape=(steps), dtype=sp.double)

total_KE = sp.zeros(shape=(steps), dtype=sp.double)
total_SE = sp.zeros(shape=(steps), dtype=sp.double)
total_PF = sp.zeros(shape=(steps), dtype=sp.double)
total_PD = sp.zeros(shape=(steps), dtype=sp.double)
total_VD = sp.zeros(shape=(steps), dtype=sp.double)
total_ND = sp.zeros(shape=(steps), dtype=sp.double)

top_KE = sp.zeros(shape=(steps), dtype=sp.double)
top_SE = sp.zeros(shape=(steps), dtype=sp.double)
top_PF = sp.zeros(shape=(steps), dtype=sp.double)
top_PD = sp.zeros(shape=(steps), dtype=sp.double)
top_VD = sp.zeros(shape=(steps), dtype=sp.double)

bottom_KE = sp.zeros(shape=(steps), dtype=sp.double)
bottom_SE = sp.zeros(shape=(steps), dtype=sp.double)
bottom_VD = sp.zeros(shape=(steps), dtype=sp.double)

disp_top = sp.zeros(shape=(steps), dtype=sp.double)
disp_bottom = sp.zeros(shape=(steps), dtype=sp.double)

external_load = sp.zeros(shape=(steps), dtype=sp.double)
input_work = sp.zeros(shape=(steps), dtype=sp.double)

for i in range(0, steps):
	time[i] = Time[i+start_step]

	shear_strain[i] = Gauss_Outputs[plastified_ele*8*18+4][i+start_step]
	shear_stress[i] = Gauss_Outputs[plastified_ele*8*18+16][i+start_step]

	total_KE[i] = Energy_Total[0][i+start_step]
	total_SE[i] = Energy_Total[1][i+start_step]
	total_PF[i] = Energy_Total[2][i+start_step]
	total_PD[i] = Energy_Total[4][i+start_step]
	total_VD[i] = Energy_Total[5][i+start_step]

	disp_top[i] = Generalized_Displacements[-3][i+start_step]
	disp_bottom[i] = Generalized_Displacements[24][i+start_step]

	external_load[i] = Element_Outputs[12][i+start_step]

	for j in range(0, num_el_ele):
		bottom_KE[i] += Energy_Element[12*j+1][i+start_step]
		bottom_SE[i] += Energy_Element[12*j+3][i+start_step]
		bottom_VD[i] += Energy_Element[12*j+11][i+start_step]

	for j in range(num_el_ele, num_total_ele):
		top_KE[i] += Energy_Element[12*j+1][i+start_step]
		top_SE[i] += Energy_Element[12*j+3][i+start_step]
		top_PF[i] += Energy_Element[12*j+5][i+start_step]
		top_PD[i] += Energy_Element[12*j+9][i+start_step]
		top_VD[i] += Energy_Element[12*j+11][i+start_step]
	

for i in range(1, steps):
	input_work[i] = input_work[i-1]-2*(external_load[i]+external_load[i-1])*(disp_bottom[i]-disp_bottom[i-1])
	total_ND[i] = input_work[i] - total_KE[i] - total_SE[i] - total_PF[i] - total_PD[i] - total_VD[i]



sample_freq = np.fft.rfftfreq(int(steps), d=dt)
total_KE_fft = np.fft.rfft(total_KE)/(steps/2.)
total_SE_fft = np.fft.rfft(total_SE)/(steps/2.)
input_work_fft = np.fft.rfft(input_work)/(steps/2.)

disp_top_fft = np.fft.rfft(disp_top)/(steps/2.)
disp_bottom_fft = np.fft.rfft(disp_bottom)/(steps/2.)






line_width = 0.5
energy_plot_scale = 1e-6
stress_plot_scale = 1e-6
strain_plot_scale = 1e4

plt.figure(1)
plt.plot(shear_strain*strain_plot_scale, shear_stress*stress_plot_scale, 'k-')
plt.ylabel('Stress (MPa)')
plt.xlabel('Strain (*10-4)')
plt.grid()
plt.savefig('Stress-Strain.pdf', bbox_inches='tight')

plt.figure(2)
input_work_plt, = plt.plot(time, input_work*energy_plot_scale, 'k-', linewidth=5*line_width)
total_SE_plt, = plt.plot(time, total_SE*energy_plot_scale, 'b-', linewidth=line_width)
total_KE_plt, = plt.plot(time, total_KE*energy_plot_scale, 'g-', linewidth=line_width)
total_PF_plt, = plt.plot(time, total_PF*energy_plot_scale, 'k-', linewidth=line_width)
total_PD_plt, = plt.plot(time, total_PD*energy_plot_scale, 'r-', linewidth=line_width)
total_VD_plt, = plt.plot(time, total_VD*energy_plot_scale, 'm-', linewidth=line_width)
total_ND_plt, = plt.plot(time, total_ND*energy_plot_scale, 'c-', linewidth=line_width)
plt.xlabel('Time [s]')
plt.ylabel('Energy [MJ]')
plt.grid()
plt.gca().set_xlim(0, 10)
# plt.gca().set_ylim(0, 250)
plt.legend([total_KE_plt, total_SE_plt, total_PF_plt, total_PD_plt, total_VD_plt, total_ND_plt, input_work_plt], ['Kinetic Energy', 'Strain Energy', 'Plastic Free Energy', 'Plastic Dissipation', 'Viscous Damping', 'Numerical Damping', 'Input Work'], loc = 1)
plt.savefig('Total_Energy_Results.pdf', bbox_inches='tight')

plt.figure(3)
top_SE_plt, = plt.plot(time, top_SE*energy_plot_scale, 'b-', linewidth=line_width)
top_KE_plt, = plt.plot(time, top_KE*energy_plot_scale, 'g-', linewidth=line_width)
top_PF_plt, = plt.plot(time, top_PF*energy_plot_scale, 'k-', linewidth=line_width)
top_PD_plt, = plt.plot(time, top_PD*energy_plot_scale, 'r-', linewidth=line_width)
top_VD_plt, = plt.plot(time, top_VD*energy_plot_scale, 'm-', linewidth=line_width)
top_RD_plt, = plt.plot(time, (bottom_KE+bottom_SE+bottom_VD)*energy_plot_scale, 'c-', linewidth=line_width)
plt.xlabel('Time [s]')
plt.ylabel('Energy [MJ]')
plt.grid()
plt.gca().set_xlim(0, 10)
# plt.gca().set_ylim(0, 250)
plt.legend([top_KE_plt, top_SE_plt, top_PF_plt, top_PD_plt, top_VD_plt, top_RD_plt], ['Kinetic Energy', 'Strain Energy', 'Plastic Free Energy', 'Plastic Dissipation', 'Viscous Damping', '\"Outside Energy\"'], loc = 1)
plt.savefig('Top_Energy_Results.pdf', bbox_inches='tight')

# plt.figure(4)
# external_input_work_plt, = plt.plot(time, external_input_work, 'k-', linewidth=line_width)
# total_material_energy_plt, = plt.plot(time, total_material_energy+beam_ND, 'b-', linewidth=line_width)
# ND_PF_PD_plt, = plt.plot(time, beam_PW+beam_ND, 'c-', linewidth=line_width)
# PF_PD_plt, = plt.plot(time, beam_PW, 'm-', linewidth=line_width)
# PD_plt, = plt.plot(time, beam_PD, 'r-', linewidth=line_width)
# plt.xlabel('Time [s]')
# plt.ylabel('Energy [J]')
# plt.grid()
# plt.legend([external_input_work_plt, total_material_energy_plt, ND_PF_PD_plt, PF_PD_plt, PD_plt], ['Input Work', 'SE+ND+PF+PD', 'ND+PF+PD', 'PF+PD', 'PD'], loc = 4)
# plt.savefig('Bertero_Style_Plot.pdf', bbox_inches='tight')

# plt.figure(5)
# plt.plot(time, external_load, 'k-')
# plt.ylabel('External Load [N]')
# plt.xlabel('Time [s]')
# plt.grid()
# plt.savefig('External_Load.pdf', bbox_inches='tight')

# plt.figure(6)
# plt.plot(sample_freq, abs(external_load_fft), 'k-')
# plt.ylabel('Fourier Amplitude')
# plt.xlabel('Frequency [Hz]')
# plt.grid()
# plt.savefig('External_Load_Spectrum.pdf', bbox_inches='tight')


plt.figure(7)
top_disp_plt, = plt.plot(time, disp_top, 'r-', linewidth=line_width)
bottom_disp_plt, = plt.plot(time, disp_bottom, 'k-', linewidth=line_width)
plt.ylabel('Displacement [m]')
plt.xlabel('Time [s]')
plt.grid()
# plt.gca().set_ylim(-0.3, 0.5)
plt.legend([top_disp_plt, bottom_disp_plt], ['Top Displacement', 'Bottom Displacemnt'], loc = 4)
plt.savefig('Displacement.pdf', bbox_inches='tight')

# plt.figure(8)
# plt.plot(time, input_work, 'k-')
# plt.ylabel('Input Work [J]')
# plt.xlabel('Time [s]')
# plt.grid()
# plt.savefig('Input_Work.pdf', bbox_inches='tight')

plt.figure(9)
disp_top_fft_plt, = plt.plot(sample_freq, abs(disp_top_fft), 'r-', linewidth=line_width)
disp_bottom_fft_plt, = plt.plot(sample_freq, abs(disp_bottom_fft), 'k-', linewidth=line_width)
plt.ylabel('Fourier Amplitude')
plt.xlabel('Frequency [Hz]')
plt.grid()
plt.gca().set_xlim(0, 10)
# plt.gca().set_ylim(0, 0.014)
plt.legend([disp_top_fft_plt, disp_bottom_fft_plt], ['Top Displacement', 'Bottom Displacement'], loc = 1)
plt.savefig('Displacement_Spectrum.pdf', bbox_inches='tight')

# plt.figure(10)
# SE_fft_plt, = plt.plot(sample_freq, abs(beam_SE_fft), 'b-', linewidth=line_width)
# KE_fft_plt, = plt.plot(sample_freq, abs(beam_KE_fft), 'g-', linewidth=line_width)
# # PF_fft_plt, = plt.plot(sample_freq, abs(beam_PF_fft), 'c-', linewidth=line_width)
# # PD_fft_plt, = plt.plot(sample_freq, abs(beam_PD_fft), 'm-', linewidth=line_width)
# ND_fft_plt, = plt.plot(sample_freq, abs(beam_ND_fft), 'r-', linewidth=line_width)
# # IW_fft_plt, = plt.plot(sample_freq, abs(external_input_work_fft), 'k-', linewidth=line_width)
# plt.xlabel('Frequency [Hz]')
# plt.ylabel('Fourier Amplitude')
# plt.grid()
# plt.gca().set_xlim(0, 20)
# plt.gca().set_ylim(0, 10000)
# plt.legend([KE_fft_plt, SE_fft_plt, ND_fft_plt], ['Kinetic Energy (KE)', 'Strain Energy (SE)', 'Numerical Dissipation (ND)'], loc = 1)
# plt.savefig('Energy_Results_Spectrum.pdf', bbox_inches='tight')

