
# clean previous meshing
rm -rf DRM2D_fei
rm -f node.fei
rm -f element.fei
rm -f load.fei

# Run gmsh to generate the mesh files
gmsh -3 DRM2D.geo


# Run gmessy to translate the mesh files to ESSI input
gmessy DRM2D.gmessi


# Copy the ESSI input files to current working directories
cp DRM2D_fei/node.fei .
cp DRM2D_fei/element.fei .
cp DRM2D_fei/load.fei .


