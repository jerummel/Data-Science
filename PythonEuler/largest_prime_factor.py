'''Project Euler Problem 3
Find the largest prime factor of the number 600851475143 '''

from math import sqrt, ceil

def main():	
	num = 600851475143
	sNum = int(ceil(sqrt(num)))
	# 600851475143 is an odd number, so 2 is not a factor.  Start with 3.
	factors = [x for x in range(3, sNum, 2) if num%x == 0]
	highestFactors = map(lambda x: num/x, factors)
	factors.reverse()
	highestFactors.extend(factors)
	for f in highestFactors:
		prime = True
		factorRoot = int(ceil(sqrt(f)))
		for x in range(2, factorRoot):
			if(f%x == 0):
				prime = False
				break
		if(prime):
			print f
			break

if __name__ == "__main__": main()
