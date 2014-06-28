''' Project Euler Problem 24
Permutations listed in numeric order are called lexographic.  Find the 1 millionth lexographic
permutation of 0, 1, 2, 3, 4, 5, 6, 7, 8, 9'''

from itertools import permutations

def main():
	i=0
	for permTuple in permutations(range(10)):
		i += 1
		if(i==1000000):
			break
	print permTuple

if __name__ == "__main__":
    main()