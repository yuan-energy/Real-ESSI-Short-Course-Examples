### Run Parallel Simulation
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
which actually executes 3 python scripts for three different results as follow.s

###### Plot the acceleration of the DOF of the node in both time and frequency domain.
```bash
# python plot_node_acce.py model_name_loading_stage.h5.feioutput your_nodetag your_dof
# e.g. node-tag 42143 is the center of foundation surface, to plot the acceleration series in x direction of node 42143 : 
python plot_node_acce.py soil_foundation_motion.h5.feioutput 42143 x
```

###### Plot the displacement of the DOF of the node in both time and frequency domain.
```bash
# python plot_node_disp.py model_name_loading_stage.h5.feioutput your_nodetag your_dof
# e.g. node-tag 42143 is the center of foundation surface, to plot the displacement series in x direction of node 42143 : 
python plot_node_disp.py soil_foundation_motion.h5.feioutput 42143 x
```

###### Plot the response spectrum of the DOF of the node.
```bash
# python plot_node_spectrum_in_period.py model_name_loading_stage.h5.feioutput your_nodetag your_dof
# e.g. node-tag 42143 is the center of foundation bottom, to plot the response spectrum in x direction of node 42143 : 
python plot_node_spectrum_in_period.py soil_foundation_motion.h5.feioutput 42143 x
```

#### Other Points for Postprocessing
You can also use the python scripts to plot other points.

```
* Center of Foundation surface.
node # 42143 at (135.000000*m,135.000000*m,0.001000*m) with 3 dofs; 
* Center of Near Bottom Soil.
node # 22793 at (135.000000*m,135.000000*m,-20.000000*m) with 3 dofs; 
```
