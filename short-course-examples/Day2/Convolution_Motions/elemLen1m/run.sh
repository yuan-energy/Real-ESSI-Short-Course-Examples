gmsh -3 column.geo
rm -rf column_fei
gmessy column.gmessi


cp column_fei/node.fei .
cp column_fei/element.fei .
cp column_fei/load.fei .

essi -f main.fei 

python extract_wave.py test_motion.h5.feioutput
# python extract_node_acce.py test_motion.h5.feioutput 5 x 
# python extract_node_disp.py test_motion.h5.feioutput 5 x 

python plot_freq.py top_acc.txt


