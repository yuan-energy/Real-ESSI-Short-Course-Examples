
current_dir=${PWD}
deepest_dir_array=( $(find . -type d  ) )

for element in $(seq 0 $((${#deepest_dir_array[@]} - 1)))
do

	cd ${current_dir}
	
	
	cd ${current_dir}/"${deepest_dir_array[$element]}"

	if [ -f $PWD/main.fei ]
	    then
	    	echo $PWD
	    	
	    	# cp -f ${current_dir}/run*.sh ${current_dir}/"${deepest_dir_array[$element]}"/
	    	# cp -f ${current_dir}/*.md ${current_dir}/"${deepest_dir_array[$element]}"/
	    	# cp -f ${current_dir}/*.html ${current_dir}/"${deepest_dir_array[$element]}"/
	    	# cp -f ${current_dir}/*.png ${current_dir}/"${deepest_dir_array[$element]}"/
	    	# rm geometry_slice.png
	    	# rm slice_overview.png
	    	rm -f run_sequential_simulation.sh
	    	# cd motion
	    	# pyplot_acc base_correct_x_acc.txt
	    	# pyplot_acc base_correct_y_acc.txt
	    	# pyplot_acc base_correct_z_acc.txt

	    	# pyplot_acc scaled_NORTHR_x_A.txt
	    	# pyplot_acc scaled_NORTHR_y_A.txt
	    	# pyplot_acc scaled_NORTHR_z_A.txt

	    	# pyplot_acc sw4_free_field_center_ax.txt
	    	# pyplot_acc sw4_free_field_center_ay.txt
	    	# pyplot_acc sw4_free_field_center_az.txt


	    	# pyplot_dis base_correct_x_dis.txt
	    	# pyplot_dis base_correct_y_dis.txt
	    	# pyplot_dis base_correct_z_dis.txt

	    	# pyplot_dis scaled_NORTHR_x_D.txt
	    	# pyplot_dis scaled_NORTHR_y_D.txt
	    	# pyplot_dis scaled_NORTHR_z_D.txt

	    	# pyplot_dis sw4_free_field_center_ux.txt
	    	# pyplot_dis sw4_free_field_center_uy.txt
	    	# pyplot_dis sw4_free_field_center_uz.txt



	    	# mkdir -p sample_results
	    	# mv *_node_*_x_*.txt sample_results
	    	# mv *_node_*_x_*.pdf sample_results

	    	# mkdir -p motion
	    	# mv base_correct*.txt motion
	    	# mv scaled_NORTHR_*.txt motion
	    	# mv scaled_northridge*.dat motion
	    	# mv sw4_free_field_center*.txt motion

	    	# mkdir -p preprocess
	    	# mv *.geo preprocess
	    	# mv *.gmessi preprocess
	    	# mv *.msh preprocess

	    	# mkdir -p postprocess
	    	# mv extract_node_* postprocess
	    	# mv compare_top_acc.py postprocess
	    	
	    	# sed -i 's/acceleration\_filename\ =\ \"sw4/acceleration\_filename\ =\ \"\.\/motion\/sw4/' main.fei
	    	# sed -i 's/displacement\_filename\ =\ \"sw4/displacement\_filename\ =\ \"\.\/motion\/sw4/' main.fei

	    	# sed -i 's/python\ extract_node_/python\ postprocess\/extract_node_/' run_plot_results.sh

	    	# echo $PWD
	    	# rm -f *.tgz
	    	# rm -f *.tar.gz
	    	# tar -czvf _all_files_packaged_for_${PWD##*/}.tar.gz *
	else
		:
	fi


	# echo $PWD
	# rm -f *.tgz
	# tar -czvf ${PWD##*/}.tgz *
done
