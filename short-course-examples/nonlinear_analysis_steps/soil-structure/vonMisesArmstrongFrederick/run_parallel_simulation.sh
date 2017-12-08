#!/bin/bash


# Execute parallel essi with the file main.fei

# Meanwhile, measure the time and script the terminal logs.

script -c "time mpirun -np $(nproc) essi_parallel -f main.fei" benchmark.txt

