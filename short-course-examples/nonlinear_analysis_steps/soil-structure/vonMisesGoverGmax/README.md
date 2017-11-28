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
# e.g. node-tag 3195 is the center of foundation bottom, to plot the response spectrum in x direction of node 3195 : 
python extract_node_spectrum.py shell_structure_motion.h5.feioutput 3195 x
```

#### Other Critical Points for Postprocessing
You can also use the python scripts to plot other points.
```
* Center of Topmost Structure.
node 38 at (135.000*m,135.000*m,60.001*m) with 6 dofs; 
* Center of Foundation bottom. 
node 3195 at (135.000*m,135.000*m,-5.000*m) with 3 dofs; 
* Center of middle soil 
node 21607 at (135.000*m,135.000*m,-20.000*m) with 3 dofs;  
* Center of bottom soil (DRM exterior node)
node 21610 at (135.000*m,135.000*m,-35.000*m) with 3 dofs; 
```

```
* Near structure of surface soil
add node  11078 at (110.000*m,135.000*m,0.000*m) with 3 dofs; 
* Near structure of shallow soil
add node  3167 at (110.000*m,135.000*m,-5.000*m) with 3 dofs; 
* Near structure of middle soil
add node  21411 at (110.000*m,135.000*m,-20.000*m) with 3 dofs; 
* Near structure of bottom soil (DRM exterior node)
add node  21414 at (110.000*m,135.000*m,-35.000*m) with 3 dofs; 
```

```
* Near DRM of surface soil
add node  11204 at (20.000*m,135.000*m,0.000*m) with 3 dofs; 
* Near DRM of shallow soil
add node  3041 at (20.000*m,135.000*m,-5.000*m) with 3 dofs; 
* Near DRM of middle soil
add node  20529 at (20.000*m,135.000*m,-20.000*m) with 3 dofs; 
* Near DRM of bottom soil (DRM exterior node)
add node  20532 at (20.000*m,135.000*m,-35.000*m) with 3 dofs; 
```








