
# clean previous meshing
rm -rf DRM3D_fei

# Run gmsh to generate the mesh files
gmsh -3 DRM3D.geo


# Run gmessy to translate the mesh files to ESSI input
gmessy DRM3D.gmessi


# Copy the ESSI input files to current working directories
cp DRM3D_fei/node.fei .
cp DRM3D_fei/element.fei .
cp DRM3D_fei/load.fei .


