
# Open the leaf folder
cd soil-structure/elastic

# Run the simulation 
./run_parallel_simulation.sh 

# Visualize in paraview
paraview shell_structure_motion.h5.feioutput & 

# Visualize in Python
./run_plot_results.sh




