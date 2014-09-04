'''Project Euler Problem 32
Find the sum of all products whose multiplicand/multiplier/product identity can be written 
as a 1 through 9 pandigital'''

from itertools import permutations

def convertToNumber(numList):
	strList = map(str, numList)
	return int(''.join(strList))

def findEquationParts(m1Len, m2Len, numTuple):
	m1List = numTuple[0:m1Len]
	m1 = convertToNumber(m1List)
	m2List = numTuple[m1Len:m1Len+m2Len]
	m2 = convertToNumber(m2List)
	m3List = numTuple[m1Len+m2Len:]
	m3 = convertToNumber(m3List)
	return m1, m2, m3

def main():
	prodList = []
	for permTuple in permutations(range(1, 10)):
		# there are only 2 combinations of numbers that will work:
		# 1 digit number * 4 digit number can equal a 4 digit number
		# 2 digit number * 3 digit number can equal a 4 digit number
		for lenTuple in ((1, 4), (2, 3)):
			multiplicand, multiplier, product = findEquationParts(lenTuple[0], lenTuple[1], permTuple)
			if(multiplicand * multiplier == product):
				prodList.append(product)
	prodSet = set(prodList) # take all duplicates out of the product list
	print sum(prodSet)

if __name__ == "__main__":
    main()