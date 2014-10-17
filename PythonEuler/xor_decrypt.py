'''Project Euler Problem 59
A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, 
taken from a secret key.  The encryption key for this problme consists of three lower case characters.  Using cipher.txt
a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, 
decrypt the message and find the sum of the ASCII values in the original text'''

from itertools import product

def xor(ascii1, ascii2):
	binString1, binString2 = bin(ascii1)[2:], bin(ascii2)[2:]
	lenDiff = abs(len(binString1) - len(binString2))
	if lenDiff > 0:
		if len(binString1) > len(binString2):
			binString2 = ''.join(['0' for x in range(lenDiff)]) + binString2
		else:
			binString1 = ''.join(['0' for x in range(lenDiff)]) + binString1
	newString = ''
	for idx, bit in enumerate(binString1):
		if bit == binString2[idx]:
			newString = newString + '0'
		else:
			newString = newString + '1'
	return int(newString, 2)

def decrypt(cipher, perm, limit):
		idx = 0
		for c in cipher[:limit]:
			if idx == 3:
				idx = 0
			yield c, perm[idx]
			idx += 1
			
def main():
	wordfile = open('xor_wordsEn.txt')
	englishList = [word.strip() for word in wordfile]
	wordLen = map(lambda x: len(x), englishList)
	maxLen = max(wordLen)
	cipherfile = open('xor_cipher.txt')
	cipher = []
	for c in cipherfile:
		c = c.strip()
		cList = c.split(',')
		cipher.extend(cList)
	cipher = map(int, cipher)
	for permTuple in product(range(97, 123), repeat=3):
		# we don't want to convert the whole cipher until we find the right one for efficiency's sake
		# use maxLen * 3 as the limit so that decryptList should contain at least 3 words (and 2 spaces in between)
		decryptList = [str(unichr(xor(byte, key))).lower() for byte, key in decrypt(cipher, permTuple, maxLen*3 + 2)]
		d = ''.join(decryptList)
		wordList = d.split(' ')
		# if it does not contain at least 3 words, then permTuple is not the right password
		if len(wordList) < 3:
			continue
		wordCount = 0
		englishCount = 0
		for word in wordList:
			newWord = ''.join([w for w in word if (w >= 'A' and w <= 'Z') or (w >= 'a' and w <= 'z')])
			# newWord will be blank if the word is completely made up of non-letters, so skip it.
			if newWord in englishList:
				englishCount += 1
			wordCount += 1
		# if at least 2/3 are legitimate English words, then we've likely found the password
		# (you could have proper names, which are legitimate words that would not be in the englishList, hence why I used 2/3 and not 100%)
		if float(englishCount)/wordCount > 0.66:
			break
	decryptList = [xor(byte, key) for byte, key in decrypt(cipher, permTuple, len(cipher))]
	print sum(decryptList)
		
if __name__ == "__main__": main()