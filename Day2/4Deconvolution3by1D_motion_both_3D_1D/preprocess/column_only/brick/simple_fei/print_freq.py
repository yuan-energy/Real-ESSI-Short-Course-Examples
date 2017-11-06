import h5py
import numpy as np 
import sys

filename = sys.argv[1]
# filename = "column_eigen.h5.feioutput"

file = h5py.File(filename, 'r')
data = file['/Eigen_Mode_Analysis/Eigen_Frequencies/'][()]

print data 

