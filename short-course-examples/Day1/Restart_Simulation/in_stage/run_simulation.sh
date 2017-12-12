
# Run the simulation with a relatively big tolerance.
essi -f 0main_all.fei

# Run the simulation with a very small tolerance (failed).
essi -f 1main_fail.fei

# Restart the failed simulation
essi -f 2main_restart.fei



# Compare Node and Elements results
echo ""
echo ""
echo "----------------------------------------------"
echo "Printing the Difference: "
echo "----------------------------------------------"
h5diff -r t_1.h5.feioutput t_1_restart.h5.feioutput /Date_and_Time_Start
h5diff -r t_1.h5.feioutput t_1_restart.h5.feioutput /Date_and_Time_End
echo "Done!"
echo ""

# Notes:
# Since the results are in different column of the hdf5 output,
# so h5diff always give lots of differences.
# The real results can be checked in paraview.


