
current_dir=${PWD}
all_dir_array=( $(find . -type d  ) )

for element in $(seq 0 $((${#all_dir_array[@]} - 1)))
do

	cd ${current_dir}
	
	
	cd ${current_dir}/"${all_dir_array[$element]}"

	if [ -f $PWD/main.fei ]
	    then
	    	echo $PWD
	    	rm -f material.fei
	    	rm -f soil_profile.txt
	    	rm -f soil_profile_Vp.txt
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
