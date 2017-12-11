
# clean previous meshing
rm -rf Example_2_ESSI_Simulation

# Run gmsh to generate the mesh files
gmsh -3 Example_2.geo


# Run gmessy to translate the mesh files to ESSI input
gmessy Example_2.gmessi


# Copy the ESSI input files to current working directories
cp Example_2_ESSI_Simulation/node.fei .
cp Example_2_ESSI_Simulation/element.fei .
cp Example_2_ESSI_Simulation/load.fei .


