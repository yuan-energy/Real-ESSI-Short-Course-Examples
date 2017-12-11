#!/bin/bash

# clean previous results
rm -f *.feioutput
rm -f essi*.log

# run essi simulation
essi -f main.fei

# postprocessing: plot results
python plot.py von_Mises_Loading.h5.feioutput

