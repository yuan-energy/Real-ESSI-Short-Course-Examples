gmsh -3 shell_structure_DRM3D.geo
rm -rf shell_structure_DRM3D_fei

gmessy shell_structure_DRM3D.gmessi

cp shell_structure_DRM3D_fei/load.fei .
cp shell_structure_DRM3D_fei/element.fei .
cp shell_structure_DRM3D_fei/node.fei .


mpirun -np 8 essi_parallel -f main.fei

