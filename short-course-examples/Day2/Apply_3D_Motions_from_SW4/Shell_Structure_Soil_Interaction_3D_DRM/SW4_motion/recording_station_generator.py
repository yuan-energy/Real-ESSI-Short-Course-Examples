# -*- coding: utf-8 -*-
# @Author: hexiang
# @Date:   2017-10-29 23:16:24
# @Last Modified by:   hexiang6666
# @Last Modified time: 2017-11-29 17:27:47

### The function generates all recording commands in SW4 to track all ESSI box stations response.   

#! /usr/bin/env python

import scipy as sp
import math

### input arguments: 
# 					origin_x: x coordinate of ESSI box origin (least number in x direction)
#					origin_y: y coordinate of ESSI box origin (least number in y direction)
#					origin_z: z coordinate of ESSI box origin (least number in z direction)
#					box_length: the length of ESSI box (corresponding to x direction)
#					box_width: the width of ESSI box (corresponding to y direction)
#					box_height: the height of ESSI box (corresponding to z direction)
#					station_spacing: nodal spacing of ESSI box  

def recording_station_generator(origin_x, origin_y, origin_z, box_length, box_width, box_height, station_spacing_x, station_spacing_y, station_spacing_z, sw4_input):

	No_station_x= int(math.ceil(box_length/station_spacing_x))+1;

	No_station_y= int(math.ceil(box_width/station_spacing_y))+1;

	No_station_z= int(math.ceil(box_height/station_spacing_z))+1;

	with open(sw4_input,'a') as myfile:

		myfile.write('\n### Recording motion at following ESSI box stations stations ###\n');

		for x1 in xrange(0,No_station_x):
		
			for x2 in xrange(0,No_station_y):
		
				for x3 in xrange(0,No_station_z):
		
					ID_x= str(x1);
				
					ID_y= str(x2);

					ID_z= str(x3);

					if x1<10:
				
						ID_x='0'+ID_x;
				
					if x1>=100:
				
						print 'Codes need to be modified, currently the number of stations in each direction must be less than 100\n';
				
					ID_x = '0'+ID_x;

					if x2<10:	

						ID_y='0'+ID_y;

					if x2>=100:
				
						print 'Codes need to be modified, currently the number of stations in each direction must be less than 100\n';
				
					ID_y = '0'+ID_y;

					if x3<10:
					
						ID_z= '0'+ID_z; 

					if x3>=100:
				
						print 'Codes need to be modified, currently the number of stations in each direction must be less than 100\n';
				
					ID_z = '0'+ID_z;

					station_name= "E_"+ ID_x + "_" + ID_y + "_" + ID_z; 

					myfile.write('rec x=' + str(origin_x+station_spacing_x*x1) +' y='+str(origin_y+station_spacing_y*x2)+' depth='+str(origin_z+station_spacing_z*x3)+' sta='+station_name+' file='+station_name+'\n')




				
##################### Define usr input ##################################

Origin_x = 2100;

Origin_y = 2300;

Origin_z = 0;

Box_length = 300;

Box_width = 300; 

Box_height = 100; 

Station_spacing_x = 10;

Station_spacing_y = 10; 

Station_spacing_z = 10;

Sw4_input_file = '3D_motion.in'; 


recording_station_generator(Origin_x, Origin_y, Origin_z, Box_length, Box_width, Box_height, Station_spacing_x, Station_spacing_y, Station_spacing_z, Sw4_input_file); 