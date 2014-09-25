'''Project Euler Problem 48
Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.'''

selfPowers = [i**i for i in range(1, 1001)]
result = sum(selfPowers)
resultString = str(result)
print resultString[-10:]