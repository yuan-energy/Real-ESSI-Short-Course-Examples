
current_dir=${PWD}
deepest_dir_array=( $(find . -type d  ) )

for element in $(seq 0 $((${#deepest_dir_array[@]} - 1)))
do

	cd ${current_dir}
	
	
	cd ${current_dir}/"${deepest_dir_array[$element]}"

	if [ -f $PWD/main.fei ]
	    then
	    	echo $PWD

	    	mkdir -p sample_results
	    	mv *_node_*_x_*.txt sample_results
	    	mv *_node_*_x_*.pdf sample_results

	    	mkdir -p motion
	    	mv base_correct*.txt motion
	    	mv scaled_NORTHR_*.txt motion
	    	mv scaled_northridge*.dat motion
	    	mv sw4_free_field_center*.txt motion

	    	mkdir -p preprocess
	    	mv *.geo preprocess
	    	mv *.gmessi preprocess
	    	mv *.msh preprocess

	    	mkdir -p postprocess
	    	mv extract_node_* postprocess
	    	mv compare_top_acc.py postprocess
	    	
	    	sed -i 's/acceleration\_filename\ =\ \"sw4/acceleration\_filename\ =\ \"\.\/motion\/sw4/' main.fei
	    	sed -i 's/displacement\_filename\ =\ \"sw4/displacement\_filename\ =\ \"\.\/motion\/sw4/' main.fei

	    	sed -i 's/python\ extract_node_/python\ postprocess\/extract_node_/' run_plot_results.sh

	    	# echo $PWD
	    	rm -f *.tgz
	    	rm -f *.tar.gz
	    	tar -czvf _all_files_packaged_for_${PWD##*/}.tar.gz *
	else
		:
	fi


	# echo $PWD
	# rm -f *.tgz
	# tar -czvf ${PWD##*/}.tgz *
done
