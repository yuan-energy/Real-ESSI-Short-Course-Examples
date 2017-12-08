### Run Parallel Simulation
```bash
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
# e.g. node-tag 42143 is the center of foundation surface, to plot the acceleration series in x direction of node 42143 : 
python extract_node_acce.py soil_foundation_motion.h5.feioutput 42143 x
```

###### Extract the displacement of the DOF of the node in both time and frequency domain.
```bash
python extract_node_disp.py your_output.h5.feioutput your_nodetag your_dof
# e.g. node-tag 42143 is the center of foundation surface, to plot the displacement series in x direction of node 42143 : 
python extract_node_disp.py soil_foundation_motion.h5.feioutput 42143 x
```

###### Extract the response spectrum of the DOF of the node.
```bash
python extract_node_spectrum.py your_output.h5.feioutput your_nodetag your_dof
# e.g. node-tag 42143 is the center of foundation bottom, to plot the response spectrum in x direction of node 42143 : 
python extract_node_spectrum.py soil_foundation_motion.h5.feioutput 42143 x
```

#### Other Critical Points for Postprocessing
You can also use the python scripts to plot other points.

```
* Center of Foundation surface.
node # 42143 at (135.000000*m,135.000000*m,0.001000*m) with 3 dofs; 
* Center of Near Bottom Soil.
node # 22793 at (135.000000*m,135.000000*m,-20.000000*m) with 3 dofs; 
```
