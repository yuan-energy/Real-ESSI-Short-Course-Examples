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
# e.g. node-tag 30239 is the center of foundation surface, to plot the acceleration series in x direction of node 30239 : 
python extract_node_acce.py soil_foundation_motion.h5.feioutput 30239 x
```

###### Extract the displacement of the DOF of the node in both time and frequency domain.
```bash
python extract_node_disp.py your_output.h5.feioutput your_nodetag your_dof
# e.g. node-tag 30239 is the center of foundation surface, to plot the displacement series in x direction of node 30239 : 
python extract_node_disp.py soil_foundation_motion.h5.feioutput 30239 x
```

###### Extract the response spectrum of the DOF of the node.
```bash
python extract_node_spectrum.py your_output.h5.feioutput your_nodetag your_dof
# e.g. node-tag 2685 is the center of foundation bottom, to plot the response spectrum in x direction of node 2685 : 
python extract_node_spectrum.py soil_foundation_motion.h5.feioutput 2685 x
```

#### Other Critical Points for Postprocessing
You can also use the python scripts to plot other points.

```
* Center of Foundation surface.
node 30239 at (135.000*m,135.000*m,60.001*m) with 6 dofs; 
* Center of Foundation bottom. 
node 2685 at (135.000*m,135.000*m,-5.000*m) with 3 dofs; 
* Center of middle soil 
node 21097 at (135.000*m,135.000*m,-20.000*m) with 3 dofs;  
* Center of bottom soil (DRM exterior node)
node 21100 at (135.000*m,135.000*m,-35.000*m) with 3 dofs; 
```

```
* Near structure of surface soil
add node  10568 at (110.000*m,135.000*m,0.000*m) with 3 dofs; 
* Near structure of shallow soil
add node  2657 at (110.000*m,135.000*m,-5.000*m) with 3 dofs; 
* Near structure of middle soil
add node  20901 at (110.000*m,135.000*m,-20.000*m) with 3 dofs; 
* Near structure of bottom soil (DRM exterior node)
add node  20904 at (110.000*m,135.000*m,-35.000*m) with 3 dofs; 
```

```
* Near DRM of surface soil
add node  10694 at (20.000*m,135.000*m,0.000*m) with 3 dofs; 
* Near DRM of shallow soil
add node  20019 at (20.000*m,135.000*m,-5.000*m) with 3 dofs; 
* Near DRM of middle soil
add node  20019 at (20.000*m,135.000*m,-20.000*m) with 3 dofs; 
* Near DRM of bottom soil (DRM exterior node)
add node  20022 at (20.000*m,135.000*m,-35.000*m) with 3 dofs; 
```








