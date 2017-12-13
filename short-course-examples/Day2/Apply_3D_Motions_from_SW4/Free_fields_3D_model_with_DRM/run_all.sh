#!/bin/bash

## delete old DRMinput file

rm -rf *.hdf5

rm -rf *.feioutput

## Generate DRM input  
gmessy simplified.gmessi

mv ./simplified_fei/element.fei  ./element.fei

mv ./simplified_fei/node.fei     ./node.fei

mv ./simplified_fei/load.fei     ./load.fei

rm -rf ./simplified_fei

echo "<========== Finish writing DRM inut files ==============>"


## run SW4 

cd SW4_motion

./run_SW4.sh

echo "<========== Finish generating 3D motion ==============>"


## run SW42ESSI

cd ..

python SW42ESSI.py SW42ESSI_meta_info.txt


echo "<========== Finish transition from SW4 to RealESSI ==============>"

## run RealESSI

mpirun -np $(nproc) essi_parallel -f main.fei