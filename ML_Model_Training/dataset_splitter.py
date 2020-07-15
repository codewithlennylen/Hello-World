import pandas as pd
from sklearn.utils import shuffle

data = pd.read_csv("C:\\Users\\lenovo\\Documents\\GitHub\\Hello-World\\ML_Model_Training\\data\\twitter1.6m.csv")
data = shuffle(data)
print("loaded and shuffled dataset")

new_data = data[:2000]
new_data.to_csv("C:\\Users\\lenovo\\Documents\\GitHub\\Hello-World\\ML_Model_Training\\data\\mini.csv")
print("successfully wrote changes")