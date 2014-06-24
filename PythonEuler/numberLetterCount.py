'''Project Euler Problem 17
Find the number of letters used if all the numbers from 1 to 1000 (one thousand) inclusive 
were written out in words.'''

def main():
    ones = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    teens = ('ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen')
    tens = ('twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety')
    hundred = 'hundred'
    thousand = 'thousand'
    a = 'and'
    
    letterSum = 0
    
    #count all the times the one digits appear
    for o in ones:
        #each ones digit appears 9 times for each hundred and there are 10 hundreds in one thousand.
        #Each ones digit also appears 100 more times at the beginning of each hundred (i.e. one hundred, two hundred, etc)
        letterSum += 90*len(o) + 100*len(o)
    #one appears one additional time at the beginning of one thousand
    letterSum += len(ones[0])
    
    #count all of the times the teens appear
    for t in teens:
        #each teen appears once in each hundred and there are 10 hundreds in one thousand
        letterSum += 10*len(t)
        
    #count all of the times the tens appear
    for tn in tens:
        #each ten appears 10 times in each hundred and there are 10 hundreds in one thousand
        letterSum += 100*len(tn)
        
    #the word 'hundred' appears 100 times in each hundred, except the first hundred
    letterSum += 900*len(hundred)
    
    #the word 'thousand' only appears once
    letterSum += len(thousand)
    
    #the word 'and' appears 99 times in each hundred, except the first hundred
    letterSum += 99*9*len(a)
    
    print(letterSum)
        
if __name__ == "__main__": main()