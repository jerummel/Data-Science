'''Project Euler Problem 35
Find how many circular primes there are below one million.'''

from math import sqrt

def isPrime(primeList, num):
	for prime in primeList:
		if(prime > sqrt(num)):
			break
		elif(num%prime==0):
				return False
	return True

def alreadyChecked(numString):
	if(numString[0] == '1'):
		return False
	else:
		for i in range(1, int(numString[0])):
			if str(i) in numString:
				return True
	return False

def main():
	primes = [2, ]
	otherPrimes = []
	for num in range(3, 10**6, 2):
		if(isPrime(otherPrimes, num)):
			otherPrimes.append(num)
	primes.extend(otherPrimes)
	circularList = []
	i=0
	while i < len(primes):
		prime = primes[i]
		circulars = [prime, ]
		newString = str(prime)
		if(alreadyChecked(newString)):
			i+=1
			continue
		lastIdx = len(newString)-1
		if lastIdx == 0:
			circularList.extend(circulars)
			i+=1
			continue
		allPrimes = True
		for primeIdx in range(lastIdx):
			newString = "%s%s" % (newString[lastIdx], newString[0:lastIdx])
			if int(newString) not in circulars:
				if int(newString) in primes:
					primes.remove(int(newString))
				else:
					allPrimes = False
				circulars.append(int(newString))
			else:
				break
		if allPrimes:
			circularList.extend(circulars)	
		i+= 1
	print len(circularList)
			
	
if __name__ == "__main__": main()