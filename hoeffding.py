import random

# Helper function 1
def flip():
	''' flip one coin '''
	return random.choice(['H', 'T'])

def flipCoins(numCoins=1000):
	''' flip numCoins coins 10 times each and return res per coin '''
	res = []
	for i in range(numCoins):
		aCoin = []
		for j in range(10):		# flip each coin 10 times
			aCoin.append(flip())
		res.append(aCoin)
	return res

# Helper function 2
def countH(aCoin):
	counter = 0
	for i in range(len(aCoin)):
		if aCoin[i] == 'H':
			counter += 1
	return counter

# Helper function 3
def minHeads(allCoins):
	numHeads = 10 				# max num heads per coin
	coinIndex = 0
	for i in range(len(allCoins)):
		freqOfH = countH(allCoins[i])
		if freqOfH < numHeads:
			numHeads = freqOfH
			coinIndex = i
	return coinIndex

def pick3(allCoins):
	c1 = allCoins[0]
	cRand = random.choice(allCoins)
	minIndex = minHeads(allCoins)
	cMin = allCoins[minIndex]
	nu1 = countH(c1) / float(len(c1))
	nuRand = countH(cRand) / float(len(cRand))
	nuMin = countH(cMin) / float(len(cMin))
	return [(c1, nu1), (cRand, nuRand), (cMin, nuMin)]

