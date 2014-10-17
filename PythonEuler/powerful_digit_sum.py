'''Project Euler Problem 56
Considering natural numbers of the form, a**b, where a, b < 100, find the maximum digital sum.'''

def findDigitSum(num):
	numString = str(num)
	digitList = [int(x) for x in numString]
	return sum(digitList)
		
def main():
	maxSum = 0
	# the greatest digit sum of 1**b will be 1
	# the greatest digit sum of a**1 will be 18 (99**1 = 99)
	# since both of those numbers are small, we can assume the maxSum will be much greater
	# so start a and b at 2
	for a in range(2, 100):
		# if a is divisble by ten, it was already checked when single digits were checked
		# ex. 5**2 = 25, 50**2 = 2500, both have digit sum of 7
		if a%10 == 0:
			continue
		for b in range(2, 100):
			thisSum = findDigitSum(a**b)
			if thisSum > maxSum:
				maxSum = thisSum
	print maxSum
			
if __name__ == "__main__":
	main()