#!/bin/bash
# Format
# python script_path/script.py your_outputfilename.feioutput node_tag <x|y|z>

# Example:

# plot displacment in time and frequency domain at node # 30239 in x direction.
python postprocess/extract_node_disp.py soil_foundation_motion.h5.feioutput 30239 x

# plot acceleration in time and frequency domain at node # 30239 in x direction.
python postprocess/extract_node_acce.py soil_foundation_motion.h5.feioutput 30239 x

# plot response spectrum (pseudo acceleration/displacement) in frequency domain at node # 2685 in x direction.
python postprocess/extract_node_spectrum_in_freq.py soil_foundation_motion.h5.feioutput 2685 x

# plot response spectrum (pseudo acceleration/displacement) in period domain at node # 2685 in x direction.
python postprocess/extract_node_spectrum_in_period.py soil_foundation_motion.h5.feioutput 2685 x


