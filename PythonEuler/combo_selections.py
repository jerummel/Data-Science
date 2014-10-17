'''Project Euler Problem 53
Find how many, not necessarily distinct, values of  n!/(r!*(n-r)!), for 1 <= n <= 100, are greater than one-million.'''

from math import factorial
	
def main():
	valCount = 0
	for n in range(23, 101):
		for r in range(1, int(n/2)+1):
			if factorial(n)/(factorial(r)*factorial(n-r)) > 10**6:
				valCount += n-2*r+1 #(n-r)-r+1
				break
	print valCount
	
if __name__ == "__main__":
    main()