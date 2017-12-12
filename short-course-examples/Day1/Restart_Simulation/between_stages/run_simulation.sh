
# Run the simulation of all stages
essi -f 0main_all.fei

# Run the simulation of Stage 1 only
essi -f 1main_stage1.fei

# Run the simulation of Restart to Stage 2.
essi -f 2main_restart.fei

# Compare Node and Elements results
echo ""
echo "----------------------------------------------"
echo "Printing the Difference: "
echo "----------------------------------------------"
h5diff t_2.h5.feioutput t_2_restart.h5.feioutput /Model/Nodes
h5diff t_2.h5.feioutput t_2_restart.h5.feioutput /Model/Nodes
h5diff t_2.h5.feioutput t_2_restart.h5.feioutput /Date_and_Time_Start
h5diff t_2.h5.feioutput t_2_restart.h5.feioutput /Date_and_Time_End
echo "Done!"
echo ""
