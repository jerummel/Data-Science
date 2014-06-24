'''This script will plot the playoff stats for Penguins goaltenders and do a kmeans clustering
of all goaltenders that have made the playoffs from 2009-2014.  The outputs from this script are
intended to be used for a blog.'''

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import imp
imp.load_source('plotFunction', '../plotFunction.py')
from plotFunction import plotFigure

def changeValue(oldValue, sep):
	seperator = oldValue.find(sep)
	return oldValue[seperator+1:]

def  modifydf(df, playoffs):
	df = df.sort(columns = ('Year', 'Rk'))
	for i in range(len(df)):
		df.Player[i] = changeValue(df.Player[i], ' ')
		if(playoffs == False):
			df.Year[i] = "20%s" % changeValue(df.Year[i], '-')
	df['SPG'] = pd.Series(np.array([round(float(df.iloc[i]['SA']/df.iloc[i]['GP']), 2) for i in range(len(df))]), index=df.index)
	df = df[(df.MIN > 120)]
	return df

def createIndex(df):
	return np.array(df.apply(lambda x:'%s  %s' % (x['Player'], x['Year']), axis=1))

def getDataFrame(playoffs, regular, columnName, isPercent):
	dataList = []
	for i in range(len(playoffs)):
		playoffVal = playoffs.iloc[i][columnName]
		if(isPercent):
			playoffVal = playoffVal * 100
		playerName = playoffs.iloc[i]['Player']
		year = str(playoffs.iloc[i]['Year'])
		regularVal = 0
		for j in range(len(regular)):
			if(regular.iloc[j]['Player'] == playerName and regular.iloc[j]['Year'] == year):
				regularVal = regular.iloc[j][columnName]
				if(isPercent):
					regularVal = regularVal * 100
				break
		dataList.append((regularVal, playoffVal))
	idx = createIndex(playoffs)
	return pd.DataFrame(np.array(dataList), index=idx, columns=pd.Index(('Regular Season', 'Playoffs')))

def clusterGoalies(df, idx, numOfClusters):
	model = KMeans(n_clusters=numOfClusters, n_init=20)
	distMat = model.fit_transform(df)
	resultList = [[] for i in range(numOfClusters)]
	for i, rowList in enumerate(distMat):
		minIndex = min(enumerate(rowList), key = lambda x: x[1])[0]
		resultList[minIndex].append(idx[i])
	return resultList

def main():
	playoffsdf = pd.read_csv("Goaltending_playoffs.csv", sep=',')
	playoffsdf = modifydf(playoffsdf, True)
	regulardf = pd.read_csv("Goaltending_regularSeason.csv", sep=',')
	regulardf.rename(columns={'Season': 'Year'}, inplace=True)
	regulardf = modifydf(regulardf, False)
	pensPlayoffdf = playoffsdf[(playoffsdf.Tm == 'PIT')]
	pensRegulardf = regulardf[(regulardf.Tm == 'PIT')]
	savePercent = getDataFrame(pensPlayoffdf, pensRegulardf, 'SV%', True)
	plotFigure(savePercent, "bar", "Penguins Goalies Save Percentage, 2009-2014", "Goaltenders", "Save Percentage", ('black', 'gold'), (12, 8), 0, "save_percent.png", True, [80, 95])
	gaa = getDataFrame(pensPlayoffdf, pensRegulardf, 'GAA', False)
	plotFigure(gaa, "bar", "Penguins Goalies Goals Against Average, 2009-2014", "Goaltenders", "Goals Against Average (GAA)", ('black', 'gold'), (12, 8), 0, "gaa.png", False, [0, 0])
	spg = getDataFrame(pensPlayoffdf, pensRegulardf, 'SPG', False)
	plotFigure(spg, "bar", "Penguins Goalies Shots Faced Per Game, 2009-2014", "Goaltenders", "Shots Faced Per Game", ('black', 'gold'), (12, 8), 0, "spg.png", False, [0, 0])
	winners = (('2009', 'Fleury', 'PIT'), ('2010', 'Niemi', 'CHI'), ('2011', 'Thomas', 'BOS'), ('2012', 'Quick', 'LAK'), ('2013', 'Crawford', 'CHI'), ('2014', 'Lundqvist', 'NYR'), ('2014', 'Quick', 'LAK'))
	winnerShots = pd.Series(np.array([playoffsdf.iloc[i]['SPG'] for i in range(len(playoffsdf)) if(str(playoffsdf.iloc[i]['Year']), playoffsdf.iloc[i]['Player'], playoffsdf.iloc[i]['Tm']) in winners]), index=np.array(('Fleury 2009', 'Niemi 2010', 'Thomas 2011', 'Quick 2012', 'Crawford 2013', 'Lundqvist 2014', 'Quick 2014')))
	plotFigure(winnerShots, "bar", "Stanley Cup Winning Goalies Shots Faced Per Game, 2009-2014", "Goaltenders", "Shots Faced Per Game", ('gold'), (12, 8), 0, "winnersSPG.png", False, [0,0])
	idx = createIndex(playoffsdf)
	goalieStatsdf = playoffsdf[['SV%', 'GAA']]
	clusterList = clusterGoalies(goalieStatsdf, idx, 10)
	for num, cluster in enumerate(clusterList):
		print "Cluster%s: %s" % (num+1, ", ".join(cluster))


if __name__ == "__main__": main()