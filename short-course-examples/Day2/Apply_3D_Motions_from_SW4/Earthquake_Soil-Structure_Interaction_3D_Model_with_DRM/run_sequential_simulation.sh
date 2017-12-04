#!/bin/bash

if [ -f $PWD/DRMinput_Solid.hdf5 ]
    then
        :
else
	wget http://cml08.engr.ucdavis.edu/for_yuan/short_course/DRMinput_Solid.hdf5
fi

script -c "time essi_sumeet -f main.fei" log_sequential.txt
