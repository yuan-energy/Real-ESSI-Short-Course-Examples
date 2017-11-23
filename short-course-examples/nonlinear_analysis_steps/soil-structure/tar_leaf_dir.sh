#!/bin/bash
# ********************************************************************
# Author: Yuan Feng
# Date: Sun Sep 24 12:00:55 PDT 2017
# Comments: 
# 	1. This script will compress the complete files in each example
# 	   to one compressed tgz file in each example subfolder, 
#      such that we will have a downloadable link for each example. 
#   2. The downloadable link is then used in example documentation in
#      Lecture_notes or other documentation.
# ********************************************************************


current_dir=${PWD}
deepest_dir_array=( $(find . -type d -links 2 ) )

for element in $(seq 0 $((${#deepest_dir_array[@]} - 1)))
do
	cd ${current_dir}
	
	# cp run_sequential_simulation.sh ${current_dir}/"${deepest_dir_array[$element]}"
	# cp run_parallel_simulation.sh ${current_dir}/"${deepest_dir_array[$element]}"
	cp run_plot_results.sh ${current_dir}/"${deepest_dir_array[$element]}"
	# cp extract_node_acce.py ${current_dir}/"${deepest_dir_array[$element]}"
	# cp extract_node_disp.py ${current_dir}/"${deepest_dir_array[$element]}"
	# cp extract_node_spectrum.py ${current_dir}/"${deepest_dir_array[$element]}"
	cp README.md ${current_dir}/"${deepest_dir_array[$element]}"
	# cp README.html ${current_dir}/"${deepest_dir_array[$element]}"
	# cp geometry_slice.png ${current_dir}/"${deepest_dir_array[$element]}"


	cd ${current_dir}/"${deepest_dir_array[$element]}"
	echo $PWD
	rm -f *.tgz
	tar -czvf ${PWD##*/}.tgz *
done