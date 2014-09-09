'''Project Euler Problem 5
Find the smallest positive number that is evenly divisible by all of the numbers from 1 to 20'''

numList = [x for x in range(19, 0, -1)]
found = False
i=2
while(not found):
	multiple = 20*i
	for num in numList:
		if(multiple%num != 0):
			break
		elif(num == 1):
			found = True
	i+=1
print multiple