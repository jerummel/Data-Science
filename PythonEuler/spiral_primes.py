'''Project Euler Problem 58
Find the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%'''

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
		
	def addPrime(self, num):
		isPrime = True
		for prime in self.primeList:
			if prime == 2:
				continue
			elif(prime > sqrt(num)):
				break
			elif(num%prime==0):
				isPrime = False
				break
		if isPrime:
			self.primeList.append(num)

def main():
	limit = 1000000
	primeObj = Primes(limit)
	numer, denom, sideLen, level = 0, 1, 1, 0
	while float(numer)/denom >= 0.1 or numer == 0:
		sideLen += 2
		level += 1
		for multiple in range(0, 7, 2):
			diag = sideLen**2-level*multiple
			if diag >= limit:
				primeObj.addPrime(diag)
			if diag in primeObj.primeList:
				numer += 1
			denom += 1
	print sideLen
	
if __name__ == "__main__": main()