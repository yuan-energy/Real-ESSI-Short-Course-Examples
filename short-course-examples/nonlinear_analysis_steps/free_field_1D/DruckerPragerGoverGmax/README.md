### Run Sequential Simulation
```bash
./run_sequential_simulation.sh
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
# e.g. node-tag 6 is the center of soil surface, to plot the acceleration series in x direction of node 6 : 
python extract_node_acce.py shell_structure_motion.h5.feioutput 6 x
```

###### Extract the displacement of the DOF of the node in both time and frequency domain.
```bash
python extract_node_disp.py your_output.h5.feioutput your_nodetag your_dof
# e.g. node-tag 6 is the center of soil surface, to plot the displacement series in x direction of node 6 : 
python extract_node_disp.py shell_structure_motion.h5.feioutput 6 x
```

###### Extract the response spectrum of the DOF of the node.
```bash
python extract_node_spectrum.py your_output.h5.feioutput your_nodetag your_dof
# e.g. node-tag 6 is the center of soil surface, to plot the response spectrum in x direction of node 6 : 
python extract_node_spectrum.py shell_structure_motion.h5.feioutput 6 x
```

#### Other Critical Points for Postprocessing
You can also use the python scripts to plot other points.

```
* Surface soil
 Node # 6 
* Near Bottom Soil
 Node # 21
```







