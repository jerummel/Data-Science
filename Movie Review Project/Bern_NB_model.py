from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
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
	train_X, vocabList = createVectorizer(trainingCorpus, 'None')
	NB_Bern_model = BernoulliNB().fit(train_X, trainingTarget)

	# Test the algorithm
	test_X = createVectorizer(testCorpus, vocabList)
	test_predict = NB_Bern_model.predict(test_X)
	print(np.mean(test_predict == testTarget))	
	print metrics.classification_report(testTarget, test_predict, target_names=['0', '1'])

	# Make Predictions
	predict_df = pd.read_csv('test2.csv')
	predictCorpus = [review for review in predict_df.review]
	member = [memberid for memberid in predict_df.ID]
	predict_X = createVectorizer(predictCorpus, vocabList)
	predictions = NB_Bern_model.predict(predict_X)
	predict_df.columns = ['ID', 'Predicted']
	for i in range(len(member)):
	 	predict_df.loc[predict_df['ID'] == member[i], 'Predicted'] = predictions[i]
	predict_df.to_csv('submission1.csv', sep = ',', index=False)


def createVectorizer(corpus, vocab):
	if(vocab == 'None'):
		vectorizer = CountVectorizer(stop_words = 'english', binary=True, vocabulary=None, min_df=2)
	else:
		vectorizer = CountVectorizer(stop_words = 'english', binary=True, vocabulary=vocab)
	stemmer = PorterStemmer()
	new_corpus = []
	for text in corpus:
		wordList = tokenize(normalize(text))
		stemmedList = stemmed(stemmer, wordList)
		new_text = ' '.join(stemmedList)
		new_corpus.append(new_text)
	if(vocab == 'None'):
		vec_fit = vectorizer.fit_transform(new_corpus)
		vec_feat = vectorizer.get_feature_names()
		return vec_fit, vec_feat
	else:
		return vectorizer.fit_transform(new_corpus)


def normalize(text):
	return text.lower()

def tokenize(text):
	alphabetic_only = ''.join(char for char in text if char == ' ' or char.isalpha())
	return alphabetic_only.split()

def stemmed(stemmer, wordList):
	return[stemmer.stem(word) for word in wordList]

if __name__ == "__main__": main()