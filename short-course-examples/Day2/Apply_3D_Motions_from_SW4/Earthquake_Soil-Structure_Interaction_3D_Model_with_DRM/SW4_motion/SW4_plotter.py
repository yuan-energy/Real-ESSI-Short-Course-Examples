# -*- coding: utf-8 -*-
# @Author: hexiang
# @Date:   2017-11-20 20:03:07
# @Last Modified by:   hexiang6666
# @Last Modified time: 2017-12-01 17:13:49


## This is a simple script to plot the result of SW4 simulation 

## To plot the displacement(or velocity, acceleration) distribution of three types of sections: Ux, Uz distribution in XZ plane and Ux, Uy distribution in XY plane and Uy, Uz distribution in YZ plane.      

import h5py

import numpy as np

import time

import pickle

import math

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import axes3d

from obspy import read

import sys

import os

np.set_printoptions(threshold='nan')

###################### Define Usr input #####################################

ESSI_box_length = 300;  ## Dimension in X direction 

ESSI_box_width = 300;   ## Dimension in Y direction 

ESSI_box_height = 100;  ## Dimension in Z direction 

ESSI_x_spacing = 10;   ## ESSI nodes spacing in x direction 

ESSI_y_spacing = 10;   ## ESSI nodes spacing in y direction 

ESSI_z_spacing = 10;   ## ESSI nodes spacing in z direction 

ESSI_box_x_origin = 2100;  ## starting point x, minumum x  

ESSI_box_y_origin = 2300;  ## starting point y, minimum y

ESSI_box_z_origin = 0;   ## starting point z, minimum z 

Y_xz_plane = 2450;     ###   6000;         ## None;     ## 6000;   ## the coordinate of xz plane y= Y_xz_plane; if Y_xz_plane = None, then means do not need to plot displacement vector field in xz plane.   

Z_xy_plane = 0;    ## 0;    # 0;    ## the coordinate of xy plane z= Z_xy_plane; if Z_xy_plane = None, then means do not need to plot displacement vector field in xy plane.   

X_yz_plane = 2250;     ## 4000;   ## the coordinate of xy plane x= X_yz_plane; if X_yz_plane = None, then means do not need to plot displacement vector field in yz plane.   

motion_dir = './step2:SW4/3D_motion'    ## '/home/hexiang/SMR_work/smr/sw4_motion/M5.5_ESSI_srf.sw4output'; 

sampling_interval = 5; 

file_prefix = '/E'; 

file_postfix_x='.x';

file_postfix_y='.y';

file_postfix_z='.z';
 
vector_field_sampling_x = 10; 

vector_field_sampling_y = 10; 

vector_field_sampling_z = 10; 

cubic_output = False  #/False; 

XY_output =  True; 

XZ_output =  True; 

YZ_output =  True; 


##################### Ending usr input definition ###########################


Num_x_ESSI_nodes = 1+ ESSI_box_length / ESSI_x_spacing ; 

Num_y_ESSI_nodes = 1+ ESSI_box_width / ESSI_y_spacing ; 

Num_z_ESSI_nodes = 1+ ESSI_box_height / ESSI_z_spacing ; 

# print Num_x_ESSI_nodes;       ### For debugging by Hexiang

X_xz_plane, Z_xz_plane = np.meshgrid(np.arange(ESSI_box_x_origin, ESSI_box_x_origin+Num_x_ESSI_nodes*ESSI_x_spacing, vector_field_sampling_x), np.arange(ESSI_box_z_origin, ESSI_box_z_origin+Num_z_ESSI_nodes*ESSI_z_spacing, vector_field_sampling_z))

Z_xz_plane = -1 * Z_xz_plane; 

X_xy_plane, Y_xy_plane = np.meshgrid(np.arange(ESSI_box_x_origin, ESSI_box_x_origin+Num_x_ESSI_nodes*ESSI_x_spacing, vector_field_sampling_x), np.arange(ESSI_box_y_origin, ESSI_box_y_origin+Num_y_ESSI_nodes*ESSI_y_spacing, vector_field_sampling_y))

Y_xy_plane = -1 * Y_xy_plane; 

Y_yz_plane, Z_yz_plane = np.meshgrid(np.arange(ESSI_box_y_origin, ESSI_box_y_origin+Num_y_ESSI_nodes*ESSI_y_spacing, vector_field_sampling_y), np.arange(ESSI_box_z_origin, ESSI_box_z_origin+Num_z_ESSI_nodes*ESSI_z_spacing, vector_field_sampling_z))

Y_yz_plane = -1 * Y_yz_plane ; 

Z_yz_plane = -1 * Z_yz_plane ; 


X, Y, Z = np.meshgrid(np.arange(ESSI_box_x_origin, ESSI_box_x_origin+Num_x_ESSI_nodes*ESSI_x_spacing, vector_field_sampling_x), np.arange(ESSI_box_y_origin, ESSI_box_y_origin+Num_y_ESSI_nodes*ESSI_y_spacing, vector_field_sampling_y), np.arange(ESSI_box_z_origin, ESSI_box_z_origin+Num_z_ESSI_nodes*ESSI_z_spacing, vector_field_sampling_z))

Y = -1* Y; 

Z = -1* Z; 



num_sampling_x = Z_xz_plane.shape[1]; 

num_sampling_y = Y_xy_plane.shape[0];

num_sampling_z = Z_xz_plane.shape[0];  


# print "Verifying: ",  num_sampling_x , num_sampling_y, num_sampling_z ;   ### For debugging by Hexiang

#  print "I am printing", X_xz_plane.shape,  Z_xz_plane.shape ;    ### For debugging by Hexiang Wang 

# print "Verifying: ", X.shape, Y.shape, Z.shape, X[0,0,0], Y[1,0,0], X[0,1,0], Z[0,0,1]     ### For debugging by Hexiang , first index is Y, second index is X, third index is Z.  


info_file = file_prefix + '_000_000_000.x'; 

info_sta_dir = motion_dir + '/' + info_file ; 

info_station =  read(info_sta_dir, debug_headers = True)

original_time_step = info_station[0].stats.delta; 

No_original_time_step = info_station[0].data.shape[0]; 

Time = [original_time_step*x for x in xrange(0, No_original_time_step)]; 

sampled_time_step = original_time_step*sampling_interval;

sampled_No_time_step = int(math.floor((No_original_time_step-1)/sampling_interval)+1);

Sampled_Time=[i*sampled_time_step for i in xrange(0,sampled_No_time_step)];


# print "Verifying", No_original_time_step, sampled_No_time_step ;     ### For debugging by Hexiang 

### Plotting the displacement vector field in xz plane in jpg format, 

if (Y_xz_plane != None) and (XZ_output == True) :

	y = int ( math.floor(( Y_xz_plane - ESSI_box_y_origin ) / ESSI_y_spacing )) ;

	ID_y = str(y); 

	if y <10:

		ID_y= '0' + ID_y;

	if y >=100:
		
		print 'Too many stations, check if codes need modified!';

	vel_x = np.zeros((num_sampling_z, num_sampling_x, No_original_time_step)); 

	# print "array size: ", vel_x.shape   ## For debugging by Hexiang 
  
	vel_z = np.zeros((num_sampling_z, num_sampling_x, No_original_time_step));

	dis_x = np.zeros((num_sampling_z, num_sampling_x, No_original_time_step)); 

	dis_z = np.zeros((num_sampling_z, num_sampling_x, No_original_time_step));

	acc_x = np.zeros((num_sampling_z, num_sampling_x, No_original_time_step)); 

	acc_z = np.zeros((num_sampling_z, num_sampling_x, No_original_time_step));



	# sampled_vel_x = np.zeros((num_sampling_z, num_sampling_x, sampled_No_time_step));    ### we do not look at velocity

	# sampled_vel_z = np.zeros((num_sampling_z, num_sampling_x, sampled_No_time_step));

	sampled_dis_x = np.zeros((num_sampling_z, num_sampling_x, sampled_No_time_step)); 

	sampled_dis_z = np.zeros((num_sampling_z, num_sampling_x, sampled_No_time_step));

	sampled_acc_x = np.zeros((num_sampling_z, num_sampling_x, sampled_No_time_step)); 

	sampled_acc_z = np.zeros((num_sampling_z, num_sampling_x, sampled_No_time_step));



	for x1 in xrange(0,num_sampling_x):

		for x2 in xrange(0,num_sampling_z): 

			z= int ( math.floor(( - ESSI_box_z_origin -Z_xz_plane[x2,0] ) / ESSI_z_spacing )) ;

			ID_z = str(z);

			x= int ( math.floor(( X_xz_plane[0,x1] - ESSI_box_x_origin ) / ESSI_x_spacing )) ;

			ID_x = str(x);

			if x <10:
					
				ID_x= '0' + ID_x;
	
			if z <10: 
					
				ID_z= '0' + ID_z;
			

			if x >=100: 
		
				print 'Too many stations, check if codes need modified!';

	
			if z >=100:
					
				print 'Too many stations, check if codes need modified!';

			filename = file_prefix + '_0' + ID_x + '_0' + ID_y + '_0' + ID_z;

			print "Current station name " , filename;  

			filename_x = motion_dir + filename + file_postfix_x ; 

			filename_z = motion_dir + filename + file_postfix_z ; 

			sac_info_x = read(filename_x, debug_headers=True); 

			sac_info_z = read(filename_z, debug_headers=True); 

			print "x2 = ", x2, "x1= ", x1;  
				
			vel_x[x2, x1, :] = sac_info_x[0].data; 

			vel_z[x2, x1, :] = sac_info_z[0].data * (-1.0);

			print "Getting velocity at x= ", X_xz_plane[x2, x1] , ', z= ', Z_xz_plane[x2, x1];  

			for x3 in xrange(1,No_original_time_step):
				
				dis_x[:, :, x3] = dis_x[:, :, x3-1] + vel_x[:,:,x3] * original_time_step; 

				dis_z[:, :, x3] = dis_z[:, :, x3-1] + vel_z[:,:,x3] * original_time_step;

				acc_x[:, :, x3] = (vel_x[:, :, x3] - vel_x[:, :, x3-1])/original_time_step ; 

				acc_z[:, :, x3] = (vel_z[:, :, x3] - vel_z[:, :, x3-1])/original_time_step ;  

			print 'Finish Transformation from velocity to displacement and acceleration'; 

			for x4 in xrange(0, sampled_No_time_step):

				sampled_dis_x[:, :, x4]=dis_x[:, :, x4*sampling_interval];
	
				sampled_acc_x[:, :, x4]=acc_x[:, :, x4*sampling_interval];

				sampled_dis_z[:, :, x4]=dis_z[:, :, x4*sampling_interval];

				sampled_acc_z[:, :, x4]=acc_z[:, :, x4*sampling_interval];

			print 'Finish sampling of displacement and acceleration'; 



	### Use for loop to generate a time seris of sectional vector field in PDF format 

	directory_name_dis = './XZ_plane_dis_y'+str(Y_xz_plane); 

	directory_name_acc = './XZ_plane_acc_y'+str(Y_xz_plane); 

	if not os.path.exists(directory_name_dis):

		os.makedirs(directory_name_dis); 

	if not os.path.exists(directory_name_acc):

		os.makedirs(directory_name_acc); 

	for x5 in xrange(0,sampled_No_time_step):
	
	# for x5 in xrange(373, 374):    ### For testing 


		# figure_name_dis = './XZ_plane_dis/DisXZ_plane_y_'+ str(Y_xz_plane)+'_'+str(x5)+'.jpg';

		# figure_name_acc = './XZ_plane_acc/AccXZ_plane_y_'+ str(Y_xz_plane)+'_'+str(x5)+'.jpg';


		
		figure_name_dis = directory_name_dis+ '/'+str(x5)+'.jpg';

		figure_name_acc = directory_name_acc+'/'+str(x5)+'.jpg';

		fig= plt.figure()

		ax= fig.add_subplot(111); 

		# M = np.hypot(sampled_dis_x[:,:,x5], sampled_dis_z[:,:,x5]);

		# print  'Printing x displacment\n', sampled_dis_x[:,:,x5], 'Printing z displacement\n', sampled_dis_z[:,:,x5]; 

		# print  'Printing x acceleration\n', sampled_acc_x[:,:,x5], 'Printing z acceleration\n', sampled_acc_z[:,:,x5];    ### For debugging by Hexiang

		Q = plt.quiver(X_xz_plane, Z_xz_plane, sampled_dis_x[:,:,x5], sampled_dis_z[:,:,x5], scale = 0.5)    # , units='x', pivot='tip', width=0.022, scale= 500); 

		qk = plt.quiverkey(Q, 0.9, 0.9, 0.1, r'$0.1 m$', labelpos='E', coordinates='figure')

		plt.scatter(X_xz_plane, Z_xz_plane, color = 'k', s=5);

		plt.grid( ); 

		plt.xlabel('X [m]');

		plt.ylabel('Z [m]'); 


		### plot the outline of SMR 

		# plt.plot([3925, 3925], [0, -66], 'r-', [3925, 4075], [-66, -66], 'r-', [4075, 4075], [-66,0], 'r-',[4075,4015], [0, 0], 'r-', [4015, 4015], [0, 15], 'r-', [4015, 3985], [15, 15], 'r-', [3985, 3985], [15,0], 'r-' , [3985, 3925], [0,0], '-r' , linewidth= 3)


		### save figure 
		plt.savefig(figure_name_dis); 

		# plt.show(); 

		fig= plt.figure()

		ax= fig.add_subplot(111); 

		Q = plt.quiver(X_xz_plane, Z_xz_plane, sampled_acc_x[:,:,x5], sampled_acc_z[:,:,x5], scale = 7.0, units = 'inches')    # , units='x', pivot='tip', width=0.022, scale= 500); 

		qk = plt.quiverkey(Q, 0.9, 0.9, 10, r'$1 g$', labelpos='E', coordinates='figure')

		plt.scatter(X_xz_plane, Z_xz_plane, color = 'k', s=5);

		plt.grid( ); 

		plt.xlabel('X [m]');

		plt.ylabel('Z [m]'); 


		### plot the outline of SMR
		# plt.plot([3925, 3925], [0, -66], 'r-', [3925, 4075], [-66, -66], 'r-', [4075, 4075], [-66,0], 'r-',[4075,4015], [0, 0], 'r-', [4015, 4015], [0, 15], 'r-', [4015, 3985], [15, 15], 'r-', [3985, 3985], [15,0], 'r-', [3985, 3925], [0,0], '-r', linewidth= 3)


		### save the figure
		plt.savefig(figure_name_acc); 

		# plt.show(); 


	#### The following code is used to generate single time step sectional vector plot ###

	# x5 = 385;    ### Time step number of sample time step series. 

	# figure_name_dis = 'Dis_XZ_plane_y_'+ str(Y_xz_plane)+'_'+str(x5)+'.jpg';

	# figure_name_acc = 'Acc_XZ_plane_y_'+ str(Y_xz_plane)+'_'+str(x5)+'.jpg';

	# M = np.hypot(sampled_dis_x[:,:,x5], sampled_dis_z[:,:,x5]);

	# print  'Printing x displacment\n', sampled_dis_x[:,:,x5], 'Printing z displacement\n', sampled_dis_z[:,:,x5];    ### For debugging by Hexiang

	# print  'Printing x acceleration\n', sampled_acc_x[:,:,x5], 'Printing z acceleration\n', sampled_acc_z[:,:,x5];    ### For debugging by Hexiang

	# Q = plt.quiver(X_xz_plane, Z_xz_plane, sampled_dis_x[:,:,x5], sampled_dis_z[:,:,x5], scale = 1.0)    # , units='x', pivot='tip', width=0.022, scale= 500); 

	# qk = plt.quiverkey(Q, 0.9, 0.9, 0.1, r'$0.1 m$', labelpos='E', coordinates='figure')

	# plt.scatter(X_xz_plane, Z_xz_plane, color = 'k', s=5);

	# plt.grid( ); 

	# plt.xlabel('X [m]');

	# plt.ylabel('Z [m]'); 

	# plt.savefig(figure_name_dis); 

	# plt.show(); 

	# fig= plt.figure()

	# ax= fig.add_subplot(111); 

	# Q = plt.quiver(X_xz_plane, Z_xz_plane, sampled_acc_x[:,:,x5], sampled_acc_z[:,:,x5], scale = 12.0, units = 'inches')    # , units='x', pivot='tip', width=0.022, scale= 500); 

	# qk = plt.quiverkey(Q, 0.9, 0.9, 10, r'$1 g$', labelpos='E', coordinates='figure')

	# plt.scatter(X_xz_plane, Z_xz_plane, color = 'k', s=5);

	# plt.grid( ); 

	# plt.xlabel('X [m]');

	# plt.ylabel('Z [m]'); 

	# plt.savefig(figure_name_acc); 

	# plt.show(); 

### Plotting the displacement vector field in xy plane 

if (Z_xy_plane != None) and (XY_output == True) :

	z = int ( math.floor(( Z_xy_plane - ESSI_box_z_origin ) / ESSI_z_spacing )) ;

	ID_z = str(z); 

	if z <10: 
					
		ID_z= '0' + ID_z;

	if z >=100:
					
		print 'Too many stations, check if codes need modified!';


	vel_x = np.zeros((num_sampling_y, num_sampling_x, No_original_time_step)); 

	# print "array size: ", vel_x.shape   ## For debugging by Hexiang 
  
	vel_y = np.zeros((num_sampling_y, num_sampling_x, No_original_time_step));

	dis_x = np.zeros((num_sampling_y, num_sampling_x, No_original_time_step)); 

	dis_y = np.zeros((num_sampling_y, num_sampling_x, No_original_time_step));

	acc_x = np.zeros((num_sampling_y, num_sampling_x, No_original_time_step)); 

	acc_y = np.zeros((num_sampling_y, num_sampling_x, No_original_time_step));



	# sampled_vel_x = np.zeros((num_sampling_z, num_sampling_x, sampled_No_time_step));    ### we do not look at velocity

	# sampled_vel_z = np.zeros((num_sampling_z, num_sampling_x, sampled_No_time_step));

	sampled_dis_x = np.zeros((num_sampling_y, num_sampling_x, sampled_No_time_step)); 

	sampled_dis_y = np.zeros((num_sampling_y, num_sampling_x, sampled_No_time_step));

	sampled_acc_x = np.zeros((num_sampling_y, num_sampling_x, sampled_No_time_step)); 

	sampled_acc_y = np.zeros((num_sampling_y, num_sampling_x, sampled_No_time_step));


	for x1 in xrange(0,num_sampling_x):

		for x2 in xrange(0,num_sampling_y): 

			y= int ( math.floor(( - ESSI_box_y_origin -Y_xy_plane[x2,0] ) / ESSI_y_spacing )) ;

			ID_y = str(y);

			x= int ( math.floor(( X_xy_plane[0,x1] - ESSI_box_x_origin ) / ESSI_x_spacing )) ;

			ID_x = str(x);

			if x <10:
					
				ID_x= '0' + ID_x;
			
			if y <10:

				ID_y= '0' + ID_y;

			if x >=100: 
		
				print 'Too many stations, check if codes need modified!';

			if y >=100:
		
				print 'Too many stations, check if codes need modified!';


			filename = file_prefix + '_0' + ID_x + '_0' + ID_y + '_0' + ID_z;

			print "Current station name " , filename;  

			filename_x = motion_dir + filename + file_postfix_x ;

			filename_y = motion_dir + filename + file_postfix_y ; 

			sac_info_x = read(filename_x, debug_headers=True); 

			sac_info_y = read(filename_y, debug_headers=True); 
				
			vel_x[x2, x1, :] = sac_info_x[0].data; 

			vel_y[x2, x1, :] = sac_info_y[0].data * (-1.0);

			print "Getting velocity at x= ", X_xy_plane[x2, x1] , ', y= ', Y_xy_plane[x2, x1];  

			for x3 in xrange(1,No_original_time_step):
				
				dis_x[:, :, x3] = dis_x[:, :, x3-1] + vel_x[:,:,x3] * original_time_step; 

				dis_y[:, :, x3] = dis_y[:, :, x3-1] + vel_y[:,:,x3] * original_time_step;

				acc_x[:, :, x3] = (vel_x[:, :, x3] - vel_x[:, :, x3-1])/original_time_step ; 

				acc_y[:, :, x3] = (vel_y[:, :, x3] - vel_y[:, :, x3-1])/original_time_step ;  

			print 'Finish Transformation from velocity to displacement and acceleration'; 

			for x4 in xrange(0, sampled_No_time_step):

				sampled_dis_x[:, :, x4]=dis_x[:, :, x4*sampling_interval];
	
				sampled_acc_x[:, :, x4]=acc_x[:, :, x4*sampling_interval];

				sampled_dis_y[:, :, x4]=dis_y[:, :, x4*sampling_interval];

				sampled_acc_y[:, :, x4]=acc_y[:, :, x4*sampling_interval];

			print 'Finish sampling of displacement and acceleration'; 



	### Use for loop to generate a time seris of sectional vector field  

	directory_name_dis = './XY_plane_dis_z'+str(Z_xy_plane); 

	directory_name_acc = './XY_plane_acc_z'+str(Z_xy_plane); 

	if not os.path.exists(directory_name_dis):

		os.makedirs(directory_name_dis); 

	if not os.path.exists(directory_name_acc):

		os.makedirs(directory_name_acc); 

	for x5 in xrange(0,sampled_No_time_step):
	
	# for x5 in xrange(373,374):


		# figure_name_dis = './XY_plane_dis/DisXY_plane_z_'+ str(Z_xy_plane)+'_'+str(x5)+'.jpg';

		# figure_name_acc = './XY_plane_acc/AccXY_plane_z_'+ str(Z_xy_plane)+'_'+str(x5)+'.jpg';

		# figure_name_dis = './XY_plane_dis/'+str(x5)+'.jpg';

		# figure_name_acc = './XY_plane_acc/'+str(x5)+'.jpg';

		figure_name_dis = directory_name_dis+ '/'+str(x5)+'.jpg';

		figure_name_acc = directory_name_acc+'/'+str(x5)+'.jpg';

		fig= plt.figure()

		ax= fig.add_subplot(111); 

		# M = np.hypot(sampled_dis_x[:,:,x5], sampled_dis_y[:,:,x5]);

		print  'Printing x displacment\n', sampled_dis_x[:,:,x5], 'Printing y displacement\n', sampled_dis_y[:,:,x5];    ## For debugging by Hexiang

		print  'Printing x acceleration\n', sampled_acc_x[:,:,x5], 'Printing y acceleration\n', sampled_acc_y[:,:,x5];    ### For debugging by Hexiang

		Q = plt.quiver(X_xy_plane, Y_xy_plane, sampled_dis_x[:,:,x5], sampled_dis_y[:,:,x5], scale = 0.5)    # , units='x', pivot='tip', width=0.022, scale= 500); 

		qk = plt.quiverkey(Q, 0.9, 0.9, 0.1, r'$0.1 m$', labelpos='E', coordinates='figure')

		plt.scatter(X_xy_plane, Y_xy_plane, color = 'k', s=5);

		plt.grid( ); 

		plt.xlabel('X [m]');

		plt.ylabel('Y [m]'); 


		# plt.plot([3925, 4075], [-5925, -5925], 'r-', [4075, 4075], [-5925, -6075], 'r-', [4075, 3925], [-6075,-6075], 'r-',[3925,3925], [-6075, -5925], 'r-', [3985, 4015], [-5985, -5985], 'r-', [4015, 4015], [-5985, -6015], 'r-', [4015, 3985], [-6015,-6015], 'r-' , [3985, 3985], [-6015,-5985], '-r' , linewidth= 3)

		plt.savefig(figure_name_dis); 		 

		# plt.show(); 


		fig= plt.figure()

		ax= fig.add_subplot(111); 

		Q = plt.quiver(X_xy_plane, Y_xy_plane, sampled_acc_x[:,:,x5], sampled_acc_y[:,:,x5], scale = 7.0, units = 'inches')    # , units='x', pivot='tip', width=0.022, scale= 500); 

		qk = plt.quiverkey(Q, 0.9, 0.9, 10, r'$1 g$', labelpos='E', coordinates='figure')

		plt.scatter(X_xy_plane, Y_xy_plane, color = 'k', s=5);

		plt.grid( ); 

		plt.xlabel('X [m]');

		plt.ylabel('Y [m]'); 


		### plot the outline of SMR
		# plt.plot([3925, 4075], [-5925, -5925], 'r-', [4075, 4075], [-5925, -6075], 'r-', [4075, 3925], [-6075,-6075], 'r-',[3925,3925], [-6075, -5925], 'r-', [3985, 4015], [-5985, -5985], 'r-', [4015, 4015], [-5985, -6015], 'r-', [4015, 3985], [-6015,-6015], 'r-' , [3985, 3985], [-6015,-5985], '-r' , linewidth= 3)


		### save the figure
		plt.savefig(figure_name_acc); 

		# plt.show(); 


#### The following code is used to generate single time step sectional vector plot ###

	# x5 = 385 ;   ### ID of time step 

	# figure_name_dis = './XY_plane_dis/DisXY_plane_z_'+ str(Z_xy_plane)+'_'+str(x5)+'.jpg';

	# figure_name_acc = './XY_plane_acc/Acc_XY_plane_z_'+ str(Z_xy_plane)+'_'+str(x5)+'.jpg';

	# fig= plt.figure()

	# ax= fig.add_subplot(111); 

	# # M = np.hypot(sampled_dis_x[:,:,x5], sampled_dis_y[:,:,x5]);

	# # print  'Printing x displacment\n', sampled_dis_x[:,:,x5], 'Printing y displacement\n', sampled_dis_y[:,:,x5];    ## For debugging by Hexiang

	# # print  'Printing x acceleration\n', sampled_acc_x[:,:,x5], 'Printing y acceleration\n', sampled_acc_y[:,:,x5];    ### For debugging by Hexiang

	# Q = plt.quiver(X_xy_plane, Y_xy_plane, sampled_dis_x[:,:,x5], sampled_dis_y[:,:,x5])    # , units='x', pivot='tip', width=0.022, scale= 500); 

	# qk = plt.quiverkey(Q, 0.9, 0.9, 0.1, r'$0.1 m$', labelpos='E', coordinates='figure', scale = 1.0)

	# plt.scatter(X_xy_plane, Y_xy_plane, color = 'k', s=5);

	# plt.grid( ); 

	# plt.xlabel('X [m]');

	# plt.ylabel('Y [m]'); 

	# plt.plot([3925, 4075], [5925, 5925], 'r-', [4075, 4075], [5925, 6075], 'r-', [4075, 3925], [6075,6075], 'r-',[3925,3925], [6075, 5925], 'r-', [3985, 4015], [5985, 5985], 'r-', [4015, 4015], [5985, 6015], 'r-', [4015, 3985], [6015,6015], 'r-' , [3985, 3985], [6015,5985], '-r' , linewidth= 3)


	# plt.savefig(figure_name_dis); 		 

	# # plt.show(); 


	# fig= plt.figure()

	# ax= fig.add_subplot(111); 

	# Q = plt.quiver(X_xy_plane, Y_xy_plane, sampled_acc_x[:,:,x5], sampled_acc_y[:,:,x5], scale = 12.0, units = 'inches')    # , units='x', pivot='tip', width=0.022, scale= 500); 

	# qk = plt.quiverkey(Q, 0.9, 0.9, 10, r'$1 g$', labelpos='E', coordinates='figure')

	# plt.scatter(X_xy_plane, Y_xy_plane, color = 'k', s=5);

	# plt.grid( ); 

	# plt.xlabel('X [m]');

	# plt.ylabel('Y [m]'); 


	# ### plot the outline of SMR
	# plt.plot([3925, 4075], [5925, 5925], 'r-', [4075, 4075], [5925, 6075], 'r-', [4075, 3925], [6075,6075], 'r-',[3925,3925], [6075, 5925], 'r-', [3985, 4015], [5985, 5985], 'r-', [4015, 4015], [5985, 6015], 'r-', [4015, 3985], [6015,6015], 'r-' , [3985, 3985], [6015,5985], '-r' , linewidth= 3)

	# ### save the figure
	# plt.savefig(figure_name_acc); 

	# # plt.show(); 


### Plotting the displacement vector field in yz plane 

if ( X_yz_plane != None) and (YZ_output == True) :

	x = int ( math.floor(( X_yz_plane - ESSI_box_x_origin ) / ESSI_x_spacing )) ;

	ID_x = str(x); 

	if x <10: 
					
		ID_x= '0' + ID_x;

	if x >=100:
					
		print 'Too many stations, check if codes need modified!';


	vel_y = np.zeros((num_sampling_z, num_sampling_y, No_original_time_step)); 

	# print "array size: ", vel_x.shape   ## For debugging by Hexiang 
  
	vel_z = np.zeros((num_sampling_z, num_sampling_y, No_original_time_step));

	dis_y = np.zeros((num_sampling_z, num_sampling_y, No_original_time_step)); 

	dis_z = np.zeros((num_sampling_z, num_sampling_y, No_original_time_step));

	acc_y = np.zeros((num_sampling_z, num_sampling_y, No_original_time_step)); 

	acc_z = np.zeros((num_sampling_z, num_sampling_y, No_original_time_step));



	# sampled_vel_x = np.zeros((num_sampling_z, num_sampling_x, sampled_No_time_step));    ### we do not look at velocity

	# sampled_vel_z = np.zeros((num_sampling_z, num_sampling_x, sampled_No_time_step));

	sampled_dis_y = np.zeros((num_sampling_z, num_sampling_y, sampled_No_time_step)); 

	sampled_dis_z = np.zeros((num_sampling_z, num_sampling_y, sampled_No_time_step));

	sampled_acc_y = np.zeros((num_sampling_z, num_sampling_y, sampled_No_time_step)); 

	sampled_acc_z = np.zeros((num_sampling_z, num_sampling_y, sampled_No_time_step));


	for x1 in xrange(0,num_sampling_y):

		for x2 in xrange(0,num_sampling_z): 

			y= int ( math.floor(( - ESSI_box_y_origin -Y_yz_plane[0,x1] ) / ESSI_y_spacing )) ;

			ID_y = str(y);

			z= int ( math.floor(( - ESSI_box_z_origin -Z_yz_plane[x2,0] ) / ESSI_z_spacing )) ;

			ID_z = str(z);

			if y <10:
					
				ID_y= '0' + ID_y;
			
			if z <10:

				ID_z= '0' + ID_z;

			if y >=100: 
		
				print 'Too many stations, check if codes need modified!';

			if z >=100:
		
				print 'Too many stations, check if codes need modified!';


			filename = file_prefix + '_0' + ID_x + '_0' + ID_y + '_0' + ID_z;

			print "Current station name " , filename;  

			filename_y = motion_dir + filename + file_postfix_y ; 

			filename_z = motion_dir + filename + file_postfix_z ; 

			sac_info_y = read(filename_y, debug_headers=True); 

			sac_info_z = read(filename_z, debug_headers=True); 

			vel_y[x2, x1, :] = sac_info_y[0].data * (-1.0);

			vel_z[x2, x1, :] = sac_info_z[0].data * (-1.0);
		
			print "Getting velocity at y= ", Y_yz_plane[x2, x1] , ', z= ', Z_yz_plane[x2, x1];  

			for x3 in xrange(1,No_original_time_step):
				
				dis_y[:, :, x3] = dis_y[:, :, x3-1] + vel_y[:,:,x3] * original_time_step;
				
				dis_z[:, :, x3] = dis_z[:, :, x3-1] + vel_z[:,:,x3] * original_time_step; 

				acc_y[:, :, x3] = (vel_y[:, :, x3] - vel_y[:, :, x3-1])/original_time_step ; 

				acc_z[:, :, x3] = (vel_z[:, :, x3] - vel_z[:, :, x3-1])/original_time_step ;  

			print 'Finish Transformation from velocity to displacement and acceleration'; 

			for x4 in xrange(0, sampled_No_time_step):

				sampled_dis_y[:, :, x4]=dis_y[:, :, x4*sampling_interval];
	
				sampled_acc_y[:, :, x4]=acc_y[:, :, x4*sampling_interval];

				sampled_dis_z[:, :, x4]=dis_z[:, :, x4*sampling_interval];

				sampled_acc_z[:, :, x4]=acc_z[:, :, x4*sampling_interval];

			print 'Finish sampling of displacement and acceleration'; 


	### Use for loop to generate a time seris of sectional vector field  

	directory_name_dis = './YZ_plane_dis_x'+str(X_yz_plane); 

	directory_name_acc = './YZ_plane_acc_x'+str(X_yz_plane); 

	if not os.path.exists(directory_name_dis):

		os.makedirs(directory_name_dis); 

	if not os.path.exists(directory_name_acc):

		os.makedirs(directory_name_acc); 

	for x5 in xrange(0,sampled_No_time_step):
	
	# for x5 in xrange(373,374):


		# figure_name_dis = './YZ_plane_dis/DisYZ_plane_x_'+ str(X_yz_plane)+'_'+str(x5)+'.jpg';

		# figure_name_acc = './YZ_plane_acc/AccYZ_plane_x_'+ str(X_yz_plane)+'_'+str(x5)+'.jpg';

		# figure_name_dis = './YZ_plane_dis/'+str(x5)+'.jpg';

		# figure_name_acc = './YZ_plane_acc/'+str(x5)+'.jpg';

		figure_name_dis = directory_name_dis+ '/'+str(x5)+'.jpg';

		figure_name_acc = directory_name_acc+'/'+str(x5)+'.jpg';

		fig= plt.figure()

		ax= fig.add_subplot(111); 

		# M = np.hypot(sampled_dis_x[:,:,x5], sampled_dis_y[:,:,x5]);

		print  'Printing y displacment\n', sampled_dis_y[:,:,x5], 'Printing z displacement\n', sampled_dis_z[:,:,x5];    ## For debugging by Hexiang

		print  'Printing y acceleration\n', sampled_acc_y[:,:,x5], 'Printing z acceleration\n', sampled_acc_z[:,:,x5];    ### For debugging by Hexiang

		Q = plt.quiver(Y_yz_plane, Z_yz_plane, sampled_dis_y[:,:,x5], sampled_dis_z[:,:,x5], scale = 0.5)    # , units='x', pivot='tip', width=0.022, scale= 500); 

		qk = plt.quiverkey(Q, 0.9, 0.9, 0.1, r'$0.1 m$', labelpos='E', coordinates='figure')

		plt.scatter(Y_yz_plane, Z_yz_plane, color = 'k', s=5);

		plt.grid( ); 

		plt.xlabel('Y [m]');

		plt.ylabel('Z [m]'); 

		# plt.plot([-5925, -5925], [0, -66], 'r-', [-5925, -6075], [-66, -66], 'r-', [-6075, -6075], [-66,0], 'r-',[-6075,-6015], [0, 0], 'r-', [-6015, -6015], [0, 15], 'r-', [-6015, -5985], [15, 15], 'r-', [-5985, -5985], [15,0], 'r-' , [-5985, -5925], [0,0], '-r' , linewidth= 3)

		plt.savefig(figure_name_dis); 		 

		# plt.show(); 


		fig= plt.figure()

		ax= fig.add_subplot(111); 

		Q = plt.quiver(Y_yz_plane, Z_yz_plane, sampled_acc_y[:,:,x5], sampled_acc_z[:,:,x5], scale = 7.0, units = 'inches')    # , units='x', pivot='tip', width=0.022, scale= 500); 

		qk = plt.quiverkey(Q, 0.9, 0.9, 10, r'$1 g$', labelpos='E', coordinates='figure')

		plt.scatter(Y_yz_plane, Z_yz_plane, color = 'k', s=5);

		plt.grid( ); 

		plt.xlabel('Y [m]');

		plt.ylabel('Z [m]'); 


		### plot the outline of SMR
		# plt.plot([-5925, -5925], [0, -66], 'r-', [-5925, -6075], [-66, -66], 'r-', [-6075, -6075], [-66,0], 'r-',[-6075,-6015], [0, 0], 'r-', [-6015, -6015], [0, 15], 'r-', [-6015, -5985], [15, 15], 'r-', [-5985, -5985], [15,0], 'r-' , [-5985, -5925], [0,0], '-r' , linewidth= 3)

		### save the figure
		plt.savefig(figure_name_acc); 

		# plt.show(); 




	# x5 = 375; 

	# figure_name_dis = './YZ_plane_dis/DisYZ_plane_x_'+ str(X_yz_plane)+'_'+str(x5)+'.jpg';

	# figure_name_acc = './YZ_plane_acc/AccYZ_plane_x_'+ str(X_yz_plane)+'_'+str(x5)+'.jpg';

	# fig= plt.figure()

	# ax= fig.add_subplot(111); 

	# # M = np.hypot(sampled_dis_x[:,:,x5], sampled_dis_y[:,:,x5]);

	# print  'Printing y displacment\n', sampled_dis_y[:,:,x5], 'Printing z displacement\n', sampled_dis_z[:,:,x5];    ## For debugging by Hexiang

	# print  'Printing y acceleration\n', sampled_acc_y[:,:,x5], 'Printing z acceleration\n', sampled_acc_z[:,:,x5];    ### For debugging by Hexiang

	# Q = plt.quiver(Y_yz_plane, Z_yz_plane, sampled_dis_y[:,:,x5], sampled_dis_z[:,:,x5], scale = 1.0)    # , units='x', pivot='tip', width=0.022, scale= 500); 

	# qk = plt.quiverkey(Q, 0.9, 0.9, 0.1, r'$0.1 m$', labelpos='E', coordinates='figure')

	# plt.scatter(Y_yz_plane, Z_yz_plane, color = 'k', s=5);

	# plt.grid( ); 

	# plt.xlabel('Y [m]');

	# plt.ylabel('Z [m]'); 

	# plt.plot([-5925, -5925], [0, -66], 'r-', [-5925, -6075], [-66, -66], 'r-', [-6075, -6075], [-66,0], 'r-',[-6075,-6015], [0, 0], 'r-', [-6015, -6015], [0, 15], 'r-', [-6015, -5985], [15, 15], 'r-', [-5985, -5985], [15,0], 'r-' , [-5985, -5925], [0,0], '-r' , linewidth= 3)

	# plt.savefig(figure_name_dis); 		 

	# # plt.show(); 


	# fig= plt.figure()

	# ax= fig.add_subplot(111); 

	# Q = plt.quiver(Y_yz_plane, Z_yz_plane, sampled_acc_y[:,:,x5], sampled_acc_z[:,:,x5], scale = 12.0, units = 'inches')    # , units='x', pivot='tip', width=0.022, scale= 500); 

	# qk = plt.quiverkey(Q, 0.9, 0.9, 10, r'$1 g$', labelpos='E', coordinates='figure')

	# plt.scatter(Y_yz_plane, Z_yz_plane, color = 'k', s=5);

	# plt.grid( ); 

	# plt.xlabel('Y [m]');

	# plt.ylabel('Z [m]'); 


	# ### plot the outline of SMR
	# plt.plot([-5925, -5925], [0, -66], 'r-', [-5925, -6075], [-66, -66], 'r-', [-6075, -6075], [-66,0], 'r-',[-6075,-6015], [0, 0], 'r-', [-6015, -6015], [0, 15], 'r-', [-6015, -5985], [15, 15], 'r-', [-5985, -5985], [15,0], 'r-' , [-5985, -5925], [0,0], '-r' , linewidth= 3)

	# ### save the figure
	# plt.savefig(figure_name_acc); 

	# # plt.show(); 




# ## Plotting the displacement vector field in 3D space [Still need to work on: error is too many arguments to unpack] #####


# if (X_yz_plane != None) and (Y_xz_plane != None) and (Z_yz_plane != None) and (cubic_output == True):

	
# 	vel_x = np.zeros((num_sampling_y, num_sampling_x, num_sampling_z, No_original_time_step));   ### First index is Y, second index is X , third index is z 

# 	vel_y = np.zeros((num_sampling_y, num_sampling_x, num_sampling_z, No_original_time_step));       ###  First index is Y, second index is X , third index is z

# 	# print "array size: ", vel_x.shape   ## For debugging by Hexiang 
  
# 	vel_z = np.zeros((num_sampling_y, num_sampling_x, num_sampling_z, No_original_time_step));

# 	dis_x = np.zeros((num_sampling_y, num_sampling_x, num_sampling_z, No_original_time_step)); 

# 	dis_y = np.zeros((num_sampling_y, num_sampling_x, num_sampling_z, No_original_time_step)); 

# 	dis_z = np.zeros((num_sampling_y, num_sampling_x, num_sampling_z, No_original_time_step));

# 	acc_x = np.zeros((num_sampling_y, num_sampling_x, num_sampling_z, No_original_time_step)); 

# 	acc_y = np.zeros((num_sampling_y, num_sampling_x, num_sampling_z, No_original_time_step)); 

# 	acc_z = np.zeros((num_sampling_y, num_sampling_x, num_sampling_z, No_original_time_step));



# 	# sampled_vel_x = np.zeros((num_sampling_z, num_sampling_x, sampled_No_time_step));    ### we do not look at velocity

# 	# sampled_vel_z = np.zeros((num_sampling_z, num_sampling_x, sampled_No_time_step));

# 	sampled_dis_x = np.zeros((num_sampling_y, num_sampling_x, num_sampling_z, sampled_No_time_step)); 

# 	sampled_dis_y = np.zeros((num_sampling_y, num_sampling_x, num_sampling_z, sampled_No_time_step)); 

# 	sampled_dis_z = np.zeros((num_sampling_y, num_sampling_x, num_sampling_z, sampled_No_time_step));


# 	sampled_acc_x = np.zeros((num_sampling_y, num_sampling_x, num_sampling_z, sampled_No_time_step)); 

# 	sampled_acc_y = np.zeros((num_sampling_y, num_sampling_x, num_sampling_z, sampled_No_time_step)); 

# 	sampled_acc_z = np.zeros((num_sampling_y, num_sampling_x, num_sampling_z, sampled_No_time_step));


# 	for x1 in xrange(0,num_sampling_y):

# 		for x2 in xrange(0,num_sampling_x):

# 			for x3 in xrange(0,num_sampling_z):
			
# 				x = int ( math.floor(( X[x1,x2,x3] - ESSI_box_x_origin ) / ESSI_x_spacing )) ;

# 				ID_x = str(x); 

# 				if x <10: 
						
# 					ID_x= '0' + ID_x;

# 				if x >=100:
						
# 					print 'Too many stations, check if codes need modified!';
			
# 				y= int ( math.floor(( - ESSI_box_y_origin - Y[x1,x2,x3]) / ESSI_y_spacing )) ;

# 				ID_y = str(y);

# 				z= int ( math.floor(( - ESSI_box_z_origin -Z[x1,x2,x3]) / ESSI_z_spacing )) ;

# 				ID_z = str(z);

# 				if y <10:
						
# 					ID_y= '0' + ID_y;
				
# 				if z <10:

# 					ID_z= '0' + ID_z;

# 				if y >=100: 
			
# 					print 'Too many stations, check if codes need modified!';

# 				if z >=100:
			
# 					print 'Too many stations, check if codes need modified!';


# 				filename = file_prefix + '_0' + ID_x + '_0' + ID_y + '_0' + ID_z;

# 				print "Current station name " , filename;  

# 				filename_x = motion_dir + filename + file_postfix_x ; 

# 				filename_y = motion_dir + filename + file_postfix_y ; 

# 				filename_z = motion_dir + filename + file_postfix_z ; 

# 				sac_info_x = read(filename_x, debug_headers=True); 

# 				sac_info_y = read(filename_y, debug_headers=True); 

# 				sac_info_z = read(filename_z, debug_headers=True); 


# 				vel_x[x1, x2, x3, :] = sac_info_x[0].data;

# 				vel_y[x1, x2, x3, :] = sac_info_y[0].data * (-1.0);

# 				vel_z[x1, x2, x3, :] = sac_info_z[0].data * (-1.0);
			
# 				print "Getting velocity at x= ", X[x1, x2, x3] , ', y= ', Y[x1, x2, x3], ', z= ', Z[x1, x2, x3];  

# 				for x3 in xrange(1,No_original_time_step):

# 					dis_x[:, :, :, x3] = dis_x[:, :, :, x3-1] + vel_x[:, :, :, x3] * original_time_step;
					
# 					dis_y[:, :, :, x3] = dis_y[:, :, :, x3-1] + vel_y[:, :, :, x3] * original_time_step;
					
# 					dis_z[:, :, :, x3] = dis_z[:, :, :, x3-1] + vel_z[:, :, :, x3] * original_time_step; 

# 					acc_x[:, :, :, x3] = (vel_x[:, :, :, x3] - vel_x[:, :, :, x3-1])/original_time_step ; 

# 					acc_y[:, :, :, x3] = (vel_y[:, :, :, x3] - vel_y[:, :, :, x3-1])/original_time_step ; 

# 					acc_z[:, :, :, x3] = (vel_z[:, :, :, x3] - vel_z[:, :, :, x3-1])/original_time_step ;  

# 				print 'Finish Transformation from velocity to displacement and acceleration'; 

# 				for x4 in xrange(0, sampled_No_time_step):

# 					sampled_dis_x[:, :, :, x4]=dis_x[:, :, :, x4*sampling_interval];	

# 					sampled_acc_x[:, :, :, x4]=dis_x[:, :, :, x4*sampling_interval];	

# 					sampled_dis_y[:, :, :, x4]=dis_y[:, :, :, x4*sampling_interval];
		
# 					sampled_acc_y[:, :, :, x4]=acc_y[:, :, :, x4*sampling_interval];

# 					sampled_dis_z[:, :, :, x4]=dis_z[:, :, :, x4*sampling_interval];

# 					sampled_acc_z[:, :, :, x4]=acc_z[:, :, :, x4*sampling_interval];

# 				print 'Finish sampling of displacement and acceleration'; 


# 	### Use for loop to generate a time seris of sectional vector field  

# 	# for x5 in xrange(0,sampled_No_time_step):
	
# 	for x5 in xrange(373,374):


# 		figure_name_dis = './3D_dis/3D_dis'+'_'+str(x5)+'.jpg';

# 		figure_name_acc = './3D_acc/3D_acc'+'_'+str(x5)+'.jpg';

# 		fig= plt.figure()

# 		ax= fig.add_subplot(111, projection='3d'); 

# 		# M = np.hypot(sampled_dis_x[:,:,x5], sampled_dis_y[:,:,x5]);

# 		# print  'Printing y displacment\n', sampled_dis_y[:,:,x5], 'Printing z displacement\n', sampled_dis_z[:,:,x5];    ## For debugging by Hexiang

# 		# print  'Printing y acceleration\n', sampled_acc_y[:,:,x5], 'Printing z acceleration\n', sampled_acc_z[:,:,x5];    ### For debugging by Hexiang

# 		Q = plt.quiver(X, Y, Z, sampled_dis_x[:,:,:,x5], sampled_dis_y[:, :, :, x5], sampled_dis_z[:, :, :, x5])     ## length = 1.0)    # , units='x', pivot='tip', width=0.022, scale= 500); 

# 		# qk = plt.quiverkey(Q, 0.9, 0.9, 0.1, r'$0.1 m$', labelpos='E', coordinates='figure')

# 		# plt.scatter(X, Y, Z, color = 'k', s=5);

# 		plt.scatter(X, Y, Z, color = 'k');

# 		plt.grid( ); 


# 		ax.set_xlabel('X [m]');

# 		ax.set_ylabel('Y [m]'); 

# 		ax.set_zlabel('Z [m]');	 

# 		# plt.plot([-5925, -5925], [0, -66], 'r-', [-5925, -6075], [-66, -66], 'r-', [-6075, -6075], [-66,0], 'r-',[-6075,-6015], [0, 0], 'r-', [-6015, -6015], [0, 15], 'r-', [-6015, -5985], [15, 15], 'r-', [-5985, -5985], [15,0], 'r-' , [-5985, -5925], [0,0], '-r' , linewidth= 3)

# 		plt.savefig(figure_name_dis); 		 

# 		# plt.show(); 


# 		fig= plt.figure()

# 		ax= fig.add_subplot(111); 

# 		Q = plt.quiver(X, Y, Z, sampled_acc_x[:, :, :, x5], sampled_acc_y[:, :, :, x5], sampled_acc_z[:, :, :, x5], length = 1.0)      ### scale = 12.0, units = 'inches')    # , units='x', pivot='tip', width=0.022, scale= 500); 

# 		# qk = plt.quiverkey(Q, 0.9, 0.9, 10, r'$1 g$', labelpos='E', coordinates='figure')

# 		plt.scatter(X, Y, Z, color = 'k');

# 		plt.grid( ); 


# 		ax.set_xlabel('X [m]');

# 		ax.set_ylabel('Y [m]'); 

# 		ax.set_zlabel('Z [m]'); 


# 		### plot the outline of SMR
# 		# plt.plot([-5925, -5925], [0, -66], 'r-', [-5925, -6075], [-66, -66], 'r-', [-6075, -6075], [-66,0], 'r-',[-6075,-6015], [0, 0], 'r-', [-6015, -6015], [0, 15], 'r-', [-6015, -5985], [15, 15], 'r-', [-5985, -5985], [15,0], 'r-' , [-5985, -5925], [0,0], '-r' , linewidth= 3)

# 		### save the figure
# 		plt.savefig(figure_name_acc); 

# 		# plt.show(); 
