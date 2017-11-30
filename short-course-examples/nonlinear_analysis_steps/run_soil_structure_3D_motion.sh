
# Open the leaf folder
cd soil-structure-3by1D-motion/elastic

# Run the simulation 
# ./run_parallel_simulation.sh 

# Visualize in paraview
paraview shell_structure_motion.h5.feioutput & 

# Visualize in Python
./run_plot_results.sh

# Compare in Python
./run_plot_compare.sh




