import pandas as pd 
from nltk.tokenize import word_tokenize #
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer #
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.utils import shuffle
from sklearn.metrics import (accuracy_score, confusion_matrix, recall_score,
                             precision_score, f1_score)

print('Libraries Imported Successfully')

## Importing Tweets from the CSV file
# df = pd.read_csv('data/twitter1.6m.csv', encoding='utf-8')
# df.columns =['target','ids','date','flag','user','text']

## Importing Tweets from the CSV file ->> Tiny Dataset
df = pd.read_csv(
    "C:\\Users\\lenovo\\Documents\\GitHub\\Hello-World\\ML_Model_Training\\data\\mini.csv", encoding='utf-8')
df.columns =['target','ids','date','flag','user','text']
# Shuffle the Data
df = shuffle(df)

X = df['text'] # These are the tweets :> object
y = df['target'] # These are the scores [0-4] :> int64
# print(X.tail())
# print(y.tail())

print('Dataset Loaded and Shuffled')

## SPLIT THE DATASET INTO TRAIN AND TEST SETS
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=24)

## FEATURE EXTRACTION
# Bag-of-Words Model
count_vec = CountVectorizer()
X_train_counts = count_vec.fit_transform(X_train)

# Tf-idf
tfidf_transformer = TfidfTransformer(use_idf=False)
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

print('Done Extracting Features')
print(f"X_train_tfidf.shape : {X_train_tfidf.shape}") # (12, 140)
# print(X_train_tfidf)

# new data to be feature-extracted before being predicted by the classifier
X_test_count = count_vec.transform(X_test)
X_test_tfidf = tfidf_transformer.transform(X_test_count)
print(f"X_test_tfidf.shape : {X_test_tfidf.shape}")

## MACHINE LEARNING MODEL-BUILDING
# Define the model
clf = MultinomialNB()

# Train the model
clf.fit(X_train_tfidf, y_train)
print('Classifier Trained Successfully')

## MODEL EVALUATION
predictions = clf.predict(X_test_tfidf)
# print(predictions)

print(f'\nConfusion Matrix : {confusion_matrix(y_test, predictions)}')
print(f'\nAccuracy Score : {accuracy_score(y_test, predictions)}')
print(f'\nRecall Score : {recall_score(y_test, predictions, average=None)}')
print(f'\nPrecision Score : {precision_score(y_test, predictions, average=None)}')
print(f'\nF1 Score : {f1_score(y_test, predictions, average=None)}')
