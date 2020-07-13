import pandas as pd 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

## Importing Tweets from the CSV file
# df = pd.read_csv('data/twitter1.6m.csv', encoding='utf-8')
# df.columns =['target','ids','date','flag','user','text']

## Importing Tweets from the CSV file ->> Tiny Dataset
df = pd.read_csv('data/tiny_dataset.csv', encoding='utf-8')
df.columns =['text', 'target']

## Take a look inside the dataset
# print(df.head())
# print(df.describe)
# print(df.columns)
# print(df.info())
# print(df.isnull().sum())

## Clean the Dataset - Reformatting it to drop columns i do not need for this model
# dataset = df[['text', 'target']]
# print(dataset.head())
# print(dataset.tail())
# print(dataset.shape)
# print(dataset.columns)

# Resizing the Dataset
# tiny_dataset = dataset.iloc[1080000:1080010,:]
# print(tiny_dataset)
# tiny_dataset.to_csv('data/tiny.csv', index=False)

# X = dataset['text'] # These are the tweets :> object
# y = dataset['target'] # These are the scores [0-4] :> int64
# # print(X.tail())
# # print(y.tail())

X = df['text'] # These are the tweets :> object
y = df['target'] # These are the scores [0-4] :> int64
# print(X.tail())
# print(y.tail())

# ## Tokenization
# X_tokens = [word_tokenize(word) for word in X] # Returns a List of Lists containing tokens
# print(len(X_tokens)) #1599999
# print(X_tokens[-1])

# ## Tokenization ->> Tiny Dataset
X_tokens = [word_tokenize(word) for word in X] # Returns a List of Lists containing tokens
print(len(X_tokens)) #1599999
print(X_tokens[-1])

## Stop-words Removal
## Also unwanted_characters are being filtered out here!
print('\nStopWords\n')
stop_words = set(stopwords.words('english'))
unwanted_characters = ['@','#','%']
X_tokens_stopwords = []
for tweet_token_list in X_tokens:
	new_list = []
	for word in tweet_token_list:
		if word not in stop_words and word not in unwanted_characters:
			new_list.append(word)
	
	X_tokens_stopwords.append(new_list)

print(len(X_tokens_stopwords))
print(X_tokens_stopwords[-1])


stemmer = PorterStemmer()
X_stemmed = []
for token_list in X_tokens_stopwords:
	new_list = []
	for token in token_list:
		new_list.append(stemmer.stem(token))
	X_stemmed.append(new_list)

print(' Stemmed ')
print(len(X_stemmed))
print(X_stemmed[-1])

X = X_stemmed
print(X[-1])

## FEATURE EXTRACTION
