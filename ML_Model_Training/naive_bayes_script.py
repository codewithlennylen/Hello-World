import pandas as pd 


# Importing Tweets from the CSV file
df = pd.read_csv('data/twitter1.6m.csv', encoding='utf-8')

# Take a look inside the dataset
print(df.head())
