# Use a word occurence count vectorizer and run it though a Bernoulli  Naive Bayes

from movieRevFunctions import createVectorizer
import pandas as pd
from sklearn.naive_bayes import BernoulliNB
import numpy as np
from sklearn import metrics

def main():
	# Get the data and targets
	df = pd.read_csv('train1.csv')
	df = df[df.rating != 'rating']
	corpus = [review for review in df.review]
	splitPoint = len(corpus)*2/3
	trainingCorpus = corpus[:splitPoint]
	testCorpus = corpus[splitPoint:]
	target = [rating for rating in df.rating]
	trainingTarget = np.array(target[:splitPoint])
	testTarget = np.array(target[splitPoint:])

	# Train the algorithm
	train_X, vocabList = createVectorizer(trainingCorpus, 'None', True)
	NB_Bern_model = BernoulliNB().fit(train_X, trainingTarget)

	# Test the algorithm
	test_X = createVectorizer(testCorpus, vocabList, True)
	test_predict = NB_Bern_model.predict(test_X)
	print(np.mean(test_predict == testTarget))	
	print metrics.classification_report(testTarget, test_predict, target_names=['0', '1'])

	# Make Predictions
	predict_df = pd.read_csv('test2.csv')
	predictCorpus = [review for review in predict_df.review]
	member = [memberid for memberid in predict_df.ID]
	predict_X = createVectorizer(predictCorpus, vocabList, True)
	predictions = NB_Bern_model.predict(predict_X)
	predict_df.columns = ['ID', 'Predicted']
	for i in range(len(member)):
	 	predict_df.loc[predict_df['ID'] == member[i], 'Predicted'] = predictions[i]
	predict_df.to_csv('submission1.csv', sep = ',', index=False)




if __name__ == "__main__": main()