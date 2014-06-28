'''This script will read from a file that contains data for the home teams in the 2014 NHL playoffs.
From that data, it will calculate the overall winning percentage of the home teams.'''

import pandas as pd
import numpy as np

def main():
	homeTeamdf = pd.read_csv("playoffs_home_teams_2014.csv", sep=',')
	winSum = 0
	for i in range(len(homeTeamdf)):
		if(homeTeamdf.iloc[i]['Result'][0] == 'W'):
			winSum += 1
	print (float(winSum)/len(homeTeamdf)) * 100
if __name__ == "__main__": main()