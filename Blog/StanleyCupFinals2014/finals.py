'''This script will plot the team stats for the 2014 Stanley Cup finals between the Kings and 
the Rangers.  The outputs from this script are intended to be used for a blog.'''

import pandas as pd
import numpy as np
import imp
imp.load_source('plotFunction', '../plotFunction.py')
from plotFunction import plotFigure

def createPlotdf(datadf, columns, needDataFrame):
	dataList = []
	for columnName in columns:
		row = [datadf.iloc[i][columnName] for i in range(len(datadf))]
		dataList.append(row)
	if(needDataFrame == True):
		idx = np.array(columns)
		cols = [datadf.iloc[i]['Team'] for i in range(len(datadf))]
		return pd.DataFrame(np.array(dataList), index=idx, columns=pd.Index(cols))
	else:
		idx = [datadf.iloc[i]['Team'] for i in range(len(datadf))]
		return pd.Series(row, index=idx)

def main():
	finalsdf = pd.read_csv("finalsData.csv", sep=',')
	statsdf = createPlotdf(finalsdf, ['Goals', 'Corsi', 'Fenwick', 'Shots', 'Penalties'], True)
	plotFigure(statsdf, "bar", "Key Stats for 2014 Stanley Cup Finals", "Statistics", "Percentage", ('purple', 'blue'), (12, 8), 0, "finals_stats.png", True, [0, 70])
	savesdf = createPlotdf(finalsdf, ['SV%',], False)
	plotFigure(savesdf, "bar", "Save Percentage for 2014 Stanley Cup Finals", "Teams", "Percentage", ('purple', 'blue'), (8, 8), 0, "save_percent.png", True, [90, 95])
if __name__ == "__main__": main()