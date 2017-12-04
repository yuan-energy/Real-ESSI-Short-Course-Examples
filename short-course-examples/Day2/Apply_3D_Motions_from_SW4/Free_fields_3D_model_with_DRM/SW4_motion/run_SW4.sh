#!/bin/bash

### clean previous result 

rm -rf 3D_motion 

rm -rf *.pdf

## Run sw4 to calculate 3D motion
mpirun -np 4 sw4 3D_motion.in


## show result of 3D motion 

# python sac_reader.py

