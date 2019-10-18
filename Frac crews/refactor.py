import errno
import pandas as pd
import glob

#numpy will have built in methods for calculations
import numpy as np 		

csvFiles = glob.glob("./*.csv")

#create the map
#...

csvFiles.remove(".\\mobilization_time.csv")

print("Starting the calculations and combining the dataset...")

for f in csvFiles:
	series = pd.read_csv(f[2:])
	array = series.values
	print(f, "\n", array, "\n--------------------------------------------------------\n")