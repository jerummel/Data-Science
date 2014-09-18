'''Proiect Euler Problem 45
At n=285, the triangle, pentagonal, and hexagonal number sequences all have the same value,
40755.  Find the next triangle number that is also pentagonal and hexagonal.'''

upperBound = 100000
tri = [n*(n+1)/2 for n in range(286, upperBound)]
pent = [n*(3*n-1)/2 for n in range(286, upperBound)]
hexa = [n*(2*n-1) for n in range(286, upperBound)]
for T in tri:
	if T in pent and T in hexa:
		print T
		break
