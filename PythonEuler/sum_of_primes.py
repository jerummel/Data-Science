'''Project Euler Problem 10
Find the sum of all the primes below two million.'''

from math import sqrt

def isPrime(primeList, num):
	for prime in primeList:
		if prime == 2:
			continue
		elif(prime > sqrt(num)):
			break
		elif(num%prime==0):
				return False
	return True

def main():
	primes = [2, ]
	otherPrimes = []
	for num in range(3, 2000000, 2):
		if(isPrime(otherPrimes, num)):
			otherPrimes.append(num)
	primes.extend(otherPrimes)
	print sum(primes)

if __name__ == "__main__": main()