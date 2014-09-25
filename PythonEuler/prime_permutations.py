'''Project Euler Problem 49
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, 
is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 
4-digit numbers are permutations of one another.  There are no arithmetic sequences 
made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is 
one other 4-digit increasing sequence.  Find the 12-digit number you form by 
concatenating the three terms in this sequence'''

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

def isPermutation(firstNum, secondNum):
			secondNumList = [c for c in secondNum if c in firstNum]
			if ''.join(secondNumList) == secondNum:
				return True
			else:
				return False

def main():
	pList = getPrimeList(9877)
	pList = filter(lambda x: x > 999, pList)
	for p in pList:
		firstPrime, ppList = str(p), []
		if p == 1487:
			continue
		ppList.append(firstPrime)
		secondPrime = p + 3330
		if secondPrime in pList and isPermutation(str(firstPrime), str(secondPrime)):
			ppList.append(str(secondPrime))
			thirdPrime = secondPrime + 3330
			if thirdPrime in pList and isPermutation(str(secondPrime), str(thirdPrime)):
				ppList.append(str(thirdPrime))
				break
	print ''.join(ppList)			


if __name__ == "__main__":
    main()