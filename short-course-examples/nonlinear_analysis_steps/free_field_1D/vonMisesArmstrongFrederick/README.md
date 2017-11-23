### Run Sequential or parallel simulation
```bash
./run_sequential_simulation.sh main.fei
./run_parallel_simulation.sh main.fei
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
# e.g. node-tag 5 is the center of soil surface, to plot the acceleration series in x direction of node 5 : 
python extract_node_acce.py shell_structure_motion.h5.feioutput 5 x
```

###### Extract the displacement of the DOF of the node in both time and frequency domain.
```bash
python extract_node_disp.py your_output.h5.feioutput your_nodetag your_dof
# e.g. node-tag 5 is the center of soil surface, to plot the displacement series in x direction of node 5 : 
python extract_node_disp.py shell_structure_motion.h5.feioutput 5 x
```

###### Extract the response spectrum of the DOF of the node.
```bash
python extract_node_spectrum.py your_output.h5.feioutput your_nodetag your_dof
# e.g. node-tag 5 is the center of soil surface, to plot the response spectrum in x direction of node 5 : 
python extract_node_spectrum.py shell_structure_motion.h5.feioutput 5 x
```

#### Critical Points for Postprocessing
You can also use the python scripts to plot other points.

```
* Surface soil
add node  5 at (110.000*m,135.000*m,0.000*m) with 3 dofs; 
* Shallow soil
add node  17 at (110.000*m,135.000*m,-5.000*m) with 3 dofs; 
* Middle soil
add node  14 at (110.000*m,135.000*m,-20.000*m) with 3 dofs; 
* Bottom soil (DRM exterior node)
add node  11 at (110.000*m,135.000*m,-35.000*m) with 3 dofs; 
```







