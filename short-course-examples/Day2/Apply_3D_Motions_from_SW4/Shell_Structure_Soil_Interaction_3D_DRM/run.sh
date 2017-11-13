#!/bin/bash
if [ -f $PWD/DRM3Dmotion_fromSW4.hdf5 ]
    then
        :
else
	wget http://cml01.engr.ucdavis.edu/forShortCourse/DRM3Dmotion_fromSW4.hdf5
fi


mpirun -np 8 essi_parallel -f main.fei
