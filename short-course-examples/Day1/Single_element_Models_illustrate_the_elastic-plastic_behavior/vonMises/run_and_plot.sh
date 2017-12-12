# clean 
rm -f *.feioutput
rm -f essi*.log

essi -f main.fei

python plot.py *h5.feioutput

