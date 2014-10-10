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
data = addIntercept(data)

# for i in range(1000):
# 	# question8
# 	data = simulateNoise(data=data, noise=.1)
# 	w = calculateWeights(data)
# 	Ein.append(calculateError(w, data))

# print sum(Ein)/ float(len(Ein))

# question9

data = addFeatures(data)
data = simulateNoise(data=data, noise=.1)

choices = [[-1, -.05, .08, .13, 1.5, 1.5], [-1, -.05, .08, .13, 1.5, 15], 
[-1, -.05, .08, .13, 15, 1.5], [-1, -1.5, .08, .13, .05, .05], 
[-1, -.05, .08, 1.5, .15, .15]]

Ein_w = []
Ein_a, Ein_b, Ein_c, Ein_d, Ein_e = [], [], [], [], []
for i in range(1000):
	w = calculateWeights(data)
	Ein_w.append(calculateError(w, data))

	Ein_a.append(calculateError(choices[0], data))
	Ein_b.append(calculateError(choices[1], data))
	Ein_c.append(calculateError(choices[2], data))
	Ein_d.append(calculateError(choices[3], data))
	Ein_e.append(calculateError(choices[4], data))

print 'Ein_w', sum(Ein_w)/ float(len(Ein_w))
print 'Ein_a', sum(Ein_a)/ float(len(Ein_a))
print 'Ein_b', sum(Ein_b)/ float(len(Ein_b))
print 'Ein_c', sum(Ein_c)/ float(len(Ein_c))
print 'Ein_d', sum(Ein_d)/ float(len(Ein_d))
print 'Ein_e', sum(Ein_e)/ float(len(Ein_e))
