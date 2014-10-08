import random, pylab
import numpy as np

def plotDataSet(data, slope, intercept):
	''' 
	data consists of:
	X is an nd array of N by 2.
	y is an nd array of N by 1 (taking on values of either 1 or -1).
	Boundary line identified by slope and y intercept.
	'''
	Xplus = data[data[:, 2]==1]
	Xminus = data[data[:, 2]==-1]

	y1 = slope * -1 + intercept 
	y2 = slope * 1 + intercept
	
	pylab.plot(Xplus[:, 0], Xplus[:, 1], 'co', label='+1')
	pylab.plot(Xminus[:, 0], Xminus[:, 1], 'mo', label='-1')
	pylab.plot([-1, 1], [y1, y2], 'k-')
	pylab.xlabel('x1')
	pylab.ylabel('x2')
	pylab.legend(loc='best')
	pylab.show()

def buildDataSet(N=100):
	'''
	Construct a 3 column data set with N rows of floats choisen at random
	from the interval [-1, 1] as follow:
	x1=column1 - x2=column2 - y=column3=values of either (-1) or (+1).
	Also constructs a line separating points(y=-1) from points(y=-1).
	Returns the data set, line slope, line y intercept.
	'''
	x1, x2 = np.ndarray(shape=(N, 1)), np.ndarray(shape=(N, 1))
	for i in range(N):
		x1[i, 0] = random.uniform(-1, 1)
		x2[i, 0] = random.uniform(-1, 1)

	X = np.column_stack((x1, x2))
	pointsX, pointsY = np.ndarray(shape=(2, 1)), np.ndarray(shape=(2, 1))
	for i in range(2):
		pointsX[i, 0] = random.uniform(-1, 1)
		pointsY[i, 0] = random.uniform(-1, 1)

	# y = ax + b

	slope = (float(pointsY[1, 0]) - float(pointsY[0, 0]))/ (float(pointsX[1, 0]) - float(pointsX[0, 0]))
	yIntercept = float(pointsY[1, 0]) - (slope * float(pointsX[1, 0]))

	y = np.ndarray(shape=(N, 1), dtype=int)
	for i in range(X.shape[0]):
		yEst = slope * float(X[i, 0]) + yIntercept
		if float(X[i, 1]) > yEst:
			y[i] = 1
		elif float(X[i, 1]) < yEst:
			y[i] = -1
		else:
			y[i] = 0

	assert(y[y==0].shape[0] == 0)		# make sure there are no points on the line!
	data = np.column_stack((X, y))

	return(data, slope, yIntercept)

# dataSet, lineSlope, lineYintercept = buildDataSet()
# plotDataSet(dataSet, lineSlope, lineYintercept)
