#!/bin/bash

# Download the 3D motions for this model.
if [ -f M5.5_ESSI_Earthquake.drminput ]; then
	:
else 
	wget http://cml01.engr.ucdavis.edu/forShortCourse/M5.5_ESSI_Earthquake.drminput
fi

# Execute parallel essi with the file main.fei
mpirun -np $(nproc) essi_parallel -f main.fei

# If one wants to measure the time and save the terminal logs.
# script -c "time mpirun -np $(nproc) essi_parallel -f main.fei" terminal.log
