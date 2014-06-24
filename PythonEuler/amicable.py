''' Project Euler Problem 21
If the sum of all divisors of a equals b and the sum of all divisors of b equals a and a != b, then a and b
are amicable.  Evaluate the sum of all the amicable numbers under 10000.'''

from math import sqrt

def main():
	resultList = []
	for i in range(1, 10000):
		if(resultList.count(i) > 0):
			continue
		divSum = findDivisorSum(i)
		if(i == divSum or divSum >= 10000):
			continue
		divSum2 = findDivisorSum(divSum)
		if(i == divSum2):
			resultList.append(i)
			resultList.append(divSum)
	print sum(resultList)
	
def findDivisorSum(numerator):
	maxRange = int(sqrt(numerator)) + 1
	divList = [num for num in range(1, maxRange) if numerator%num == 0]
	secHalf = [numerator/num for num in divList if num != 1 and num != sqrt(numerator)]
	secHalf.reverse()
	divList.extend(secHalf)
	return sum(divList)
	
if __name__ == "__main__":
    main()