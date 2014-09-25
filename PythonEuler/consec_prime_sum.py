'''Project Euler Problem 50
Find which prime, below one-million, that can be written as the sum of the most consecutive 
primes.'''

def getPrimeList(Limit):
	factors=[0]*Limit # number of prime factors.
	count=0
	for i in xrange(2,Limit):
	    if factors[i]==0:
	        # i is prime
	        count =0
	        val =i*2
	        while val < Limit:
	            factors[val] += 1
	            val+=i
	return [i for i in xrange(2, len(factors)) if factors[i] == 0]


def main():
	maxList, limit = [], 1000000
	pList = getPrimeList(limit)
	for idx, p in enumerate(pList):
		if p > limit/2:
			break
		newList, pSum = [], 0
		for i in range(idx, len(pList)):
			pSum += pList[i]
			if pSum > limit:
				break
			else:
				newList.append(pList[i])
		if len(newList) < len(maxList):
			break
		while len(newList) > len(maxList):
			if sum(newList) in pList:
				maxList = newList
				break
			else:
				newList.pop()
	print sum(maxList)

if __name__ == "__main__":
    main()