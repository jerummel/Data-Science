''' Project Euler Problem 25
Find the first term in a Finbonacci sequence that contains 1000 digits'''

def main():
	fib1 = 1
	fib2 = 1
	term = 2
	limit = pow(10, 999)
	while fib2 < limit:
		fib1, fib2 = fib2, fib1+fib2
		term += 1
	print term

if __name__ == "__main__":
    main()