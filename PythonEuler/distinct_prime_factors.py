'''Project Euler Problem 47
Find the first four consecutive integers to have four distinct prime factors. 
Output the first of these numbers.'''

from math import sqrt

class Prime:
		
	def primes(self, maxNum):
		primeList = [2, ]
		if maxNum < 4:
			return primeList
		for num in range(3, maxNum, 2):
			isPrime = True
			for p in primeList:
				if p > int(sqrt(num)):
					break
				if num%p == 0:
					isPrime = False
					break
			if(isPrime):
				primeList.append(num)
		return primeList
		
primeObj = Prime()
pList = primeObj.primes(1000000)
firstNum = 2*3*5*7
consec = 1
for num in xrange(firstNum+1, 1000000):
	if num in pList:
		consec = 0
	else:
		factors = 0
		newNum = num
		for p in pList:
			if newNum % p == 0:
				while newNum%p == 0:
					newNum /= p
				factors += 1
				if newNum in pList:
					factors += 1
					break
		if factors == 4:
			consec += 1
		else:
			consec = 0
	if consec == 4:
		break
print num-3 # Runs in 491s