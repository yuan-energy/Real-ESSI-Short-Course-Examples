#!/bin/bash

# Modify to specify the local directory you want
local_DIR=/home/yuan/public_html/shortCourse





# Download the examples.
git clone https://github.com/yuan-energy/Real-ESSI-Short-Course-Examples.git

echo "My local Directory for Examples: "
echo $local_DIR

# Copy the examples.
echo "Copying Examples to local Directory ... "
rm -rf $local_DIR/*
cp -r ./Real-ESSI-Short-Course-Examples/short-course-examples/* $local_DIR
echo "Done Copying Examples!"

echo "Cleaning Downloaded Examples ... "
rm -rf Real-ESSI-Short-Course-Examples
echo "Done Cleaning!"



