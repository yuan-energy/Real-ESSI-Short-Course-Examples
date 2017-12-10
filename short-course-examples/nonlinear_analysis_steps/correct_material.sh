
current_dir=${PWD}
all_dir_array=( $(find . -type d  ) )

for element in $(seq 0 $((${#all_dir_array[@]} - 1)))
do

	cd ${current_dir}
	
	
	cd ${current_dir}/"${all_dir_array[$element]}"

	if [ -f $PWD/vonMisesArmstrongFrederick/main.fei ]
	    then
	    	echo $PWD/vonMisesArmstrongFrederick/
	    	cp ${current_dir}/material_set1.fei $PWD/vonMisesArmstrongFrederick/
	    	cp ${current_dir}/material_set2.fei $PWD/vonMisesArmstrongFrederick/
	    	cp ${current_dir}/material_set3.fei $PWD/vonMisesArmstrongFrederick/
	fi

	# if [ -f $PWD/vonMisesGoverGmax/main.fei ]
	#     then
	#     	echo $PWD/vonMisesGoverGmax/
	#     	cp ${current_dir}/material_set1.fei $PWD/vonMisesGoverGmax/
	#     	cp ${current_dir}/material_set2.fei $PWD/vonMisesGoverGmax/
	#     	cp ${current_dir}/material_set3.fei $PWD/vonMisesGoverGmax/
	# fi

	# if [ -f $PWD/DruckerPragerGoverGmax/main.fei ]
	#     then
	#     	echo $PWD/DruckerPragerGoverGmax/
	#     	cp ${current_dir}/material_set1.fei $PWD/DruckerPragerGoverGmax/
	#     	cp ${current_dir}/material_set2.fei $PWD/DruckerPragerGoverGmax/
	#     	cp ${current_dir}/material_set3.fei $PWD/DruckerPragerGoverGmax/
	# fi
	# echo $PWD
	# rm -f *.tgz
	# tar -czvf ${PWD##*/}.tgz *
done
