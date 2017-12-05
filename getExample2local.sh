#!/bin/bash

# Modify to specify the local directory you want
local_DIR=/home/yuan/public_html/shortCourse
# And do the same string substitution in all tex files. 




# Download the examples.
git clone https://github.com/yuan-energy/Real-ESSI-Short-Course-Examples.git

echo "My local Directory for Examples: "
echo $local_DIR

# Copy the examples.
echo "Copying Examples to local Directory ... "
cp -r short-course-examples/* $local_DIR

echo "Done!"


