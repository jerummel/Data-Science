'''Project Euler Problem 39
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are 
exactly three solutions for p = 120: {20,48,52}, {24,45,51}, {30,40,50}
Find which value of p <= 1000 that the number of solutions is maximised.'''

from collections import Counter
from math import sqrt

squares = [x**2 for x in range(1, 1001)]
p = []
for aSquared in squares:
	count = 0
	for bSquared in squares:
		cSquared = aSquared + bSquared
		if sqrt(aSquared) + sqrt(bSquared) + sqrt(cSquared) > 1000:
			break
		count+=1
		if cSquared in squares:
			p.append(int(sqrt(aSquared) + sqrt(bSquared) + sqrt(cSquared)))

	if count == 0:
		break
maxP = Counter(p).most_common(1)
print maxP[0][0]