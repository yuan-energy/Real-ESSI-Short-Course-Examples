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


find . -name *tgz -delete

find . -type d -maxdepth 1 -mindepth 1 -exec tar zcvf {}.tgz {} \;

mv Earthquake_Soil-Structure_Interaction_3D_Model_with_DRM.tgz Earthquake_Soil-Structure_Interaction_3D_Model_with_DRM
mv Free_fields_3D_model_with_DRM.tgz Free_fields_3D_model_with_DRM
mv Shell_Structure_Soil_Interaction_3D_DRM.tgz Shell_Structure_Soil_Interaction_3D_DRM

