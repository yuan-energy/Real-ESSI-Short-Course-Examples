rm -rf shell_structure_DRM3D_fei

gmessy shell_structure_DRM3D.gmessi

cp shell_structure_DRM3D/load.fei
cp shell_structure_DRM3D/element.fei
cp shell_structure_DRM3D/node.fei


mpirun -np 4 essi_parallel -f main.fei

