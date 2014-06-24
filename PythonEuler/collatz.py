'''Project Euler Problem 14
Find the starting number under 1 million that produces the longest collatz sequence.'''

def main():
    maxSequence = []
    longestChain = 1
    for x in range(1, 1000000):
        sequence = findCollatz(x)
        if len(maxSequence) < len(sequence):
            maxSequence = sequence
            longestChain = x
    print(longestChain)
    print(maxSequence)
    
def findCollatz(num):
    seqList = [num,]
    n = num
    while n != 1:
        if(n % 2 == 0):
            n = int(n/2)
        else:
            n = 3*n+1
        seqList.append(n)
    return seqList
    
if __name__ == "__main__": main()