
current_dir=${PWD}
all_dir_array=( $(find . -type d  ) )

for element in $(seq 0 $((${#all_dir_array[@]} - 1)))
do

	cd ${current_dir}
	
	
	cd ${current_dir}/"${all_dir_array[$element]}"

	if [ -f $PWD/main.fei ]
	    then
	    	echo $PWD
	    	# sed -i 's/elastic_modulus\ =\ 1\.1e9\*N\/m\^2$/elastic_modulus\ =\ 1\.1e9\*N\/m\^2\ \ \ \/\/\ for\ shear\ wave\ velocity\ Vs\ =\ 500\ m\/s/' material_set1.fei
	    	# sed -i 's/elastic_modulus\ =\ 4\.4e9\*N\/m\^2$/elastic_modulus\ =\ 4\.4e9\*N\/m\^2\ \ \ \/\/\ for\ shear\ wave\ velocity\ Vs\ =\ 1000\ m\/s/' material_set2.fei
	    	# sed -i 's/elastic_modulus\ =\ 4\.4\*GPa$/elastic_modulus\ =\ 4\.4\*GPa\ \ \ \/\/\ for\ shear\ wave\ velocity\ Vs\ =\ 1000\ m\/s/' material_set2.fei
	    	# sed -i 's/elastic_modulus\ =\ 396\*MPa$/elastic_modulus\ =\ 396\*MPa\ \ \ \/\/\ for\ shear\ wave\ velocity\ Vs\ =\ 300\ m\/s/' material_set3.fei

	    	# sed -i '/\/\/\ \ \ \ m\/s\ \ \ \ \ \ \ kg\/m\^3\ \ / d'  soil_profile*txt
	    	# sed -i '/\/\/\ Vs_or_Vp\ \ \ \ \ rho\ \ \ \ \ damp\ \ \ thickness/ a \/\/\ \ \ \ m\/s\ \ \ \ \ \ \ kg\/m\^3\ \ \ \ \.\ \ \ \ meter' soil_profile*txt

	    	sed -i 's/vonmisesArmstrongFrederick/vonMisesArmstrongFrederick/' material_set*.fei
	    	
	    	# sed -i '/include\ \"boundary_condition\.fei\"/ d' main.fei
	    	# sed -i '/include\ \"element\.fei\";/ a include\ \"boundary_condition\.fei\";' main.fei

	else
		:
	fi

	# echo $PWD
	# rm -f *.tgz
	# tar -czvf ${PWD##*/}.tgz *
done
