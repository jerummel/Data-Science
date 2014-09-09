'''Project Euler Problem 1
Find the sum of all the multiples of 3 or 5 below 1000.'''

mults = [x for x in range(3, 1000, 3)]
fives = [x for x in range(5, 1000, 5)]
mults.extend(fives)
multSet = set(mults)
print sum(multSet)