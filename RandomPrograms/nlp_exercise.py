# This is a short exercise designed to test your knowledge of basic natural
# language processing (NLP) techniques in Python. It is also one of the interview
# questions I ask entry-level data science candidates at Whisper.

# In each of the parts below, I have provided a function definition (with the
# correct arguments but no implementation) and some tests that will pass *if* 
# you fill in the correct implementation for each function. If you run this file
#  (i.e. run `python nlp_exercise.py` from your shell) and it does not throw
#  any errors, then you have finished the exercise!

from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords

# Question 1: Normalization and Tokenization

def process_text(text):
    normalized_text = text.lower()
    return tokenize(normalized_text)

def tokenize(text):
	alpha_text = ''.join(c for c in text if c == ' ' or c.isalpha())
	return alpha_text.split()

# BEGIN TESTS
assert process_text('Python is SO AWESOME!!!!!! YAy!!!!@ I love programming in python!') == ['python', 'is', 'so', 'awesome', 'yay', 'i', 'love', 'programming', 'in', 'python']
# END TESTS


# # Question 2: Count word occurences
def count_words(text):
	vectorizer = CountVectorizer(token_pattern= '\w+')
	corpus = [text]
	X = vectorizer.fit_transform(corpus)
	keys = vectorizer.get_feature_names()
	stops = vectorizer.get_stop_words()
	countList = X.toarray()[0]
	final_dict =  {str(keys[i]): countList[i] for i in range(0, len(keys))}
	return final_dict

# BEGIN TESTS
assert count_words('Python is SO AWESOME!!!!!! YAy!!!!@ I love programming in python!') == {'yay': 1, 'python': 2, 'is': 1, 'programming': 1, 'i': 1, 'so': 1, 'in': 1, 'love': 1, 'awesome': 1}
# END TESTS

# Question 3: Create a string distance function
def distance(text1, text2):
	stopWordList = stopwords.words('english')
	stopped1 = [word for word in process_text(text1) if word not in stopWordList]
	stopped2 = [word for word in process_text(text2) if word not in stopWordList]
	newList = []
	found = False
	for word1 in stopped1:
		for word2 in stopped2:
			if(word1 == word2):
				found = True
				break
		if(found == False):
			newList.append(word1) # any word unique to list 1 is appended to newList
		else:
			# any word that appears in both lists is removed from list 2 so it is not compared again
			stopped2.remove(word2) 
			found = False
	newList.extend(stopped2) # any word unique to list 2 is extended into newList
	return len(newList) #newList only contains words that are unique to one list or the other

# BEGIN TESTS
assert distance('I love my mom', 'i love my daddy') < distance('I love my mom', 'I am a big boy now')
assert distance('some strings are similar to other strings', 'some strings') > distance('some strings are similar to other strings', 'some strings are similar')
assert distance('i hate hate hate noodles.', 'i hate hate noodles') < distance('i hate hate hate noodles.', 'i hate noodles.')
# END TESTS

print 'All tests passed. Congratulations!'