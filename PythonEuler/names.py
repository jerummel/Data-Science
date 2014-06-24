'''Project Euler Problem 22
Read names from a text file into a list,
sort the list into alphabetical order, take the sum
of the letters of each word based on the position
the letter appears in the alphabet, then multiply
the sum by the position the word appears in the list
to get the score for the word.  Output the sum of
of all of the scores.'''


def main():
    f = open('names.txt')
    totalLine = ""
    for line in f:
        totalLine = totalLine + line
    totalLine = totalLine.replace('"', '')
    nameList = totalLine.split(',')
    nameList.sort()
    score = 0
    for idx, name in enumerate(nameList):
        letterSum = findLetterSum(name)
        score += letterSum * (idx+1)
    print score

def findLetterSum(theName):
    letterSum = 0
    for letter in theName:
        letterNum = ord(letter)
        if(letterNum >= 65 and letterNum <= 90):
            letterNum -= 64
        else:
            letterNum -= 96
        letterSum += letterNum
    return letterSum

if __name__ == "__main__":
    main()
