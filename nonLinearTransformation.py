import numpy as np 
import random
from buildDataSet import *
from linearRegression import *

def simulateNoise(noise=.1):
	'''
	Picks noise percent of the data and flip its y value
	Returns the data set with noise percent noise
	'''
	for i in range(int(len(data) * noise)):
		index = random.randint(0, len(data) - 1)
		if data[index, 2] == 1:
			data[index, 2] = -1
		else:
			data[index, 2] = 1

	return data

# Run experiement 1000 times
Ein = []
data, slope, intercept = buildDataSet(N=1000)
for i in range(1000):
	data = simulateNoise()
	w = calculateWeights(data)
	Ein.append(calculateError(w, data))

print sum(Ein)/ float(len(Ein))