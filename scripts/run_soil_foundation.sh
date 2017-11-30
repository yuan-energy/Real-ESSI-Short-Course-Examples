
# Open the leaf folder
cd soil-foundation/elastic

# Run the simulation 
./run_parallel_simulation.sh 

# Visualize in paraview
paraview soil_foundation_motion.h5.feioutput & 

# Visualize in Python
./run_plot_results.sh




