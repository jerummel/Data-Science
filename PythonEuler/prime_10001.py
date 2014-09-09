'''Project Euler Problem 7
Find the 10 001st prime number'''

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
	prime = [2, ]
	i = 1
	while len(prime) < 10001:
		i += 2
		if(isPrime(prime, i)):
			prime.append(i)
	print prime[len(prime)-1]

if __name__ == "__main__": main()