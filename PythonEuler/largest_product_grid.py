'''Project Euler Problem 11
Find the greatest product of four adjacent numbers in the same direction (up, down, left, 
right, or diagonally) in a 20x20 grid'''

f = open('largest_product_grid.txt')
grid = []
for line in f:
	line.strip()
	row = line.split(' ')
	grid.append(map(int, row))
maxCols = len(grid[0])
maxRows = len(grid)
prodList = []
for i in range(maxRows):
	for j in range(maxCols):
		# horizontal products
		if j+3<maxCols:
			prodList.append(grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3])
		# vertical products
		if i+3<maxRows:
			prodList.append(grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j])
		# diagonal products
		if i+3<maxRows:
			# left to right diagonal products
			if j+3<maxCols:
				prodList.append(grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3])
			# right to left diagonal products
			if j-3 > -1:
				prodList.append(grid[i][j]*grid[i+1][j-1]*grid[i+2][j-2]*grid[i+3][j-3])
print max(prodList)

