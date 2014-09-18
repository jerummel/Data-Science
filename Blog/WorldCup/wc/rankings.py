'''Output to csv countries sorted in descending order based on how successful they have been
in the World Cup tournament'''

import pandas as pd
import numpy as np
import csv
import codecs

def wonMatch(isHome, res):
	if 'PSO' not in res:
		resList = res.split(' ')
		scoreList = resList[0].split(':')
	else:
		scoreList = []
		idx = res.rfind(':')
		if res[idx-1] == ' ':
			scoreList.append(res[idx-2])
		else:
			scoreList.append(res[idx-1])
		if res[idx+1] == ' ':
			scoreList.append(res[idx+2])
		else:
			scoreList.append(res[idx+1])
	if isHome:
		if scoreList[0] > scoreList[1]:
			return True
		else:
			return False
	else:
		if scoreList[0] < scoreList[1]:
			return True
		else:
			return False
	
def findCountries(df):
	home = df['hometeam'].tolist()
	away = df['awayteam'].tolist()
	allYears = df['year'].tolist()
	home.extend(away)
	return sorted(set(home))

def findScore(df, yr, grp, rnd, isHome, res):
	if grp == 'Final':
		if wonMatch(isHome, res):
			return 100.0
		else:
			return 50.0
	elif grp == 'Third place':
		if wonMatch(isHome, res):
			return 37.5
		else:
			return 25.0
	else:
		groupDF = df[(df['year'] == yr) & (df['wcRound'] == rnd)]
		grpCountries = findCountries(groupDF)
		return 100.0/len(grpCountries)

def main():
	data = pd.read_csv("webScrape.csv", sep=',')
	data.sort(('year', 'match'), ascending = (False, True), inplace=True)
	replacements = (('Germany FR', 'Germany'), ('German DR', 'East Germany'), ('Soviet Union', 'Russia'),
			('Korea DPR', 'North Korea'), ('Korea Republic', 'South Korea'), ('China PR', 'China'), 
			('Serbia and Montenegro', 'Serbia'), ('Republic of Ireland', 'Ireland'),
			('Match for third place', 'Third place'), ('Play-off for third place', 'Third place'))
	for nameTuple in replacements:
		data.replace(nameTuple[0], nameTuple[1], inplace = True)
	allYears = data['year'].tolist()
	countries = findCountries(data)
	years = sorted(set(allYears), reverse=True)
	scoreDict = {}
	score = 0
	for country in countries:
		score = 0
		scoreDict[country] = 0
		for year in years:
			newDF = data[(data['year'] == year) & ((data['hometeam'] == country) | (data['awayteam'] == country))]
			if newDF.empty:
				continue
			surviveToGroup = newDF.iloc[-1]['group']
			surviveToRound = newDF.iloc[-1]['wcRound']
			result = newDF.iloc[-1]['results']
			if newDF.iloc[-1]['hometeam'] == country:
				home = True
			else:
				home = False
			# 1950 did not have a final.  It had a final group and Uruguay won that group to win the Cup
			if(country == 'Uruguay' and year == 1950):
				scoreDict[country] += 100.0
			else:
				scoreDict[country] += findScore(data, year, surviveToGroup, surviveToRound, home, result)
		scoreDict[country] = round(scoreDict[country], 2)
	sorted_scores = sorted(scoreDict.items(), key=lambda x: x[0], reverse=False)
	sorted_scores = sorted(sorted_scores, key=lambda x: x[1], reverse=True)
	rnk = 0
	count = 0
	score = 0
	ranked_scores = []
	for s in sorted_scores:
		count += 1
		if s[1] != score:
			score = s[1]
			rnk = count
			ranked_scores.append((rnk, s[0], s[1]))
		else:
			ranked_scores.append((rnk, s[0], s[1]))

	with codecs.open('wcRankings.csv', 'wb') as csvfile:
		rankWriter = csv.writer(csvfile, delimiter=',')
		rankWriter.writerow(('Rank', 'Country', 'Score'))
		for countryTuple in ranked_scores:
			rankWriter.writerow(countryTuple)
	csvfile.close()


if __name__ == "__main__": main()