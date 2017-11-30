
# Open the leaf folder
cd structure/imposed_motion

# Run the simulation 
./run_sequential_simulation.sh 

# Visualize in paraview
paraview shell_structure_imposed_motion.h5.feioutput & 

# Visualize in Python
./run_plot_results.sh




