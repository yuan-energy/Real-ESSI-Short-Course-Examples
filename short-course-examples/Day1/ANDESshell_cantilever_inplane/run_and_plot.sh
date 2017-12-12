# clean previous results
rm -f *.feioutput
rm -f essi*.log

# run essi simulation
essi -f main.fei


# postprocessing: paraview
paraview 6meter_cantilever_4NodeANDES_Fy.h5.feioutput


