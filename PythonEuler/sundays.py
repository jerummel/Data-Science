'''Project Euler Problem 19
Find how many Sundays fell on the first of the month during the twentieth century 
(1 Jan 1901 to 31 Dec 2000).'''

daysInMonths = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
startday = 1
count = 0
for year in range(1900, 2001):
	for days in daysInMonths:
		if(year%4 == 0 and days == 28):
			realDays = 29
		else:
			realDays = days
		startday += realDays%7
		if(startday >= 7):
			startday -= 7
		if(startday == 0 and year > 1900):
			count += 1
print count