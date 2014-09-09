'''Project Euler Problem 4
Find the largest palindrome made from the product of two 3-digit numbers.'''

from math import ceil, sqrt

def isPalindrome(numString):
	if len(numString) == 1:
		return True
	elif len(numString)%2 == 0:
		firstNum = numString[0:len(numString)/2]
		secondNum = numString[len(numString)/2:]
	else:
		breakPoint = int(ceil(len(numString)/2))
		firstNum = numString[0:breakPoint]
		secondNum = numString[breakPoint+1:]

	if(firstNum == secondNum[::-1]):
		return True
	else:
		return False

def main():
	found = False	
	for x in range(999**2, 0, -1):
		if(isPalindrome(str(x))):
			root = int(ceil(sqrt(x)))
			if(root > 1000):
				limit = 1000
			else:
				limit = root+1
			for y in range(100, limit):
				if(x%y == 0 and len(str(x/y)) == 3):
					found = True
					print x
					break
			if(found):
				break

if __name__ == "__main__": main()
