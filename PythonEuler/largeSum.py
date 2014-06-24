'''Project Euler Problem  13
Work out the first ten digits of the sum of the one-hundred 50-digit numbers in largeSum.txt.'''

def main():
    f = open('largeSum.txt')
    lineSum = 0
    for line in f.readlines():
        lineInt = int(line)
        lineSum += lineInt
    sumString = str(lineSum)
    print(sumString[:10])

if __name__ == "__main__": main()
