
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
	    	# rm -f edit_multiple_material.sh
	    	# bash edit_multiple_material.sh
	    	# cp ${current_dir}/wave_field*fei ${current_dir}/"${all_dir_array[$element]}"
	    	# cp ${current_dir}/damping_parameters.fei ${current_dir}/"${all_dir_array[$element]}"
	    	rm -f *acce.pdf
	    	rm -f *disp.pdf
	    	rm -f *spectrum_freq.pdf
	    	rm -f *spectrum_period.pdf
	    	rm -f *acce_compare.pdf
	    	
	    	rm -f *acce.txt
	    	rm -f *disp.txt
	    	rm -f *spectrum.txt
	    	# cp ${current_dir}/*.py ${current_dir}/"${all_dir_array[$element]}"/postprocess
	    	# cd motion
	    	# git checkout README.md

	    	# sed -i 's/your_results\.h5\.feioutput/model_name_loading_stage\.h5\.feioutput/' README.md
	    	# sed -i 's/your_output\.h5\.feioutput/model_name_loading_stage\.h5\.feioutput/' README.md

	    	# sed -i 's/Execution\ the\ Paraview\ for\ Postprocessing/Postprocessing\ with\ ParaView/' README.md

	    	# sed -i 's/Execution\ the\ Python\ Scripts\ for\ Postprocessing/Postprocessing\ with\ Python Scripts/' README.md

	    	# sed -i 's/Extract\ the\ acceleration\ of\ the\ DOF/Plot\ the\ acceleration\ of\ the\ DOF/' README.md

	    	# sed -i 's/Extract\ the\ displacement\ of\ the\ DOF/Plot\ the\ displacement\ of\ the\ DOF/' README.md

	    	# sed -i 's/Extract\ the\ response\ spectrum\ of\ the\ DOF/Plot\ the\ response\ spectrum\ of\ the\ DOF/' README.md

	    	# sed -i 's/Other\ Critical\ Points\ /Other\ Points\ /' README.md


	    	# sed -i 's/extract_node_acce\.py/plot_node_acce.py/' README.md
	    	# sed -i 's/extract_node_disp\.py/plot_node_acce.py/' README.md
	    	# sed -i 's/extract_node_spectrum\.py/plot_node_acce.py/' README.md


	    	# sed -i 's/^python\ plot_node_acce.py\ model_name_loading_stage/#\ python\ plot_node_acce.py\ model_name_loading_stage/' README.md

	    	# sed -i 's/^python\ plot_node_disp.py\ model_name_loading_stage/#\ python\ plot_node_disp.py\ model_name_loading_stage/' README.md

	    	# sed -i 's/^python\ plot_node_spectrum_in_period.py\ model_name_loading_stage/#\ python\ plot_node_spectrum_in_period.py\ model_name_loading_stage/' README.md

	    	# cat -s main.fei > main2.fei
	    	# mv main2.fei main.fei
	    	
	    	# grip --export

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

	    	echo $PWD
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
