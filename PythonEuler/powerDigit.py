'''Project Euler Problem 16
Find the sum of the digits of the number 2^1000'''

def main():
    powerNum = 2**1000
    powerString = str(powerNum)
    digitSum = 0
    for digit in powerString:
        digitSum += int(digit)
    print(digitSum)
    
if __name__ == "__main__": main()