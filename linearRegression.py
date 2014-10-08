import numpy as np 
from buildDataSet import buildDataSet

# Helper function 
def extract(dataSet):
	'''
	Extracts X and y from the data set and adds intercept term to X
	'''
	X = dataSet[:, 0:2]
	y = dataSet[:, 2]
	
	interceptTerm = np.ones(shape=(X.shape[0], 1))
	X = np.column_stack((X, interceptTerm))

	return (X, y)

def calculateWeights(dataSet):
	'''
	Takes a data set of X and y in nd array and returns the weights
	base on the normal equation (w = pinv(X' * X) * X' * y)
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

# repeat experiement 1000 times
Ein = []
for i in range(1000):
	data, slope, intercept = buildDataSet()
	w = calculateWeights(data)
	Ein.append(calculateError(w, data))

print sum(Ein)/ float(len(Ein))

