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
which actually executes 3 python scripts for three different results as follow.s

###### Plot the acceleration of the DOF of the node in both time and frequency domain.
```bash
# python plot_node_acce.py model_name_loading_stage.h5.feioutput your_nodetag your_dof
# e.g. node-tag 38 is the center of topmost structure, to plot the acceleration series in x direction of node 38 : 
python plot_node_acce.py shell_structure_motion.h5.feioutput 38 x
```

###### Plot the displacement of the DOF of the node in both time and frequency domain.
```bash
# python plot_node_disp.py model_name_loading_stage.h5.feioutput your_nodetag your_dof
# e.g. node-tag 38 is the center of topmost structure, to plot the displacement series in x direction of node 38 : 
python plot_node_disp.py shell_structure_motion.h5.feioutput 38 x
```

###### Plot the response spectrum of the DOF of the node.
```bash
# python plot_node_spectrum_in_period.py model_name_loading_stage.h5.feioutput your_nodetag your_dof
# e.g. node-tag 3391 is the center of foundation bottom, to plot the response spectrum in x direction of node 3391 : 
python plot_node_spectrum_in_period.py shell_structure_motion.h5.feioutput 3391 x
```

#### Other Points for Postprocessing
You can also use the python scripts to plot other points.
```
* Center of Topmost Structure.
node 38    at (135.000*m,135.000*m,60.001*m) with 6 dofs; 
* Center of Foundation Bottom. 
node 3391  at (135.000*m,135.000*m,-5.000*m) with 3 dofs; 
* Center of near Soil Bottom
node 23436 at (135.000*m,135.000*m,-25.000*m) with 3 dofs; 
```



