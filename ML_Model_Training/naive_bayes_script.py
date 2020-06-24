import pandas as pd 


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
print(dataset.head())
print(dataset.tail())
print(dataset.shape)
print(dataset.columns)