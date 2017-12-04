#!/bin/bash

## delete old DRMinput file

rm -rf *.hdf5

rm -rf *.feioutput

## Generate DRM input  
gmessy solid_structure_DRM3D.gmessi

rm -rf ./solid_structure_DRM3D_fei

echo "<========== Finish writing DRM inut files ==============>"


## run SW42ESSI
python SW42ESSI.py SW42ESSI_meta_info.txt

echo "<========== Finish transition from SW4 to RealESSI ==============>"

## run RealESSI

mpirun -np 10 essi_parallel -f main.fei




