'''Project Euler Problem 31
In England the currency is made up of pound, L, and pence, p, and there are eight coins in 
general circulation: 1p, 2p, 5p, 10p, 20p, 50p, L1 (100p) and L2 (200p).  Find how many 
different ways L2 can be made using any number of coins.'''

target = 200
coinWays = 0

for first in range(200, -1, -200):
	for second in range(first, -1, -100):
		for third in range(second, -1, -50):
			for fourth in range(third, -1, -20):
				for fifth in range(fourth, -1, -10):
					for sixth in range(fifth, -1, -5):
						for seventh in range(sixth, -1, -2):
							coinWays += 1
print coinWays