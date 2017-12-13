#!/bin/bash
# Format
# python script_path/script.py your_outputfilename.feioutput node_tag <x|y|z>

# Example:

# plot acceleration in time and frequency domain at node # 6 in x direction.
python postprocess/plot_node_acce.py test_motion.h5.feioutput 6 x


