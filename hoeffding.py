import random

def flip():
	''' flip one coic '''
	return random.choice(['H', 'T'])

def flip1000(numCoins=1000):
	''' flip numCoins coins and return res per coin '''
	res, aCoin = [], []
	for i in range(numCoins):
		for j in range(10):
			aCoin.append(flip())
		res.append(aCoin)
	return res

def pick3(listOfLists):
	c1 = listOfLists[0]
	cRand = random.choice(listOfLists)
	cMin = 

	return (c1, cRand, cMin)