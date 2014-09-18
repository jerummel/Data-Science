'''Project Euler Problem 41
Find the largest n-digit pandigital prime that exists'''

from itertools import permutations
from math import sqrt

def isPrime(primeList, num):
	for prime in primeList:
		if(prime > sqrt(num)):
			break
		elif(num%prime==0):
				return False
	return True

def main():
	primes = [2, ]
	otherPrimes = []
	for num in range(3, int(sqrt(987654321)), 2): # 987654321 is the largest pandigital number
		if isPrime(otherPrimes, num):
			otherPrimes.append(num)
	primes.extend(otherPrimes)
	foundPrime = False
	for highDigit in range(9, 0, -1):
		for permTuple in permutations(range(highDigit, 0, -1)):
			stringTuple = map(str, permTuple)
			permString = ''.join(stringTuple)
			perm = int(permString)
			if isPrime(primes, perm):
				print perm
				foundPrime = True
				break
		if foundPrime:
			break

if __name__ == "__main__": main()