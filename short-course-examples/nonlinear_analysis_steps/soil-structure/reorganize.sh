
current_dir=${PWD}
deepest_dir_array=( $(find . -type d  ) )

for element in $(seq 0 $((${#deepest_dir_array[@]} - 1)))
do

	cd ${current_dir}
	
	
	cd ${current_dir}/"${deepest_dir_array[$element]}"

	if [ -f $PWD/main.fei ]
	    then
	    	echo $PWD
	    	
	    	cp -f ${current_dir}/run_plot_results.sh ${current_dir}/"${deepest_dir_array[$element]}"

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
