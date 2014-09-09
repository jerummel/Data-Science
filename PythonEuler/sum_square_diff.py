'''Project Euler Problem 6
Find the difference between the sum of the squares of the first one hundred natural numbers 
and the square of the sum'''

numList = [x for x in range(1, 101)]
squares = map(lambda x: x**2, numList)
sumOfSquares = sum(squares)
squareOfSums = sum(numList)**2
print abs(sumOfSquares - squareOfSums)