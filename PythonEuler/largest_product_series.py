'''Project Euler Problem 8
Find the thirteen adjacent digits in the 1000-digit number that have the greatest product and
return that product'''

f = open('largest_product_series.txt')
numList = []
for line in f:
	line = line.strip()
	lineList = [int(x) for x in line]
	numList.extend(lineList)
prodList = [reduce(lambda x, y: x*y, numList[maxIdx-13:maxIdx]) for maxIdx in range(13, len(numList))]
print max(prodList)
