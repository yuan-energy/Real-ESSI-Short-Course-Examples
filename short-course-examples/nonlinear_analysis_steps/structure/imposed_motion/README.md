### Run Sequential or parallel simulation
```bash
./run_sequential_simulation.sh main.fei
./run_parallel_simulation.sh main.fei
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
# e.g. : 
python plot_node_acce.py shell_structure_motion.h5.feioutput 38 x
```

###### Plot the displacement of the DOF of the node in both time and frequency domain.
```bash
# python plot_node_acce.py model_name_loading_stage.h5.feioutput your_nodetag your_dof
# e.g. : 
python plot_node_acce.py shell_structure_motion.h5.feioutput 38 x
```

###### Plot the response spectrum of the DOF of the node.
```bash
# python plot_node_acce.py model_name_loading_stage.h5.feioutput your_nodetag your_dof
# e.g. : 
python plot_node_acce.py shell_structure_motion.h5.feioutput 38 x
```

#### Critical Points for Postprocessing
You can also use the python scripts to plot other points.

```
* Center of Topmost Structure.
node 38 at (135.000*m,135.000*m,60.001*m) with 6 dofs; 
* Center of Foundation bottom. 
node 5 at (135.000*m,135.000*m,-4.999*m) with 6 dofs; 
```





