#!/bin/bash
# Format
# python script_path/script.py your_outputfilename.feioutput node_tag <x|y|z>

# Example:

# plot displacment in time and frequency domain at node # 6 in x direction.
python postprocess/plot_node_disp.py DRM1D_motion.h5.feioutput 6 x

# plot acceleration in time and frequency domain at node # 6 in x direction.
python postprocess/plot_node_acce.py DRM1D_motion.h5.feioutput 6 x

# plot acceleration in time and frequency domain at node # 21 in x direction.
python postprocess/plot_node_acce.py DRM1D_motion.h5.feioutput 21 x

# plot response spectrum (pseudo acceleration/displacement) in frequencies at node # 6 in x direction.
python postprocess/plot_node_spectrum_in_freq.py DRM1D_motion.h5.feioutput 6 x

# plot response spectrum (pseudo acceleration/displacement) in periods at node # 6 in x direction.
python postprocess/plot_node_spectrum_in_period.py DRM1D_motion.h5.feioutput 6 x




