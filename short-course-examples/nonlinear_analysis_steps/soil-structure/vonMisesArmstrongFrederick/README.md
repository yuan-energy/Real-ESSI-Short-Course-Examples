### Run Sequential or parallel simulation
```bash
./run_sequential_simulation.sh
./run_parallel_simulation.sh
```

### Execution the Paraview for Postprocessing
```bash
paraview your_results.h5.feioutput
```

### Execution the Python Scripts for Postprocessing
```bash
./run_plot_results.sh
```
which actually executes 3 python scripts for three different results as follow.s

###### Extract the acceleration of the DOF of the node in both time and frequency domain.
```bash
python extract_node_acce.py your_output.h5.feioutput your_nodetag your_dof
# e.g. node-tag 38 is the center of topmost structure, to plot the acceleration series in x direction of node 38 : 
python extract_node_acce.py shell_structure_motion.h5.feioutput 38 x
```

###### Extract the displacement of the DOF of the node in both time and frequency domain.
```bash
python extract_node_disp.py your_output.h5.feioutput your_nodetag your_dof
# e.g. node-tag 38 is the center of topmost structure, to plot the displacement series in x direction of node 38 : 
python extract_node_disp.py shell_structure_motion.h5.feioutput 38 x
```

###### Extract the response spectrum of the DOF of the node.
```bash
python extract_node_spectrum.py your_output.h5.feioutput your_nodetag your_dof
# e.g. node-tag 3391 is the center of foundation bottom, to plot the response spectrum in x direction of node 3391 : 
python extract_node_spectrum.py shell_structure_motion.h5.feioutput 3391 x
```

#### Other Critical Points for Postprocessing
You can also use the python scripts to plot other points.
```
* Center of Topmost Structure.
node 38    at (135.000*m,135.000*m,60.001*m) with 6 dofs; 
* Center of Foundation Bottom. 
node 3391  at (135.000*m,135.000*m,-5.000*m) with 3 dofs; 
* Center of near Soil Bottom
node 23436 at (135.000*m,135.000*m,-25.000*m) with 3 dofs; 
```



