### Run Sequential Simulation
```bash
./run_sequential_simulation.sh
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
# e.g. node-tag 38 is the center of soil surface, to plot the acceleration series in x direction of node 38 : 
python plot_node_acce.py shell_structure_motion.h5.feioutput 38 x
```

###### Plot the displacement of the DOF of the node in both time and frequency domain.
```bash
# python plot_node_disp.py model_name_loading_stage.h5.feioutput your_nodetag your_dof
# e.g. node-tag 38 is the center of soil surface, to plot the displacement series in x direction of node 38 : 
python plot_node_disp.py shell_structure_motion.h5.feioutput 38 x
```

###### Plot the response spectrum of the DOF of the node.
```bash
# python extract_node_spectrum_in_period.py model_name_loading_stage.h5.feioutput your_nodetag your_dof
# e.g. node-tag 5 is the center of soil surface, to plot the response spectrum in x direction of node 5 : 
python extract_node_spectrum_in_period.py shell_structure_motion.h5.feioutput 5 x
```

#### Other Points for Postprocessing
You can also use the python scripts to plot other points.

```
* Center of Topmost Structure.
node 38 at (135.000*m,135.000*m,60.001*m) with 6 dofs; 
* Center of Foundation bottom. 
node 5 at (135.000*m,135.000*m,-4.999*m) with 6 dofs; 
```









