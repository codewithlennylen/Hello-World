import pandas as pd 
from nltk.tokenize import word_tokenize

## Importing Tweets from the CSV file
df = pd.read_csv('data/twitter1.6m.csv', encoding='utf-8')
df.columns =['target','ids','date','flag','user','text']

## Take a look inside the dataset
# print(df.head())
# print(df.describe)
# print(df.columns)
# print(df.info())
# print(df.isnull().sum())

## Clean the Dataset - Reformatting it to drop columns i do not need for this model
dataset = df[['text', 'target']]
# print(dataset.head())
# print(dataset.tail())
# print(dataset.shape)
# print(dataset.columns)

X = dataset['text'] # These are the tweets :> object
y = dataset['target'] # These are the scores [0-4] :> int64
# print(X.tail())
# print(y.tail())

## Tokenization
# X_tokens = [word_tokenize(word) for word in X] # Returns a List of Lists containing tokens
# print(X_tokens[-1])

## Stop-words Removal