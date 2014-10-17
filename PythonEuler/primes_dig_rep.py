'''Project Euler Problem 51
Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of 
an eight prime value family.'''

class primeDigitRepeat():
	def __init__(self):
		self.repeatList = {}
		
	def hasRepeats(self, numString):
		newString = numString[:-1]
		newList = [newString.count(d) for d in newString]
		if max(newList) > 1:
			self.repeatList[numString] = set([newString[idx] for idx, appearCount in enumerate(newList) if appearCount > 1])
			return True
		else:
			return False
		
def findPrimes(Limit):	
	factors=[0]*Limit # number of prime factors.
	count=0
	for i in xrange(2,Limit):
		if factors[i]==0:
			# i is prime
			count =0
			val =i*2
			while val < Limit:
				factors[val] += 1
				val+=i
	primes = [i for i in xrange(2, len(factors)) if factors[i] == 0]
	primes = filter(lambda x: x > 57000, primes)
	primes = map(str, primes)
	return primes
	
def main():
	pList = findPrimes(1000000)
	repeats = primeDigitRepeat()
	pList = filter(lambda x: repeats.hasRepeats(x), pList)
	found = False
	for p in pList:
		for digit in repeats.repeatList[p]:
			if int(digit) > 2:
				continue
			else:
				numList = [p, ]
				for num in range(int(digit)+1, 10):
					newNum = p[:-1].replace(digit, str(num))
					newNum = '%s%s' % (newNum, p[-1])
					if newNum in pList:
						numList.append(newNum)
				if len(numList) == 8:
					print numList[0]
					print numList
					found = True
					break
		if found:
			break
	
if __name__ == "__main__":
    main()