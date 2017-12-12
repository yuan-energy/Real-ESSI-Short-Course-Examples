
current_dir=${PWD}
all_dir_array=( $(find . -type d  ) )

for element in $(seq 0 $((${#all_dir_array[@]} - 1)))
do

	cd ${current_dir}
	
	
	cd ${current_dir}/"${all_dir_array[$element]}"

	if [ -f $PWD/main.fei ]
	    then
	    	echo $PWD
	    	# cp ${current_dir}/edit_multiple_material.sh ${current_dir}/"${all_dir_array[$element]}"/
	    	# cp ${current_dir}/README.* ${current_dir}/"${all_dir_array[$element]}"/

	    	cp ${current_dir}/boundary_condition.fei ${current_dir}/"${all_dir_array[$element]}"/
	    	cp ${current_dir}/damping.fei ${current_dir}/"${all_dir_array[$element]}"/

	   
	    	echo $PWD
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
