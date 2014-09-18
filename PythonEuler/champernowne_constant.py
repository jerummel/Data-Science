'''Project Euler Problem 40
An irrational decimal fraction is created by concatenating the positive integers: 
0.1234567891011121314151617...  If dn represents the nth digit of the fractional part, 
find the value of the following expression:
d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000'''

intList = []
num=0
while len(intList) < 1000001:
	num+=1
	numList = [int(x) for x in str(num)]
	intList.extend(numList)
print intList[0]*intList[9]*intList[99]*intList[999]*intList[9999]*intList[99999]*intList[999999]