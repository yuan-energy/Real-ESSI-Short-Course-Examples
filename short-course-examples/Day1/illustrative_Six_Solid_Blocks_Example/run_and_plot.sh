# clean previous results
rm -f *.feioutput
rm -f essi*.log

# run essi simulation
essi -f main.fei


# postprocessing: paraview
paraview Six_Solid_Blocks_Example_With_Contact_Shear_Loading.h5.feioutput



