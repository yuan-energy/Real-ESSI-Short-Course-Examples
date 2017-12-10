#!/bin/bash
# Format
# python script_path/script.py your_outputfilename.feioutput node_tag <x|y|z>

# Example:

# plot displacment in time and frequency domain at node # 4454 in x direction.
python postprocess/plot_node_disp.py DRM3D_motion.h5.feioutput 4454 x

# plot acceleration in time and frequency domain at node # 4454 in x direction.
python postprocess/plot_node_acce.py DRM3D_motion.h5.feioutput 4454 x

# plot acceleration in time and frequency domain at node # 11685 in x direction.
python postprocess/plot_node_acce.py DRM3D_motion.h5.feioutput 11685 x

# plot response spectrum (pseudo acceleration/displacement) in frequency domain at node # 4454 in x direction.
python postprocess/plot_node_spectrum_in_freq.py DRM3D_motion.h5.feioutput 4454 x

# plot response spectrum (pseudo acceleration/displacement) in period domain at node # 4454 in x direction.
python postprocess/plot_node_spectrum_in_period.py DRM3D_motion.h5.feioutput 4454 x

