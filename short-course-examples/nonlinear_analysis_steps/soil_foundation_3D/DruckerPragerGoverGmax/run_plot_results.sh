#!/bin/bash
# Format
# python script_path/script.py your_outputfilename.feioutput node_tag <x|y|z>

# Example:

# plot displacment in time and frequency domain at node # 42143 in x direction.
python postprocess/extract_node_disp.py soil_foundation_motion.h5.feioutput 42143 x

# plot acceleration in time and frequency domain at node # 42143 in x direction.
python postprocess/extract_node_acce.py soil_foundation_motion.h5.feioutput 42143 x

# plot acceleration in time and frequency domain at node # 22793 in x direction.
python postprocess/extract_node_acce.py soil_foundation_motion.h5.feioutput 22793 x

# plot response spectrum (pseudo acceleration/displacement) in frequency domain at node # 42143 in x direction.
python postprocess/extract_node_spectrum_in_freq.py soil_foundation_motion.h5.feioutput 42143 x

# plot response spectrum (pseudo acceleration/displacement) in period domain at node # 42143 in x direction.
python postprocess/extract_node_spectrum_in_period.py soil_foundation_motion.h5.feioutput 42143 x


