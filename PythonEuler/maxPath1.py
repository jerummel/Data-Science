'''Project Euler Problem 18
By starting at the top of the triangle in maxPath1.txt and moving to adjacent numbers on the 
row below, find the maximum total from top to bottom.'''

maxSum = 0

def main():
	global maxSum
	triangle = []
	fh = open('maxPath1.txt')
	for line in fh:
		line = line.rstrip('\n')
		row = line.split(' ',)
		triangle.append([int(num) for num in row])
	findMaxSum(1, 0, triangle[0][0], triangle)
	print maxSum

def findMaxSum(rowNum, colNum, oldSum, triangle):
	global maxSum
	thisSum = oldSum + triangle[rowNum][colNum]
	if(rowNum == len(triangle)-1):
		if(thisSum > maxSum):
			maxSum = thisSum
	else:
		findMaxSum(rowNum+1, colNum, thisSum, triangle)
		if(rowNum < len(triangle)-2):
			thisSum = oldSum + triangle[rowNum][colNum+1]
		findMaxSum(rowNum+1, colNum+1, thisSum, triangle)

if __name__ == "__main__": main()