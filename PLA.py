import random
import numpy as np
from buildDataSet import buildDataSet
from linearRegression import extract, calculateWeights


def PLA(dataSet, weights):
	'''
	Runs PLA on weights obtained from Linear Regression and returns num_iters
	it takes PLA to converge
	'''	
	yEst = np.sign(np.dot(X, weights))
	iters = 0
	while len(yEst[yEst!=y]) < 0 :
		iters += 1
		diffs = yEst - y
		indices = []
		for i in range(len(diffs)):
			if diffs[i] != 0:			# indicates a misclassified point
				indices.append(i)
		index = random.choice(indices)
		weights = weights + np.dot(X[index, :].transpose(), y[index])
		yEst = np.sign(np.dot(X, w))
	return iters

# Run experiement 1000 times
num_iters = []
for i in range(1000):
	data, slope, intercept = buildDataSet(N=10)
	w = calculateWeights(data)
	X, y = extract(data)

	num_iters.append(PLA(data, w))

print 'Average num_iters = ' + str(sum(num_iters)/ float(len(num_iters)))