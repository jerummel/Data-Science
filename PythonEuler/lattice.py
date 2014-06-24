'''Project Euler Problem 15
Starting in the top left corner of a 20×20 grid, and only being able to move to the right and down,
how many routes are there to the bottom right corner.'''

# A 20 x 20 lattice will actually have 21 rows and columns
maxRange = 21
prevRow = [1 for i in range(maxRange)]

# We already have the first prevRow, so the loop should run through maxRange-1 iterations
for rowNum in range(maxRange-1):
	thisRow = [1, ]
	for i in range(1, maxRange):
		numPaths = thisRow[i-1] + prevRow[i]
		thisRow.append(numPaths)
	prevRow = thisRow
	
print prevRow[maxRange-1]