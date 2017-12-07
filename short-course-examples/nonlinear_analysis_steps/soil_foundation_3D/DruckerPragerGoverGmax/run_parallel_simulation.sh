#!/bin/bash
script -c "time mpirun -np $(nproc) essi_parallel -f main.fei" benchmark.txt

