#!/bin/bash

# Execute parallel essi with the file main.fei
mpirun -np $(nproc) essi_parallel -f main.fei

# If one wants to measure the time and save the terminal logs.
# script -c "time mpirun -np $(nproc) essi_parallel -f main.fei" terminal.log
