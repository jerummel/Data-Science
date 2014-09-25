'''Project Euler Problem 46
Find the smallest odd composite that cannot be written as the sum of a prime and twice 
a square.'''

from math import sqrt

def conjecture(primeList, num):
	for p in primeList:
		if(num-p) % 2 != 0:
			continue
		else:
			square = sqrt((num-p)/2)
			if square == int(square):
				return True
	return False

def isPrime(primeList, num):
	for prime in primeList:
		if(prime > sqrt(num)):
			break
		elif(num%prime==0):
				return False
	return True

def main():
	oddComposites = []
	primes = [2, ]
	maxNum = 10000
	for num in range(3, maxNum, 2):
		if isPrime(primes, num):
			primes.append(num)
		else:
			if conjecture(primes, num) == False:
				print num
				break


if __name__ == "__main__": main()