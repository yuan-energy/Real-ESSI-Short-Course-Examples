### Run Sequential or parallel simulation
```bash
./run_sequential_simulation.sh
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
# e.g. node-tag 9 is the center of soil surface, to plot the acceleration series in x direction of node 9 : 
python plot_node_acce.py shell_structure_motion.h5.feioutput 9 x
```

###### Plot the displacement of the DOF of the node in both time and frequency domain.
```bash
# python plot_node_disp.py model_name_loading_stage.h5.feioutput your_nodetag your_dof
# e.g. node-tag 9 is the center of soil surface, to plot the displacement series in x direction of node 9 : 
python plot_node_disp.py shell_structure_motion.h5.feioutput 9 x
```

###### Plot the response spectrum of the DOF of the node.
```bash
# python plot_node_spectrum_in_period.py model_name_loading_stage.h5.feioutput your_nodetag your_dof
# e.g. node-tag 9 is the center of soil surface, to plot the response spectrum in x direction of node 9 : 
python plot_node_spectrum_in_period.py shell_structure_motion.h5.feioutput 9 x
```

#### Other Points for Postprocessing
You can also use the python scripts to plot other points.

```
* Surface soil
  node # 9
* Near Bottom soil
  node # 16
```







