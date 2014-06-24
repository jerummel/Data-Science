'''Project Euler Problem 23
If the sum of a numbers divisors exceeds the number, that number is called abundant. 
By mathematical analysis, it can be shown that all integers greater than 28123 can be written 
as the sum of two abundant numbers.  Find the sum of all the positive integers which cannot be 
written as the sum of two abundant numbers'''

from amicable import findDivisorSum

def main():
	# smallest abundant number is 12, all numbers above 28123 are the sum of 2 abundants, so we
	# don't need to go above 28123
	abundantNumList = [n for n in range(12, 28124) if n < findDivisorSum(n)]
	# the smallest sum of abundants is 12 + 12 = 24, so anything less is not a sum of abundants
	notSumOfAbundants = [n for n in range(1, 24)]
	found = False
	for n in range(25, 28124):
		for abundant in abundantNumList:
			if abundant > n or abundant > 28124/2:
				break
			elif(n-abundant in abundantNumList):
				found = True
				break
		if(found == False):
			notSumOfAbundants.append(n)
		else:
			found = False
	print sum(notSumOfAbundants)

if __name__ == "__main__": main()