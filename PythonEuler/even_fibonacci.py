'''Project Euler Problem 2
By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.'''

fib1 = 1
fib2 = 1
limit = 4*10**6
evenFibs = []
while(fib2 < limit):
	fib1, fib2 = fib2, fib1+fib2
	if(fib2%2 == 0):
		evenFibs.append(fib2)
print sum(evenFibs)

