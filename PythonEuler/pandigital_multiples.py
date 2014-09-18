'''Project Euler Problem 38
Find the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product 
of an integer with (1,2, ... , n) where n > 1

You need 9 digits in the concatenated product:
n=2:
num * 1 = 4 digits
num * 2 = 5 digits
so, 5000 <= num <= 9999

n=3:
num * 1 = 3 digits
num * 2 = 3 digits
num * 3 = 3 digits
so, 100 <= num <= 333

n=4:
num * 1 = 2 digits
num * 2 = 2 digits
num * 3 = 2 digits
num * 4 = 3 digits
so, 25 <= num <= 33

n=5:
num * 1 = 1 digit
num * 2 = 2 digits
num * 3 = 2 digits
num * 4 = 2 digits
num * 5 = 2 digits
so, 5 <= num <= 9

n=6:
num can only equal 3 and the concatenated products are not pandigital, so, ignore n>5.'''

from itertools import permutations

def isPandigitalMult(numString, n):
	numList = []
	firstDigit = 0
	digitsLeft = 9
	for i in range(n, 0, -1):
		numOfDigits = digitsLeft/i
		lastDigit = firstDigit+ numOfDigits
		numList.append(int(numString[firstDigit:lastDigit]))
		firstDigit = lastDigit
		digitsLeft -= numOfDigits
	multipleList = [numList[0]*i for i in range(1, n+1)]
	if multipleList == numList:
		return True
	else:
		return False

	

def main():
	panMult = 0
	for numberTuple in permutations(range(9, 0, -1)):
		stringTuple = map(str, numberTuple)
		numberString = ''.join(stringTuple)
		if numberTuple[0] >= 5 and numberTuple[0] <= 9:
			# check for n=2 and n=5
			if isPandigitalMult(numberString, 2) or isPandigitalMult(numberString, 5):
				panMult = int(numberString)
				break
		elif numberTuple[0] == 3:
			if numberTuple[1] >= 1 and numberTuple[1] <= 2:
				# check for n=3 and n=4
				if isPandigitalMult(numberString, 3) or isPandigitalMult(numberString, 4):
					panMult = int(numberString)
					break
			elif numberTuple[1] == 3:
				# check for n=4
				if isPandigitalMult(numberString, 4):
					panMult = int(numberString)
					break
				if numberTuple[2] >= 1 and numberTuple[2] <= 3:
					# check for n=3
					if isPandigitalMult(numberString, 3):
						panMult = int(numberString)
						break
		elif numberTuple[0] == 2:
			if numberTuple[1] >= 5 and numberTuple[1] <= 9:
				# check for n=3 and n=4
				if isPandigitalMult(numberString, 3) or isPandigitalMult(numberString, 4):
					panMult = int(numberString)
					break
			else:
				# check for n=3
				if isPandigitalMult(numberString, 3):
					panMult = int(numberString)
					break
		elif numberTuple[0] == 1:
			# check for n=3
			if isPandigitalMult(numberString, 3):
				panMult = int(numberString)
				break
	print panMult

if __name__ == "__main__": main()
