
# Run the simulation with different element size.
cd element1m
bash run_sequential_simulation.sh
cd ..

cd element5m
bash run_sequential_simulation.sh
cd ..

cd element20m
bash run_sequential_simulation.sh
cd .. 




# Plot all results for comparison
python plot_freq_all.py
python plot_time_all.py
