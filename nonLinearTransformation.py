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
		indices = []
		index = random.randint(0, len(data) - 1)
		if index not in indices:
			indices.append(index)
			if data[index, -1] == 1:
				data[index, -1] = -1
			else:
				data[index, -1] = 1
	return data

def addFeatures(dataSet):
	'''
	Add more features as per spec of question9
	*** Use after the intercept term is added ***
	'''
	X, y = extract(data)
	x3 = X[:, 1] * X[:, 2]
	x4 = X[:, 1]**2
	x5 = X[:, 2]**2
	dataSet = np.column_stack((X, x3, x4, x5, y))
	return dataSet

def pickRandomPoints(dataSet):
	'''
	For use in problem9
	Picks and returns a subset of 100 points of the dataSet randomly
	'''
	return np.array([random.choice(dataSet) for i in range(100)])

# question8
data, slope, intercept = buildDataSet(N=1000)
data = addIntercept(data)
# Ein = []
# for i in range(1000):
# 	data = simulateNoise(data=data, noise=.1)
# 	w = calculateWeights(data)
# 	Ein.append(calculateError(w, data))

# print sum(Ein)/ float(len(Ein))

# question9 
data = addFeatures(data)
data = simulateNoise(data=data, noise=.1)
w = calculateWeights(data)

choices = [[-1, -.05, .08, .13, 1.5, 1.5], 
[-1, -.05, .08, .13, 1.5, 15], 
[-1, -.05, .08, .13, 15, 1.5], 
[-1, -1.5, .08, .13, .05, .05], 
[-1, -.05, .08, 1.5, .15, .15]]
choices = [np.array(choices[i]) for i in range(len(choices))]

Ein_w, Ein_a, Ein_b, Ein_c, Ein_d, Ein_e = [], [], [], [], [], []
iters = 1
for i in range(iters):
	# 100 random points
	subset = pickRandomPoints(data)

	Ein_w.append(calculateError(w, subset))
	Ein_a.append(calculateError(choices[0], subset))
	Ein_b.append(calculateError(choices[1], subset))
	Ein_c.append(calculateError(choices[2], subset))
	Ein_d.append(calculateError(choices[3], subset))
	Ein_e.append(calculateError(choices[4], subset))

print 'Ein_w', sum(Ein_w)/ float(iters)
print
print 'Ein_a', sum(Ein_a)/ float(iters)
print 'Ein_b', sum(Ein_b)/ float(iters)
print 'Ein_c', sum(Ein_c)/ float(iters)
print 'Ein_d', sum(Ein_d)/ float(iters)
print 'Ein_e', sum(Ein_e)/ float(iters)

# # problem10
# w = calculateWeights(data)

# outOfSample = generateOutOfSamplePoints(1000, slope, intercept)
# outOfSample = addIntercept(outOfSample)
# # outOfSample = addFeatures(outOfSample)	# check function!

# X, y = extract(outOfSample)
# x3 = X[:, 1] * X[:, 2]
# x4 = X[:, 1]**2
# x5 = X[:, 2]**2
# outOfSample = np.column_stack((X, x3, x4, x5, y))
# outOfSample = simulateNoise(outOfSample)

# Eout, Ein = [], []
# for i in range(1000):
# 	Ein.append(calculateError(w, data))
# 	Eout.append(calculateError(w, outOfSample))

# print 'Ein ', sum(Ein)/ float(1000)
# print 'Eout ', sum(Eout)/ float(1000)

