gmsh -3 simple.geo

rm -rf simple_fei
gmessy simple.gmessi

cp main.fei simple_fei
cp print_freq.py simple_fei
cd simple_fei
essi -f main.fei
python print_freq.py column_eigen.h5.feioutput

cd .. 
