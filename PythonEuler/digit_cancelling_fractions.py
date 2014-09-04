'''Project Euler Problem 33
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to 
simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling 
the 9s.  There are exactly four non-trivial examples of this type of fraction, less than one in 
value, and containing two digits in the numerator and denominator.  If the product of these four 
fractions is given in its lowest common terms, find the value of the denominator.'''

from math import sqrt, floor

def findMultiples(num):
	multiples = []
	for x in range(1, int(floor(sqrt(num)))+1):
		if(num%x == 0):
			multiples.append(x)
			multiples.append(num/x)
	multiples = sorted(multiples)
	return multiples

def findNewFraction(numerator, denominator, digit):
	numerString = str(numerator)
	denomString = str(denominator)
	pos = numerString.find(str(digit))
	if(pos == 0):
		newNumerator = int(numerString[1])
	else:
		newNumerator = int(numerString[0])
	pos = denomString.find(str(digit))
	if(pos == 0):
		newDenominator = int(denomString[1])
	else:
		newDenominator = int(denomString[0])
	return newNumerator, newDenominator

def main():
	digitList = [x for x in range(1, 10)]
	numerList = []
	denomList = []
	for num in digitList:
		mult = 10*num
		firstList = [mult+digit for digit in digitList]
		secondList = [10*digit+num for digit in digitList]
		for firstNum in firstList:
			for secondNum in secondList:
				if firstNum == secondNum:
					continue
				if firstNum > secondNum:
					result1 = float(secondNum)/firstNum
					newNum, newDenom = findNewFraction(secondNum, firstNum, num)
					result2 = float(newNum)/newDenom
					if(result1 == result2):
						numerList.append(secondNum)
						denomList.append(firstNum)
				else:
					result1 = float(firstNum)/secondNum
					newNum, newDenom = findNewFraction(firstNum, secondNum, num)
					result2 = float(newNum)/newDenom
					if(result1 == result2):
						numerList.append(firstNum)
						denomList.append(secondNum)
	prodNumerator = reduce(lambda x, y: x*y, numerList)
	prodDenominator = reduce(lambda x, y: x*y, denomList)
	numerMultiples = findMultiples(prodNumerator)
	denomMultiples = findMultiples(prodDenominator)
	numerMultiples.reverse()
	denomMultiples.reverse()
	gcd = 0
	for x in numerMultiples:
		for y in denomMultiples:
			if y == x:
				gcd = x
				break
			elif y < x:
				break
		if gcd != 0:
			break
	print prodDenominator/gcd


if __name__ == "__main__": main()