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
# e.g. : 
python extract_node_acce.py shell_structure_motion.h5.feioutput 8217 x
```

###### Extract the displacement of the DOF of the node in both time and frequency domain.
```bash
python extract_node_disp.py your_output.h5.feioutput your_nodetag your_dof
# e.g. : 
python extract_node_disp.py shell_structure_motion.h5.feioutput 8217 x
```

###### Extract the response spectrum of the DOF of the node.
```bash
python extract_node_spectrum.py your_output.h5.feioutput your_nodetag your_dof
# e.g. : 
python extract_node_spectrum.py shell_structure_motion.h5.feioutput 8217 x
```

#### Critical Points for Postprocessing
You can also use the python scripts to plot other points.

```
* Center of Topmost Structure.
node 8217 at (105.000*m,105.000*m,60*m) with 6 dofs; 
* Center of Foundation bottom. 
node 1973 at (105.000*m,105.000*m,-5.000*m) with 3 dofs; 
* Center of middle soil 
node 13552 at (105.000*m,105.000*m,-20.000*m) with 3 dofs;  
* Center of bottom soil (DRM exterior node)
node 13555 at (105.000*m,105.000*m,-35.000*m) with 3 dofs; 
```

```
* Near structure of surface soil
add node  7973 at (110.000*m,105.000*m,0.000*m) with 3 dofs; 
* Near structure of shallow soil
add node  1978 at (110.000*m,105.000*m,-5.000*m) with 3 dofs; 
* Near structure of middle soil
add node  13587 at (110.000*m,105.000*m,-20.000*m) with 3 dofs; 
* Near structure of bottom soil (DRM exterior node)
add node  13590 at (110.000*m,105.000*m,-35.000*m) with 3 dofs; 
```

```
* Near DRM of surface soil
add node  7169 at (20.000*m,105.000*m,0.000*m) with 3 dofs; 
* Near DRM of shallow soil
add node  1893 at (20.000*m,105.000*m,-5.000*m) with 3 dofs; 
* Near DRM of middle soil
add node  12992 at (20.000*m,105.000*m,-20.000*m) with 3 dofs; 
* Near DRM of bottom soil (DRM exterior node)
add node  12995 at (20.000*m,105.000*m,-35.000*m) with 3 dofs; 
```








