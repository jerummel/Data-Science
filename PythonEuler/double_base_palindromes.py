'''Project Euler Problem 36
Find the sum of all numbers, less than one million, which are palindromic in base 10 and 
base 2.'''

from math import ceil

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
	palinList = []
	for num in range(1, 10**6):
		numString = str(num)
		binaryNum = bin(num)
		binaryString = str(binaryNum)[2:]
		if(isPalindrome(numString) and isPalindrome(binaryString)):
			palinList.append(num)
	print palinList
			
	
if __name__ == "__main__": main()