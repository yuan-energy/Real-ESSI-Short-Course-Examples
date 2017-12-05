#!/bin/bash

## delete old DRMinput file

rm -rf *.hdf5

rm -rf *.feioutput

## Generate DRM input  
gmessy_boris simplified.gmessi

mv ./simplified_fei/element.fei  ./element.fei

mv ./simplified_fei/node.fei     ./node.fei

mv ./simplified_fei/load.fei     ./load.fei

rm -rf ./simplified_fei

echo "<========== Finish writing DRM inut files ==============>"


## run SW42ESSI
python SW42ESSI.py SW42ESSI_meta_info.txt

echo "<========== Finish transition from SW4 to RealESSI ==============>"

## run RealESSI

mpirun -np 10 pessi_sumeet -f main.fei




