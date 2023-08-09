#%%
import os 
import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import eli5
from eli5.sklearn import PermutationImportance
import time

start_time = time.time()

data = pd.read_csv('../url_info.csv',encoding='latin1')

feature_columns = list(data.columns.difference(['url_type']))

X = data[feature_columns]
y = data['url_type']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

bag_clf = BaggingClassifier(DecisionTreeClassifier(), n_estimators=500, max_samples=25000, bootstrap=True, n_jobs=-1)

bag_clf.fit(X_train, y_train)
y_pred = bag_clf.predict(X_test)

print(accuracy_score(y_test, y_pred))

end_time = time.time()
total_time = end_time - start_time
print(f"Total running time: {total_time:.2f} seconds")
# %%
