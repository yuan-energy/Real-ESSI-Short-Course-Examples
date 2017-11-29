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
	cp extract_node_spectrum*.py ${current_dir}/"${deepest_dir_array[$element]}"
	# cp README.md ${current_dir}/"${deepest_dir_array[$element]}"
	# cp README.html ${current_dir}/"${deepest_dir_array[$element]}"
	# cp geometry_slice.png ${current_dir}/"${deepest_dir_array[$element]}"
	# cp sw4_free_field_center*.txt ${current_dir}/"${deepest_dir_array[$element]}"
	# cp base_correct_*.txt ${current_dir}/"${deepest_dir_array[$element]}"

	# cp compare_top_acc.py ${current_dir}/"${deepest_dir_array[$element]}"
	# cp run_plot_compare.sh ${current_dir}/"${deepest_dir_array[$element]}"

	cd ${current_dir}/"${deepest_dir_array[$element]}"
	# sed -i 's/acceleration_filename\ =\ \"scaled_NORTHR_x_A\.txt\"/acceleration_filename\ =\ \"base_correct_x_acc\.txt\"/' main.fei
	# sed -i 's/acceleration_filename\ =\ \"scaled_NORTHR_y_A\.txt\"/acceleration_filename\ =\ \"base_correct_y_acc\.txt\"/' main.fei
	# sed -i 's/acceleration_filename\ =\ \"scaled_NORTHR_z_A\.txt\"/acceleration_filename\ =\ \"base_correct_z_acc\.txt\"/' main.fei

	# sed -i 's/displacement_filename\ =\ \"scaled_NORTHR_x_D\.txt\"/displacement_filename\ =\ \"base_correct_x_dis\.txt\"/' main.fei
	# sed -i 's/displacement_filename\ =\ \"scaled_NORTHR_y_D\.txt\"/displacement_filename\ =\ \"base_correct_y_dis\.txt\"/' main.fei
	# sed -i 's/displacement_filename\ =\ \"scaled_NORTHR_z_D\.txt\"/displacement_filename\ =\ \"base_correct_z_dis\.txt\"/' main.fei

	# sed -i 's/213\.200716355\ \ \ 2000\ \ \ \ \ 0\.03\ \ \ 100/500\ \ \ \ \ \ \ \ \ \ \ \ \ 2000\ \ \ \ \ 0\.03\ \ \ 100/' soil_profile.txt
	# sed -i 's/319\.801074533\ \ \ 2000\ \ \ \ \ 0\.03\ \ \ 100/750\ \ \ \ \ \ \ \ \ \ \ \ \ 2000\ \ \ \ \ 0\.03\ \ \ 100/' soil_profile_Vp.txt

	# sed -i 's/^Soil\_Elastic\_Modulus\ =\ 2e8\*Pa;/Soil\_Elastic\_Modulus\ =\ 1\.1e9\*Pa;/' main.fei
	# sed -i 's/^Elastic\ =\ 2e8\*N\/m\^2;/Elastic\ =\ 1\.1e9\*N\/m\^2;/' main.fei
	# sed -i 's/add\_compensation\_time\ =\ 0\.5\ \*\ s/add\_compensation\_time\ =\ 0\.0\ \*\ s/' main.fei


	# sed -i 's/time_step\ =\ 0\.01\*s\ ;/time_step\ =\ 0\.0419384905125\*s\ ;/' main.fei
	# sed -i 's/simulate\ 3500\ steps\ using\ transient\ algorithm\ /simulate\ 210\ steps\ using\ transient\ algorithm\ /' main.fei

	# sed -i 's/simulate\ 240\ steps\ using\ transient\ algorithm\ /simulate\ 210\ steps\ using\ transient\ algorithm\ /' main.fei
	# rm -f damping.fei
	# sed -i 's/include\ \"damping\.fei\";//' main.fei
	
	echo $PWD
	# rm -f *.tgz
	# tar -czvf ${PWD##*/}.tgz *
done