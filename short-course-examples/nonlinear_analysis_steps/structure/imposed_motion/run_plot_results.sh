#!/bin/bash
# Format
# python script_path/script.py your_outputfilename.feioutput node_tag <x|y|z>

# Example:

# plot displacment in time and frequency domain at node # 38 in x direction.
python postprocess/extract_node_disp.py shell_structure_imposed_motion.h5.feioutput 38 x

# plot acceleration in time and frequency domain at node # 38 in x direction.
python postprocess/extract_node_acce.py shell_structure_imposed_motion.h5.feioutput 38 x

# plot response spectrum (pseudo acceleration/displacement) in frequencies at node # 38 in x direction.
python postprocess/extract_node_spectrum_in_freq.py shell_structure_imposed_motion.h5.feioutput 38 x

# plot response spectrum (pseudo acceleration/displacement) in periods at node # 38 in x direction.
python postprocess/extract_node_spectrum_in_period.py shell_structure_imposed_motion.h5.feioutput 38 x



