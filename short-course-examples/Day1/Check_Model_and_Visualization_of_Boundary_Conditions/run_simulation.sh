#!/bin/bash

rm -rf Example_1_ESSI_Simulation
echo "Generating the Mesh ..."
gmessy Example_1.gmessi
cp Example_1_ESSI_Simulation/element.fei . 
cp Example_1_ESSI_Simulation/load.fei . 
cp Example_1_ESSI_Simulation/node.fei . 
echo "Done! "


echo "Starting essi simulation ..."
essi -f main.fei
echo "Done! "


