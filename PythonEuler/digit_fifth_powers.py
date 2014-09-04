'''Project Euler Problem 30
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.'''

from itertools import product
resultList = []
for prodTuple in product(range(10), repeat=6):  #probably don't have to go higher than 6 digits
	for idx, digit in enumerate(prodTuple):
		if digit != 0:
			break
	if idx > 2:
		continue #only look at 4 digit numbers or larger
	digitList = prodTuple[idx:]
	powerList = [x**5 for x in digitList]
	powerSum = sum(powerList)
	digitStringList = [str(x) for x in digitList]
	numberString = ''.join(digitStringList)
	number = int(numberString)
	if(powerSum == number):
		resultList.append(number)
print sum(resultList)