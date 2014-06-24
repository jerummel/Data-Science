'''Project Euler Problem 20
Find the sum of the digits in the number 100!.'''

import math

def main():
    digitSum = 0
    hundredFact = math.factorial(100)
    factString = str(hundredFact)
    for digit in factString:
        digitSum += int(digit)
    print(digitSum)
    print(hundredFact)

if __name__ == "__main__": main()