''' Project Euler Problem 26
Find the value of d < 1000 for which 1/d contains the longest recurring cycle 
in its decimal fraction part.'''

def findRecurLength(num):
	if num == 2 or num == 5:
		return 0
	else:
		x = 1
		while(10**x % num != 1):
			x += 1
		return x

def isPrime(primeList, number):
	isPrime = True
	for primeNum in primeList:
		if(number % primeNum == 0):
			isPrime = False
			break
	return isPrime

def main():
	# if d is prime, length of the recurring cycle is x where 10^x mod d = 1
	# if d is not prime, length of the recurring cycle is the same as its largest prime factor
	# therefore, we only need to look at prime numbers to find the largest recurring cycle

	primes = [2, ]
	for num in range(3, 1000):
		if(isPrime(primes, num)):
			primes.append(num)

	recurLen = {}
	for prime in primes:
		recurLen[prime] = findRecurLength(prime)
	print max(recurLen, key=lambda k: recurLen[k])


if __name__ == "__main__":
    main()