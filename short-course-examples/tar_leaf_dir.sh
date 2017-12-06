#!/bin/bash
# ********************************************************************
# Author: Yuan Feng
# Date: Sun Sep 24 12:00:55 PDT 2017
# Comments: 
# 	1. This script will compress the complete files in each example
# 	   to one compressed tgz file in each example subfolder, 
#      such that we will have a downloadable link for each example. 
#   2. The downloadable link is then used in example documentation in
#      Lecture_notes or other documentation.
# ********************************************************************


current_dir=${PWD}
deepest_dir_array=( $(find . -type d -links 2 ) )

for element in $(seq 0 $((${#deepest_dir_array[@]} - 1)))
do
	cd ${current_dir}/"${deepest_dir_array[$element]}"
	echo $PWD

	sed  -i '/^\/\/$/d' *.fei
	sed  -i '/^\/\/\ $/d' *.fei
	sed  -i '/^\/\/\ http\:\/\/real\-essi\.info$/d' *.fei
	sed  -i '/^\/\/\ Modeling\ and\ Simulation\ Examples$/d' *.fei
	sed  -i '/^\/\/\ Real\ ESSI\ Simulator$/d' *.fei


	sed  -i '1i \/\/' *.fei
	sed  -i '1i \/\/\ http\:\/\/real\-essi\.info' *.fei
	sed  -i '1i \/\/\ Modeling\ and\ Simulation\ Examples' *.fei
	sed  -i '1i \/\/\ Real\ ESSI\ Simulator' *.fei
	sed  -i '1i \/\/\ ' *.fei



	rm -f *.tgz
	rm -f *.tar.gz
	tar -czvf _all_files_packaged_for_${PWD##*/}.tar.gz *

done