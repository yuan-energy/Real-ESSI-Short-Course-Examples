#!/bin/bash

if [ -f $PWD/free_field_DRMinput.hdf5 ]
    then
        :
else
	wget http://cml08.engr.ucdavis.edu/for_yuan/short_course/free_field_DRMinput.hdf5
fi

script -c "time mpirun -np $(nproc) essi_parallel -f main.fei" terminal.log


