import h5py
import sys
filename = sys.argv[1]
h5file = h5py.File(filename,"a")
del h5file["Accelerations"]
del h5file["Displacements"]
del h5file["Time"]

