#!/bin/bash

# Using gmsh in 3D to execute geometry-file (*.geo) to generate mesh-file (*.msh).
gmsh -3 soil_foundation_DRM3D.geo

# Using gmessy to execute translation-file (*.gmessi) to generate fei-input-files (*.fei).
#   (Notes: using specified *.msh files as the input)
gmessy soil_foundation_DRM3D.gmessi

# Copy the mesh-files to the essi analysis folder. 
cp -f ./soil_foundation_DRM3D_fei/element.fei ../
cp -f ./soil_foundation_DRM3D_fei/load.fei ../
cp -f ./soil_foundation_DRM3D_fei/node.fei ../


