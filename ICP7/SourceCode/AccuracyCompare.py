from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn import metrics
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB

# Training Data Set
twenty_train_all = fetch_20newsgroups(subset='train', shuffle=True)
print(list(twenty_train_all.target_names))

categories = ['talk.politics.guns', 'talk.politics.mideast', 'talk.politics.misc', 'talk.religion.misc']
twenty_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True)
print(list(twenty_train.target_names))

# Applying TfidfVectorizer
tfidf_Vect = TfidfVectorizer()
X_train_tfidf = tfidf_Vect.fit_transform(twenty_train.data)

# Multinomial Naive Bayes

# Test and Train Set
clf = MultinomialNB()
clf.fit(X_train_tfidf, twenty_train.target)
twenty_test = fetch_20newsgroups(subset='test', categories=categories, shuffle=True)
X_test_tfidf = tfidf_Vect.transform(twenty_test.data)

# Prediction on the Data Set
MultinomialNB_pred = clf.predict(X_test_tfidf)

# Calculating Accuracy score for the Multinomial Naive Bayes
MultinomialNB_score = metrics.accuracy_score(twenty_test.target, MultinomialNB_pred)
print("Multinomial Naive Bayes Accuracy Score", MultinomialNB_score)

# SVM

# Training model
svc = SVC()
svc.fit(X_train_tfidf, twenty_train.target)

# Applying Prediction on the Test with SVC
svc_pred = clf.predict(X_test_tfidf)

# Calculating Accuracy for SVC
svc_score = metrics.accuracy_score(twenty_test.target, svc_pred)
print("SVM Accuracy Score", svc_score)

# changing the tfidf vectorizer to use bigram and setting TfidfVectorizer(ngram_range=(1,2))
tfidf_Vect_bigram = TfidfVectorizer(ngram_range=(1, 2))

# Training the Data set
X_train_tfidf_bigram = tfidf_Vect_bigram.fit_transform(twenty_train.data)
X_test_tfidf_bigram = tfidf_Vect_bigram.transform(twenty_test.data)
svc.fit(X_train_tfidf_bigram, twenty_train.target)

# Predicting Using SVC
svc_pred = svc.predict(X_test_tfidf_bigram)

# Calculating Accuracy score after setting the tfidf vectorizer
svc_bigram = metrics.accuracy_score(twenty_test.target, svc_pred)
print("SVM Accuracy Score With bigram", svc_bigram)

# Setting argument stop_words='english'
# Setting TfidfVectorizer(ngram_range=(1,2)) & Stopword=english
tfidf_Vect_stopword = TfidfVectorizer(ngram_range=(1, 2), stop_words='english')

# Training the Data set
X_train_tfidf_stopword = tfidf_Vect_stopword.fit_transform(twenty_train.data)
X_test_tfidf_stopword = tfidf_Vect_stopword.transform(twenty_test.data)
svc.fit(X_train_tfidf_stopword, twenty_train.target)

# Predicting Using SVC
svc_pred_bigram_stopword = svc.predict(X_test_tfidf_stopword)

# Calculating Accuracy score
svc_score_bigram_stopword = metrics.accuracy_score(twenty_test.target, svc_pred_bigram_stopword)
print("SVM Accuracy Score With bigram and Stop Word", svc_score_bigram_stopword)

