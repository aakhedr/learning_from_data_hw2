import random
import numpy as np 
from linearRegression import *
from buildDataSet import *
from nonLinearTransformation import *

data, slope, intercept = buildDataSet(N=1000)

X, y = extract(data)		# extracts X and y AND adds intercept term to X
x3 = X[:, 1] * X[:, 2]
x4 = X[:, 1]**2
x5 = X[:, 2]**2

data = np.column_stack((X, x3, x4, x5, y))
X = data[:, :-1]
y = data[:, -1]

data = simulateNoise(data=data, noise=.1)	# add 10% noise as in problem 8

# calculate the weights manually
step1 = np.linalg.pinv(np.dot(X.transpose(), X))
step2 = np.dot(step1, X.transpose())
w = np.dot(step2, y)
print w

choices = [[-1, -.05, .08, .13, 1.5, 1.5], [-1, -.05, .08, .13, 1.5, 15], 
[-1, -.05, .08, .13, 15, 1.5], [-1, -1.5, .08, .13, .05, .05], 
[-1, -.05, .08, 1.5, .15, .15]]

myG = []
mis = [[], [], [], [], []]
for i in range(1000):
	randPoint = random.choice(data)
	Xrand, yRand = randPoint[:-1], randPoint[-1]
	gEst = np.sign(np.dot(Xrand, w))
	if gEst != yRand:
		myG.append(gEst)
	for j in range(len(choices)):
		yEst = np.sign(np.dot(Xrand, choices[j]))
		if yEst != yRand:
			mis[j].append(1)

print len(myG)/ float(1000)
for alist in mis:
	print len(alist)/ float(1000)