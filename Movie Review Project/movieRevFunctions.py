# Module containing the methods for breaking up the movie review text into a count vectorizer

from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords


def createVectorizer(corpus, vocab, bin):
	if(vocab == 'None'):
		vectorizer = CountVectorizer(stop_words = 'english', binary=bin, vocabulary=None, min_df=2)
	else:
		vectorizer = CountVectorizer(stop_words = 'english', binary=bin, vocabulary=vocab)
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