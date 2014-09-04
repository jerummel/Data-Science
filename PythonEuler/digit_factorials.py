'''Project Euler Problem 34
Find the sum of all numbers which are equal to the sum of the factorial of their digits.'''

from math import factorial

def isFactSumEqual(num):
	numString = str(num)
	factSum = 0
	for digit in numString:
		factSum += factorial(int(digit))
	return factSum == num

def main():
	# If n is a natural number of d digits that is a factorion, then
	# 10**(d-1) <= n <= 9!*d.  This fails to hold for d >= 8, thus n had at most 7 digits.
	# You need at least 2 numbers to have a sum, so n has at least 2 digits.

	numList = [num for num in range(10, 10**7)]
	digFactList = filter(lambda x: isFactSumEqual(x), numList)
	print sum(digFactList)
	

if __name__ == "__main__": main()