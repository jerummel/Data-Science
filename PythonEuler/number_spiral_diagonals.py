'''Project Euler Problem 28
It can be verified that the sum of the numbers on the diagonals of a 5x5 number spiral is 101.
Find the sum of the numbers on the diagonals in a 1001 by 1001 spiral.'''

# Find the squares
squares = [x**2 for x in range(3, 1002, 2)]

diagonalSum = 1 #starts with the value of the center of the number spiral
for idx, square in enumerate(squares):
	idx += 1
	for multiple in range(0, 7, 2):
		diagonalSum += square - idx * multiple
print diagonalSum