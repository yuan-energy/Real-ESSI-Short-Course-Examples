#!/bin/bash

# clean previous results
rm -f *.feioutput
rm -f essi*.log

# run essi simulation
essi -f main.fei

# Run Paraview
paraview brick_5element_eigen.h5.feioutput