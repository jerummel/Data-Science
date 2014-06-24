'''Project Euler Problem 12
The sequence of triangle numbers is generated by adding the natural numbers.  
Find the value of the first triangle number to have over five hundred divisors.'''

import math

def main():
    factors = []
    triNum, i = 1, 2
    while len(factors) < 500:
        triNum, i = triNum + i, i+1
        factors = findFactors(triNum)
    print(triNum)
    print(factors)
        
def findFactors(number):
    divList = []
    root = math.sqrt(number)
    rangeMax = int(root)
    for x in range(1, rangeMax+1):
        if(number % x == 0):
            divList.append(x)
            if(number/x != float(x)): divList.append(int(number/x))
    return divList

if __name__ == "__main__": main()