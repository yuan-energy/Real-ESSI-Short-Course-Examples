#!/bin/bash

## delete old DRMinput file

rm -rf *.hdf5

rm -rf *.feioutput

## Generate DRM input  
gmessy shell_structure_DRM3D.gmessi

rm -rf ./shell_structure_DRM3D_fei

echo "<========== Finish writing DRM inut files ==============>"


## run SW42ESSI
python SW42ESSI.py SW42ESSI_meta_info.txt

echo "<========== Finish transition from SW4 to RealESSI ==============>"

