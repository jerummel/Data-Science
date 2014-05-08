# Create and validate the model

import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
import pandas as pd
from sklearn import metrics, linear_model
from sklearn.svm import LinearSVC
import math
from collections import Counter

def main():
	# Get the training data
	train_df = readCSVFile("cleanDataFiles/trainingData.csv")
	trainingDict = createDict(train_df, False)
	X = trainingDict['data']
	y = trainingDict['target']

	# Try a Decision Tree
	# tree_model = DecisionTreeClassifier()
	# print "Decision Tree Cross Validation:"
	# print cross_val_score(tree_model, X, y, cv = 10)

	# Try a Random Forest
	rf_model = RandomForestClassifier(n_estimators=10, max_features=None)
	# print "Random Forest Cross Validation:"
	# print(cross_val_score(rf_model, X, y, cv = 10))

	# VERDICT - The 10-fold cross validation was better with a Random Forest than a Deicision Tree
	# so, use a Random Forest for the model.

	# Try Dimension Reduction
	# etc_model = ExtraTreesClassifier()
	# new_data = etc_model.fit(X, y).transform(X)
	# print "Decision Tree With Dimension Reduction Cross Validation:"
	# print(cross_val_score(tree_model, new_data, trainingDict['target'], cv = 10))
	# print "Random Forest With Dimension Reduction Cross Validation:"
	# print(cross_val_score(rf_model, new_data, y, cv = 10))

	# Dimension Reduction made the cross validation worse

	# Fit the Random Forest.  Add weights to the fit since the data is skewed toward 0.
	c = Counter()
	for days in y:
		c[days] += 1
	weights = [c[0]/c[i] for i in range(16)]
	model_weight = np.array([weights[target] for target in y])
	rf_model_fitted = rf_model.fit(X, y, model_weight)
	test_df = readCSVFile("cleanDataFiles/testData.csv")
	testDict = createDict(test_df, False)
	test_X = testDict['data']
	test_y = testDict['target']
	predicted = rf_model_fitted.predict(test_X)
	# print "Random Forest Accuracy:"
	# print(np.mean(predicted == test_y))
	# print "Metrics Report For Random Forest:"
	# print metrics.classification_report(test_y, predicted, target_names=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15+'])

	# Try Logistic Regression to prove it won't work very well
	# logreg = linear_model.LogisticRegression(C=1e5)
	# print "Cross Validation for Logisitic Regression:"
	# print cross_val_score(logreg, X, y, cv = 10)
	# log_reg_fitted = logreg.fit(X, y)
	# log_reg_predicted = log_reg_fitted.predict(test_X)
	# print "Logisitic Regression Accuracy:"
	# print np.mean(log_reg_predicted == test_y)
	# print "Metrics Report for Linear Regression:"
	# print(metrics.classification_report(test_y, log_reg_predicted, target_names=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15+']))
	
	# Get the data that the predictions are to be made on
	predict_df = readCSVFile("cleanDataFiles/predictData.csv")
	predictDict = createDict(predict_df, True)
	predict_X = predictDict['data']
	predict_member = predictDict['member']
	predictions_y4 = rf_model_fitted.predict(predict_X)
	targetFile_df = pd.read_csv("Target.csv")
	member_predict = {}
	for i in range(len(predict_member)):
	 	member_predict[predict_member[i]] = str(predictions_y4[i])
	for member in predict_member:
	 	targetFile_df.loc[targetFile_df['MemberID'] == member, 'DaysInHospital'] = member_predict[member]
	targetFile_df.to_csv('DaysInHospital_Y4.csv', sep = ',', index=False)


def readCSVFile(fileName):
	df = pd.read_csv(fileName)
	df['male'] = df['sex'].apply(lambda sex: 1 if sex == 'M' else 0)
	df['female'] = df['sex'].apply(lambda sex: 1 if sex == 'F' else 0)
	df['unknownsex'] = df['sex'].apply(lambda sex: 1 if sex == 'Unknown' else 0)
	df.drop('sex', axis=1, inplace=True)
	df['age'] = df['age'].apply(lambda age: int(age[0]) if age != 'Unknown' else 9)
	df['drugcount'] = df['drugcount'].apply(lambda drug: 7 if drug == '7+' else int(drug))
	df['labcount'] = df['labcount'].apply(lambda lab: 10 if lab == '10+' else int(lab))
	df['condition'] = df['condition'].apply(lambda cond: math.log10(int(cond, 2)) if int(cond, 2) != 0 else 0)
	cols = df.columns.tolist()
	cols = cols[:1] + cols[-3:] + cols[1:len(cols)-3]
	df = df[cols]
	return df

def createDict(df, isPredict):
	memberArray = df['memberid'].values
	dataList = df.columns.values.tolist()
	if(isPredict):
		targetArray = []
		dataArray = df[dataList[1:len(dataList)]].values
	else:
		targetArray = df['daysinhospital'].values
		dataArray = df[dataList[1:len(dataList)-1]].values
	return{'member': memberArray, 'data': dataArray, 'target': targetArray}

if __name__ == "__main__": main()