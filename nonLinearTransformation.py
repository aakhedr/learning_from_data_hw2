import numpy as np 
import random
from buildDataSet import *
from linearRegression import *

def simulateNoise(data, noise=.1):
	'''
	Picks noise percent of the data and flip its y value
	Returns the data set with noise percent noise
	'''
	for i in range(int(len(data) * noise)):
		index = random.randint(0, len(data) - 1)
		if data[index, -1] == 1:
			data[index, -1] = -1
		else:
			data[index, -1] = 1

	return data

def addFeatures(dataSet):
	'''
	Add more features as per spec of question9
	'''
	X, y = extract(data)
	x3 = X[:, 1] * X[:, 2]
	x4 = X[:, 1]**2
	x5 = X[:, 2]**2
	dataSet = np.column_stack((X, x3, x4, x5, y))

	return dataSet

# Run experiement 1000 times
Ein = []
data, slope, intercept = buildDataSet(N=1000)
[X, y] = extract(data)
X = addIntercept(X)
data = np.column_stack((X, y))

for i in range(1000):
	# question8
	data = simulateNoise(data=data, noise=.1)
	w = calculateWeights(data)
	Ein.append(calculateError(w, data))

print sum(Ein)/ float(len(Ein))

# question9
data = addFeatures(data)
w = calculateWeights(data)
myG = calculateError(w, data)
print 'Ein by w found', myG


choices = [[-1, -.05, .08, .13, 1.5, 1.5], [-1, -.05, .08, .13, 1.5, 15], 
[-1, -.05, .08, .13, 15, 1.5], [-1, -1.5, .08, .13, .05, .05], 
[-1, -.05, .08, 1.5, .15, .15]]

for j in range(len(choices)):
	print 'Ein by choice ', j
	print calculateError(choices[j], data)

