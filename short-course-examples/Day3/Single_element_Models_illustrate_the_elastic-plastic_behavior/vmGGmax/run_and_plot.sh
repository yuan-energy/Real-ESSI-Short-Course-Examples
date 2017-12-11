# clean previous results:
rm -f stress-strain*.pdf
rm -f *.feioutput
rm -f essi*.log

# run essi simulation:
essi -f main.fei

# postprocessing: plot GGmax
python plot_GGmax.py

