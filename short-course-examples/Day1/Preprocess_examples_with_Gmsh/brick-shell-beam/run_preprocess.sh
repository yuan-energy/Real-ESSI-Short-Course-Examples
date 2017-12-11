
# clean previous meshing
rm -rf Example_5_ESSI_Simulation

# Run gmsh to generate the mesh files
gmsh -3 Example_5.geo


# Run gmessy to translate the mesh files to ESSI input
gmessy Example_5.gmessi


# Copy the ESSI input files to current working directories
cp Example_5_ESSI_Simulation/node.fei .
cp Example_5_ESSI_Simulation/element.fei .
cp Example_5_ESSI_Simulation/load.fei .


