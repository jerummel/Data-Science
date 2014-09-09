'''Project Euler Problem 9
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.'''

from math import sqrt

a = 1
b = 1
c = 1000
while(a+b+c != 1000):
	a+=1
	if a==500 or a == 1000:
		continue
	b=(1000*a-500000)/(a-1000)
	c = sqrt(a**2+b**2)
print int(a*b*c)
