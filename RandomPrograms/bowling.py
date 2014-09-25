import csv

class bowlingScore:
	def __init__(self, scoreList):
		self.scores = scoreList
		self.frames = map(str, range(1, 11))

	def getFrameScore(self):
		frameScore = []
		idx = 0
		while idx < len(self.scores) and len(frameScore) < 10:
			if self.scores[idx] == 'X':
				if idx+1 >= len(self.scores) or idx+2 >= len(self.scores):
					break
				else:
					score = 10
					if self.scores[idx+1] == 'X':
						score += 10
						if self.scores[idx+2] == 'X':
							score+= 10
						else:
							score += int(self.scores[idx+2])
					elif self.scores[idx+2] == '/':
						score += 10
					else:
						score += int(self.scores[idx+1]) + int(self.scores[idx+2])
				frameScore.append(score)
				idx += 1
			elif idx+1 < len(self.scores):
				if self.scores[idx+1] == '/':
					if idx+2 < len(self.scores):
						if self.scores[idx+2] == 'X':
							score = 20
						else:
							score = 10 + int(self.scores[idx+2])
					else:
						break
				else:
					score = int(self.scores[idx]) + int(self.scores[idx+1])
				frameScore.append(score)
				idx += 2
			else:
				break
		return frameScore

	def getRunningTotal(self, frameScoreList):
		if len(frameScoreList) == 0:
			frameScoreList = self.getFrameScore()
		runningTotalList = []
		total = 0
		for score in frameScoreList:
			total += score
			runningTotalList.append(total)
		return runningTotalList

class frameResult:
	def __init__(self, scoreList):
		self.scores = scoreList
		self.index = 0
		self.frame = 0
	def __iter__(self):
		return self
		
	def next(self):
		result = ''
		self.frame += 1
		if self.frame == 11 or self.index >= len(self.scores):
			raise StopIteration
		elif self.frame == 10:
			score1 = self.scores[self.index]
			if self.index+1 >=  len(self.scores):
				score2, score3 = '', ''
			elif self.index+2 >=  len(self.scores):
				score2, score3 = '%s%s' % (' ', self.scores[self.index + 1]), ''
			else:
				score2, score3 = '%s%s' % (' ', self.scores[self.index + 1]), '%s%s' % (' ', self.scores[self.index + 2])
			return '%s%s%s' % (score1, score2, score3)
		else:
			if(self.scores[self.index] == 'X'):
				self.index+= 1
				return self.scores[self.index - 1]
			else:
				self.index += 2
				if self.index-1 >= len(self.scores):
					return self.scores[self.index-2]
				else:
					return '%s %s' % (self.scores[self.index - 2], self.scores[self.index - 1])
		
		
def main():
	results = []
	infile = open('bowlingScores.csv')
	for line in infile:
		line = line.strip()
		shots = line.split(',')
		bowlingObj = bowlingScore(shots)
		frames = bowlingObj.frames
		frames.insert(0, 'Frame:')
		frameResultObj = frameResult(bowlingObj.scores)
		frameResults = [x for x in iter(frameResultObj)]
		frameResults.insert(0, 'Result:')
		scores = bowlingObj.getFrameScore()
		runningTotal = bowlingObj.getRunningTotal(scores)
		scores.insert(0, 'FrameScore:')
		runningTotal.insert(0, 'Running Total:')
		results.append(frames)
		results.append(frameResults)
		results.append(scores)
		results.append(runningTotal)
		with open('bowlingResults.csv', 'wb') as csvfile:
			bowlingwriter = csv.writer(csvfile, delimiter=',')
			for resultList in results:
				bowlingwriter.writerow(resultList)
	
if __name__ == '__main__':
	main()
		