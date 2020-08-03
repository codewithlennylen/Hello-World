import pandas as pd 
import joblib
from nltk.tokenize import word_tokenize #
from nltk.corpus import stopwords #
from nltk.stem import PorterStemmer #
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.utils import shuffle
from sklearn.metrics import (accuracy_score, confusion_matrix, recall_score,
                             precision_score, f1_score)
from sklearn.pipeline import Pipeline

print('Libraries Imported Successfully')


## Importing Tweets from the CSV file ->> Tiny Dataset
df = pd.read_csv(
    "C:\\Users\\lenovo\\Documents\\GitHub\\Hello-World\\ML_Model_Training\\data\\mini.csv", encoding='utf-8')
df.columns =['target','ids','date','flag','user','text']
# Shuffle the Data
df = shuffle(df)

X = df['text'] # These are the tweets :> object
y = df['target'] # These are the scores [0-4] :> int64


print('Dataset Loaded and Shuffled')

## SPLIT THE DATASET INTO TRAIN AND TEST SETS
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=24)


## MACHINE LEARNING MODEL-BUILDING
# Define the model
# Using a Pipeline makes the workflow Concise
text_clf = Pipeline([
    ("vect", CountVectorizer()),
    ("tfidf", TfidfTransformer()),
    ("clf", MultinomialNB())
])

# Train the model
text_clf.fit(X_train, y_train)
print('Classifier Trained Successfully')

# Saving The Model
# joblib.dump(text_clf, open('C:/Users/lenovo/Documents/GitHub/Hello-World/ML_Model_Training/models/mini_multinomialNB.model','wb'))
# print("Model Saved")

## MODEL EVALUATION
# predictions = text_clf.predict(X_test)

# Load the model
loaded_model = joblib.load(open(
    'C:/Users/lenovo/Documents/GitHub/Hello-World/ML_Model_Training/models/mini_multinomialNB.model', 'rb'))
predictions = loaded_model.predict(X_test)




print(f'\nConfusion Matrix : {confusion_matrix(y_test, predictions)}')
print(f'\nAccuracy Score : {accuracy_score(y_test, predictions)}')
print(f'\nRecall Score : {recall_score(y_test, predictions, average=None)}')
print(f'\nPrecision Score : {precision_score(y_test, predictions, average=None)}')
print(f'\nF1 Score : {f1_score(y_test, predictions, average=None)}')
