




# Working on the soil profile file
if [ -f soil_profile.txt ] 
	then
	cp soil_profile.txt soil_profile_set1_Vs.txt
	cp soil_profile_Vp.txt soil_profile_set1_Vp.txt
	cp soil_profile_set1_Vs.txt soil_profile_set2_Vs.txt
	cp soil_profile_set1_Vp.txt soil_profile_set2_Vp.txt
	cp soil_profile_set1_Vs.txt soil_profile_set3_Vs.txt
	cp soil_profile_set1_Vp.txt soil_profile_set3_Vp.txt

	sed -i 's/^500\ /1000/' soil_profile_set2_Vs.txt
	sed -i 's/^500/300/' soil_profile_set3_Vs.txt

	sed -i 's/^750\ /1500/' soil_profile_set2_Vp.txt
	sed -i 's/^750/450/' soil_profile_set3_Vp.txt

	# Working on the material file
	sed -i '/^\/\/\ The Corresponding Vs or Vp for deconvolution/ d' material.fei
	sed -i '/^soil_profile_Vs_filename\ =\ / d' material.fei
	sed -i '/^soil_profile_Vp_filename\ =\ / d' material.fei
	
	sed -i '$ G   ' material.fei
	sed -i '$ a \/\/\ The Corresponding Vs or Vp for deconvolution ' material.fei
	sed -i '$ a soil_profile_Vs_filename = \"soil_profile_set1_Vs\.txt\"; ' material.fei
	sed -i '$ a soil_profile_Vp_filename = \"soil_profile_set1_Vp\.txt\"; ' material.fei
	sed -i '$ G   ' material.fei

fi




# Working on the material file

cp material.fei material_set1.fei
cp material.fei material_set2.fei
cp material.fei material_set3.fei

sed -i 's/elastic_modulus\ =\ 1\.1e9\*N\/m\^2/elastic_modulus\ =\ 4\.4\*\GPa/' material_set2.fei
sed -i 's/elastic_modulus\ =\ 1\.1e9\*N\/m\^2/elastic_modulus\ =\ 396\*\MPa/' material_set3.fei

sed -i 's/soil_profile_set1_Vs/soil_profile_set2_Vs/' material_set2.fei
sed -i 's/soil_profile_set1_Vp/soil_profile_set2_Vp/' material_set2.fei
sed -i 's/soil_profile_set1_Vs/soil_profile_set3_Vs/' material_set3.fei
sed -i 's/soil_profile_set1_Vp/soil_profile_set3_Vp/' material_set3.fei














# Working on the main.fei file
sed -i '/^include\ \"material/d' main.fei
sed -i '/^\/\/\ include\ \"material/d' main.fei
sed -i '/^include\ \"node\.fei\"/ i include\ \"material_set1\.fei\";' main.fei 
sed -i '/^include\ \"material_set1\.fei\"/ a \/\/\ include\ \"material_set3\.fei\";' main.fei
sed -i '/^include\ \"material_set1\.fei\"/ a \/\/\ include\ \"material_set2\.fei\";' main.fei

sed -i 's/soil_profile_filename\ =\ \"soil_profile\.txt\"/soil_profile_filename\ =\ soil_profile_Vs_filename/' main.fei
sed -i 's/soil_profile_filename\ =\ \"soil_profile_Vp\.txt\"/soil_profile_filename\ =\ soil_profile_Vp_filename/' main.fei




