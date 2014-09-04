'''Project Euler Problem 37
Find the sum of the only eleven primes that are both truncatable from left to right and 
right to left.'''

from math import sqrt

def isPrime(primeList, num):
	for prime in primeList:
		if(prime > sqrt(num)):
			break
		elif(num%prime==0):
				return False
	return True

def isRightTruncatable(primeList, num):
	numString = str(num)
	while len(numString) > 1:
		numString = numString[0:len(numString)-1]
		if int(numString) not in primeList:
			return False
	return True

def isLeftTruncatable(primeList, num):
	numString = str(num)
	while len(numString) > 1:
		numString = numString[1:]
		if int(numString) not in primeList:
			return False
	return True

def main():
	truncPrimes = []
	primes = []
	i=2
	while(len(truncPrimes) < 11):
		if(isPrime(primes, i)):
			if(i>7):
				if isLeftTruncatable(primes, i):
					if isRightTruncatable(primes, i):
						truncPrimes.append(i)
			primes.append(i)
		if(i==2):
			i+=1
		else:
			i+=2

	print sum(truncPrimes)

			
	
if __name__ == "__main__": main()