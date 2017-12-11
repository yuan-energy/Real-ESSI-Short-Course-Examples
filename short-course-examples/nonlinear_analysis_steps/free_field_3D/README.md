### Run Parallel simulation
```bash
./run_parallel_simulation.sh
```

### Postprocessing with ParaView
```bash
paraview model_name_loading_stage.h5.feioutput
```

### Postprocessing with Python Scripts
```bash
./run_plot_results.sh
```
which actually executes 3 python scripts for three different results as follows.

###### Plot the acceleration of the DOF of the node in both time and frequency domain.
```bash
# python plot_node_acce.py model_name_loading_stage.h5.feioutput your_nodetag your_dof
# e.g. node-tag 4417 is the center of soil surface, to plot the acceleration series in x direction of node 4417 : 
python plot_node_acce.py shell_structure_motion.h5.feioutput 4417 x
```

###### Plot the displacement of the DOF of the node in both time and frequency domain.
```bash
# python plot_node_disp.py model_name_loading_stage.h5.feioutput your_nodetag your_dof
# e.g. node-tag 4417 is the center of soil surface, to plot the displacement series in x direction of node 4417 : 
python plot_node_disp.py shell_structure_motion.h5.feioutput 4417 x
```

###### Plot the response spectrum of the DOF of the node.
```bash
# python plot_node_spectrum_in_period.py model_name_loading_stage.h5.feioutput your_nodetag your_dof
# e.g. node-tag 4417 is the center of soil surface, to plot the response spectrum in x direction of node 4417 : 
python plot_node_spectrum_in_period.py shell_structure_motion.h5.feioutput 4417 x
```

#### Other Points for Postprocessing
You can also use the python scripts to plot other points.

```
* Center of surface soil
 node # 4417 at (110.000*m,135.000*m,0.000*m) with 3 dofs; 
* Center of shallow soil
 node # 13202 at (110.000*m,135.000*m,-5.000*m) with 3 dofs; 
* Center of middle soil
 node # 13199 at (110.000*m,135.000*m,-20.000*m) with 3 dofs; 
* Center of bottom soil (DRM exterior node)
 node # 13196 at (110.000*m,135.000*m,-35.000*m) with 3 dofs; 
```

```
* Near DRM of surface soil
 node # 3679 at (20.000*m,135.000*m,0.000*m) with 3 dofs; 
* Near DRM of shallow soil
 node # 6560 at (20.000*m,135.000*m,-5.000*m) with 3 dofs; 
* Near DRM of middle soil
 node # 6557 at (20.000*m,135.000*m,-20.000*m) with 3 dofs; 
* Near DRM of bottom soil (DRM exterior node)
 node # 6554 at (20.000*m,135.000*m,-35.000*m) with 3 dofs; 
```








