
# Open the leaf folder
cd free_field_3D/elastic

# Run the simulation 
./run_parallel_simulation.sh 

# Visualize in paraview
paraview DRM3D_motion.h5.feioutput & 

# Visualize in Python
./run_plot_results.sh

# Compare in Python
./run_plot_compare.sh




