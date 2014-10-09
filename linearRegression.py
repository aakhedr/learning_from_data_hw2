import random
import numpy as np 
from buildDataSet import buildDataSet

# Helper function 
def extract(dataSet):
	'''
	Extracts X and y from the data set and adds intercept term to X
	'''
	X = dataSet[:, 0:-1]
	y = dataSet[:, -1]

	interceptTerm = np.ones(shape=(X.shape[0], 1))
	X = np.column_stack((interceptTerm, X))

	return (X, y)

def calculateWeights(dataSet):
	'''
	Takes a data set of X and y in nd array and returns the weights
	base on the normal equation (w = (X' * X)^-1 * X' * y)
	'''
	X, y = extract(dataSet)

	step1 = np.linalg.pinv(np.dot(X.transpose(), X))
	step2 = np.dot(step1, X.transpose())
	weights = np.dot(step2, y)

	return weights

def calculateError(weights, dataSet):
	'''
	Based on the data set and weights, get estimates and compare to actual!
	'''
	X, y = extract(dataSet)
	yEst = np.sign(np.dot(X, weights))

	return len(yEst[yEst!=y])/ float(len(yEst))

def generateOutOfSamplePoints(N, slope, intercept):
	'''
	Generate N points according to the same g (slope and intercept).
	Returns data set of N by 3 (including y to calculate out of sample error)
	'''
	x1 = np.array([random.uniform(-1, 1) for i in range(N)])
	x2 = np.array([random.uniform(-1, 1) for i in range(N)])

	X = np.column_stack((x1, x2))

	y = np.empty(shape=(N, 1), dtype=int)
	for i in range(X.shape[0]):
		yEst = slope * X[i, 0] + intercept
		if X[i, 1] > yEst:
			y[i] = 1
		elif X[i, 1] < yEst:
			y[i] = -1
		else:
			y[i] = 0

	assert(y[y==0].shape[0] == 0)		# make sure there are no points on the line!
	dataSet = np.column_stack((X, y))

	return dataSet

# # repeat experiement 1000 times
# Ein, Eout = [], []
# for i in range(1000):
# 	# question5
# 	data, slope, intercept = buildDataSet()
# 	w = calculateWeights(data)
# 	Ein.append(calculateError(w, data))
# 	# question6
# 	outOFSampleData = generateOutOfSamplePoints(1000, slope, intercept)
# 	Eout.append(calculateError(w, outOFSampleData))

# print 'Ein = ' + str(sum(Ein)/ float(len(Ein)))
# print 'Eout = ' + str(sum(Eout)/ float(len(Eout)))

# # output
# # Ein = 0.03762
# # Eout = 0.047629