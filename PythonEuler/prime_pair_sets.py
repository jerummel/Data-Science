'''Project Euler Problem 60
Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.'''

from math import sqrt

class Primes():
	def __init__(self, Limit):
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
		self.primeList = [i for i in xrange(2, len(factors)) if factors[i] == 0]
		
	def isPrime(self, num):
		for prime in self.primeList:
			if prime == 2:
				continue
			elif(prime > sqrt(num)):
				break
			elif(num%prime==0):
				return False
		return True

def maxLength(Object, limit):
	for idx, p in enumerate(Object.primeList):
		if p >= limit:
			break
	return idx

def prime(obj, num, limit):
		if num < limit:
			return num in obj.primeList
		else:
			return obj.isPrime(num)
			
def initializeDict(pList):
	newDict = {}
	for p in pList:
		newDict[p] = []
	return newDict

def main():
	primeLimit = 1000000
	primeObj = Primes(primeLimit)
	# I'm guessing all of the numbers in the answer will be less than 10000
	solutionLimit = 10000
	maxLen = maxLength(primeObj, solutionLimit)
	pList = primeObj.primeList[1:maxLen] #primeList[0] == 2. Concatenating a 2 at the end of any number will never yield a prime, so skip 2.
	pList.remove(5) #Concatenating a 5 at the end of any number will never yield a prime, so skip 5.
	pairDict = initializeDict(pList)
	for idx, p in enumerate(pList):
		if idx == len(pList)-1:
			break
		for i in range(idx+1, len(pList)):
			# if the first one is not prime, there is no need to check the second, hence why I did not do an 'and' here
			if prime(primeObj, int(str(p) + str(pList[i])), primeLimit):
				if prime(primeObj, int(str(pList[i]) + str(p)), primeLimit):
					pairDict[p].append(pList[i])
	found = False
	for p in pList:
		for otherp in pairDict[p]:
			M = 3
			result = [p,]
			nextNum = otherp
			newList = pairDict[p]
			while not found:
				intersection = list(set(newList) & set(pairDict[nextNum]))
				if len(intersection) >= M:
					result.append(nextNum)
					newList = intersection
					nextNum = min(intersection)
					if M == 1:
						result.append(nextNum)
						found = True
					else:
						M -= 1
				else:
					break
			if found:
				break
		if found:
			break
	print result
	print sum(result)
	
if __name__ == "__main__": main()