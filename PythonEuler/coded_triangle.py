''' Project Euler Problem 42
By converting each letter in a word to a number corresponding to its alphabetical position 
and adding these values we form a word value.  A sequence of triangle numbers is given by
tn = 0.5*n*(n+1).  Using coded_triangle_words.txt, a 16K text file containing nearly 
two-thousand common English words, find how many are triangle words.'''

def findWordValues(word):
	# all characers are upper case, so subtract 64 from their ascii to get the value of the letter
	wordNums = [ord(c)-64 for c in word]
	return sum(wordNums)

def main():
	infile = open('coded_triangle_words.txt')
	words = []
	maxLen = 0
	for line in infile:
		line = line.strip()
		lineList = line.split(',')
		for i, word in enumerate(lineList):
			word = word.strip('"')
			lineList[i] = word
			if len(word) > maxLen:
				maxLen = len(word)
		words.extend(lineList)
	# the upper bound is the highest possible word value, which would be if the longest word had all Z's as letters	
	upperBound = 26*maxLen
	triNums = []
	n = 1
	while(0.5*n*(n+1) <= upperBound):
		triNums.append(0.5*n*(n+1))
		n+=1
	wordValues = map(lambda x: findWordValues(x), words)
	triValues = filter(lambda x: x in triNums, wordValues)
	print len(triValues)

if __name__ == "__main__":
    main()