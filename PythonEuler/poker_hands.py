'''Project Euler Problem 54
Find how many hands of poker from poker.txt that Player 1 wins.'''

from collections import Counter

class Poker():
	def __init__(self, idxRange, allCards):
		self.hand = allCards[idxRange[0]:idxRange[1]]
		self.cards = [card[0] for card in self.hand]
		self.suits = [card[1] for card in self.hand]
		self.values = map(lambda x: self.convert(x), self.cards)
		self.cardCount = Counter(self.values)
		self.sortedCards = sorted(self.cardCount.items(), key = lambda x : (x[1], x[0]), reverse = True)


	def convert(self, cardVal):
		if cardVal == 'T':
			return 10
		elif cardVal == 'J':
			return 11
		elif cardVal == 'Q':
			return 12
		elif cardVal == 'K':
			return 13
		elif cardVal == 'A':
			return 14
		else:
			return int(cardVal)


	def royalFlush(self):
		if self.flush():
			if 'T' in self.cards and 'J' in self.cards and 'Q' in self.cards and 'K' in self.cards and 'A' in self.cards:
				return True
		return False

	def straightFlush(self):
		if self.flush() and self.straight():
			return True
		else:
			return False

	def flush(self):
		if len(set(self.suits)) == 1:
			return True
		else:
			return False

	def straight(self):
		minValue = min(self.values)
		if minValue+1 in self.values and minValue+2 in self.values and minValue+3 in self.values and minValue+4 in self.values:
				return True
		else:
			return False

	def duplicates(self, n):
		for key, value in self.cardCount.iteritems():
			if value == n:
				return True
		return False

	def twoPairs(self):
		pairCount = 0
		for key, value in self.cardCount.iteritems():
			if value == 2:
				pairCount += 1
		if pairCount == 2:
			return True
		else:
			return False

def rank(obj):
	if obj.royalFlush():
		return 10
	elif obj.straightFlush():
		return 9
	elif obj.duplicates(4): #four of a kind
		return 8
	elif obj.duplicates(3) and obj.duplicates(2): #Full House
		return 7
	elif obj.flush():
		return 6
	elif obj.straight():
		return 5
	elif obj.duplicates(3): #three of a kind
		return 4
	elif obj.twoPairs():
		return 3
	elif obj.duplicates(2): #one pair
		return 2
	else:
		return 1 #highest card

		
def main():
	pokerFile = open('poker.txt')
	player1Wins = 0
	for deal in pokerFile:
		deal = deal.strip()
		dealList = deal.split(' ')
		player1 = Poker((0, 5), dealList)
		player2 = Poker((5, 10), dealList)
		player1Rank = rank(player1)
		player2Rank = rank(player2)
		if player1Rank > player2Rank:
			player1Wins += 1
		elif player1Rank == player2Rank:
			for i in range(len(player1.sortedCards)):  # length of sortedCards for both players should be equal if the ranks are equal
				if player1.sortedCards[i][0] > player2.sortedCards[i][0]:
					player1Wins += 1
					break
				elif player2.sortedCards[i][0] > player1.sortedCards[i][0]:
					break
				else:
					continue
	print player1Wins
				
	
if __name__ == "__main__":
    main()