
current_dir=${PWD}
all_dir_array=( $(find . -type d  ) )

for element in $(seq 0 $((${#all_dir_array[@]} - 1)))
do

	cd ${current_dir}
	
	
	cd ${current_dir}/"${all_dir_array[$element]}"

	if [ -f $PWD/main.fei ]
	    then
	    	echo $PWD

	    	sed -i 's/extract_node_disp/plot_node_disp/' run_plot_results.sh
	    	sed -i 's/extract_node_acce/plot_node_acce/' run_plot_results.sh
	    	sed -i 's/extract_node_spectrum_in_freq/plot_node_spectrum_in_freq/' run_plot_results.sh
	    	sed -i 's/extract_node_spectrum_in_period/plot_node_spectrum_in_period/' run_plot_results.sh
	fi

	if [ -f $PWD/extract_node_acce.py ]
	    then
	    	echo $PWD
	    	mv extract_node_disp.py plot_node_disp.py
	    	mv extract_node_acce.py plot_node_acce.py
	    	mv extract_node_spectrum_in_freq.py plot_node_spectrum_in_freq.py
	    	mv extract_node_spectrum_in_period.py plot_node_spectrum_in_period.py
	fi

	# echo $PWD
	# rm -f *.tgz
	# tar -czvf ${PWD##*/}.tgz *
done
