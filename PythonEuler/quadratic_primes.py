'''Project Euler Problem 27
Find the product of the coefficients, a and b, where abs(a) < 1000 and abs(b) < 1000, 
for the quadratic expression that produces the maximum number of primes for consecutive values of n,
starting with n = 0.

(n-x)**2+(n-x)+41 will yeild prime numbers for n = 0 to x+39
so (n-x)**2+(n-x)+41 = n**2 + (1-2*x)*n + (x**2 - x + 41)
therfore a = 1-2*x and b = x**2-x+41 and we need to find the maximum value of x where
abs(a) < 1000 and abs(b) < 1000.'''

def main():
    x = 0
    while(abs(1-2*x) < 1000 and abs(x**2-x+41) < 1000):
        x+=1
    x-=1
    a = 1-2*x
    b = x**2 - x + 41
    print a * b
    
    
if __name__ == "__main__": main()