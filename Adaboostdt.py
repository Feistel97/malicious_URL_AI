#%%
import os
import pandas as pd 
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import eli5
from eli5.sklearn import PermutationImportance
import time

start_time = time.time()

data = pd.read_csv('../url_info.csv',encoding='latin1')

feature_columns = list(data.columns.difference(['url_type']))

X = data[feature_columns]
y = data['url_type']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=0)

ada_clf = AdaBoostClassifier(DecisionTreeClassifier(max_depth=4), n_estimators=1000, algorithm='SAMME.R', learning_rate=0.5)
ada_clf.fit(X_train, y_train)

y_pred = ada_clf.predict(X_test)
print(accuracy_score(y_test, y_pred))

end_time = time.time()
total_time = end_time - start_time
print(f"Total running time: {total_time:.2f} seconds")

perm = PermutationImportance(ada_clf, scoring = "f1", random_state = 42).fit(X_test, y_test)
eli5.show_weights(perm, top = 26, feature_names = X_test.columns.tolist())

# %%
