'''This script allows a user to enter a trim id of a car and then outputs the trim ids of cars
that are similar to the car the user entered.'''

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import euclidean_distances
import sys

# Determines how many words of the trim in each row of the data frame are also in the user's car's trim
def trimSimilarity(df, trim):
    trimList = trim.split(' ')
    simList = []
    for idx in range(len(df)):
        count = 0
        otherTrim = df.iloc[idx]['trim']
        for word in trimList:
            if word in otherTrim:
                count+=1
        simList.append(count)
    df['trim_similarity'] = simList
    return df

# Finds how similar the car in each row of the data frame is to the user's car
def findDistances(df, trimdf):
    carsParameters = df[0:][['msrp', 'invoice', 'pct_discount', 'n_ind_transactions', 'trim_similarity']]
    trimParameters = trimdf[0:][['msrp', 'invoice', 'pct_discount', 'n_ind_transactions', 'trim_similarity']]
    dists = []
    for idx in range(len(df)):
        dists.append(euclidean_distances(np.array(carsParameters.iloc[idx]), np.array(trimParameters.iloc[0]))[0][0])
    df['distances'] = dists
    return df

def main():
    carData = pd.read_csv("trims.csv", sep=',')

    #scale the columns
    carData['msrp'] = carData['msrp'] / 1000
    carData['invoice'] = carData['invoice'] / 1000
    carData['pct_discount'] = carData['pct_discount']*100
    trimData = []
    while(len(trimData) == 0):
        trimID = raw_input('Enter a trim ID (or enter e to exit):')
        if(trimID == 'e' or trimID == 'E'):
            sys.exit()
        else:
            try:
                trimID = int(trimID)
                trimData = carData[carData['trim_id'] == trimID]
                if(len(trimData) == 0):
                    print '%s is not a valid trim ID.  Please try again.' % trimID
                else:
                    trimTrim = trimData.iloc[0]['trim']
                    trimTrimList = trimTrim.split(' ')
                    trimData['trim_similarity'] = len(trimTrimList)
            except ValueError:
                print '%s is not a valid trim ID.  Please try again.' % trimID
            
    trimBody = trimData.iloc[0]['tc_body']

    filtered_cars = carData[(carData['trim_id'] != trimID) & (carData['tc_body'] == trimBody)]
    filtered_cars = trimSimilarity(filtered_cars, trimTrim)
    filtered_cars = findDistances(filtered_cars, trimData)
    sorted_cars = filtered_cars.sort(columns='distances')

    print 'Trim IDs of similar cars: %s' % np.array(sorted_cars[:5]['trim_id'])

if __name__ == "__main__": main()