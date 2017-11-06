import numpy as np 
import sys 

filename = sys.argv[1]
time_step = sys.argv[2]
# filename = "RSN164_IMPVALL.H_H-CPE147.AT2"
# time_step = 0.01

data = []
skiprows = 4 
row = 0
with open(filename) as f:
	for line in f:
		if row < skiprows :
			row = row + 1
			continue
		items = line.split()
		for item in items:
			data.append(item)


with open("essi"+filename+".txt", 'w') as f:
	for i in range(len(data)):
		f.write ( str(i * float(time_step)) + " \t " + str(data[i]) + "\n")


