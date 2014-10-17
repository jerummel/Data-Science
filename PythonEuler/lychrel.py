'''Project Euler Problem 55
Find how many Lychrel numbers are there below ten-thousand'''

def reverseNum(num):
	numString = str(num)
	return numString[::-1]

def isPalindrome(num):
	if int(reverseNum(num)) == num:
		return True
	else:
		return False
		
def main():
	lychrel = 0
	for i in xrange(1, 10000):
		found = False
		newNum = i
		for j in range(50):
			newNumRev = int(reverseNum(newNum))
			if isPalindrome(newNum+newNumRev):
				found = True
				break
			newNum += newNumRev
		if not found:
			lychrel += 1
	print lychrel
			
if __name__ == "__main__":
	main()