'''Project Euler Problem 57
sqrt(2) = 1 + 1/((2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
In the first one-thousand expansions, find how many fractions contain a numerator with more digits than denominator'''

def numOfDigits(num):
	return len(str(num))
	
def main():
	fraction=[1, 2] # fraction[0] = numerator, fraction[1] = denominator
	# the first expansion is 1+1/2 = 3/2, in which numerator and denominator have same number of digits
	expansion = 1
	count = 0
	while expansion < 1000:
		fraction[0] += 2*fraction[1]
		fraction.reverse()
		if numOfDigits(fraction[0]+fraction[1]) > numOfDigits(fraction[1]):
			count += 1
		expansion += 1
	print count
		
if __name__ == "__main__":
	main()