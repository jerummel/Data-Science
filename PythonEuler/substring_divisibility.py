'''Project Euler Problem 43
Find the sum of all 0 to 9 pandigital numbers with this property with the property:
Let d1 be the first digit, d2 the second, etc.
d2d3d4 are divisible by 2
d3d4d5 are divisible by 3
d4d5d6 are divisible by 5
d5d6d7 are divisible by 7
d6d7d8 are divisible 11
d7d8d9 are divisible by 13
d8d9d10 are divisible by 17'''

from itertools import permutations

primes = (2, 3, 5, 7, 11, 13, 17)
numsWithProp = []
for permTuple in permutations(range(0, 10)):
	numString = ''.join(map(str, permTuple))
	hasProperty = True
	for d in range(1, 8):
		if(int(numString[d:d+3])%primes[d-1] != 0):
			hasProperty = False
			break
	if(hasProperty):
		numsWithProp.append(int(numString))
print sum(numsWithProp)