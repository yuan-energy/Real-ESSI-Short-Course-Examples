
current_dir=${PWD}
all_dir_array=( $(find . -type d  ) )

for element in $(seq 0 $((${#all_dir_array[@]} - 1)))
do

	cd ${current_dir}
	
	
	cd ${current_dir}/"${all_dir_array[$element]}"

	if [ -f $PWD/extract_node_spectrum_in_freq.py ]
	    then
	    	echo $PWD
	    	cp ${current_dir}/extract_node_spectrum_in_freq.py ${current_dir}/"${all_dir_array[$element]}"/
	fi

	# if [ -f $PWD/run_sequential_simulation.sh ]
	#     then
	#     	echo $PWD
	#     	cp ${current_dir}/run_sequential_simulation.sh ${current_dir}/"${all_dir_array[$element]}"/run_sequential_simulation.sh
	# else
	# 	:
	# fi
	# echo $PWD
	# rm -f *.tgz
	# tar -czvf ${PWD##*/}.tgz *
done
