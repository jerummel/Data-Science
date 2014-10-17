'''Project Euler Problem 52
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.'''

from math import floor
from collections import Counter

def countDigits(numString):
	cnt = Counter()
	for digit in numString:
		cnt[digit] += 1
	return cnt
		
def main():
	found = False
	n=4
	while not found:
		upper = int(floor(10**n/6.0) + 1)
		for i in range(10**(n-1), upper):
			numString = str(i)
			digitCount = countDigits(numString)
			resultList = [i, ]
			for x in range(2, 7):
				newString = str(i*x)
				newDigitCount = countDigits(newString)
				if newDigitCount != digitCount:
					break
				else:
					resultList.append(i*x)
			if len(resultList) == 6:
				print resultList[0]
				print resultList
				found = True
				break
		n+=1
			
	
if __name__ == "__main__":
    main()