# clean:
rm -f *.feioutput
rm -f essi*.log
# run:
essi -f main.fei
# plot:
python plot.py


# for pvESSI, pvpython and paraview if available
# pvpython pvESSI_camera.py *.h5.feioutput
