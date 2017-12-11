#!/bin/bash

# clean previous results
rm -f *.feioutput
rm -f essi*.log

# run essi simulation
essi -f main.fei

# postprocessing: plot results
python plot.py Numerical_Damping_Loading.h5.feioutput

