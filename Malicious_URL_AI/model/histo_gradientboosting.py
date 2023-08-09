#%%
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate
from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingClassifier
import eli5
from eli5.sklearn import PermutationImportance
import time

start_time = time.time()

data = pd.read_csv('../url_info.csv',encoding='latin1')

feature_columns = list(data.columns.difference(['url_type']))

X = data[feature_columns]
y = data['url_type']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=0)

hgb = HistGradientBoostingClassifier(random_state=42)
scores = cross_validate(hgb, X_train, y_train, return_train_score=True, n_jobs=-1)

print(np.mean(scores['train_score']), np.mean(scores['test_score']))

end_time = time.time()
total_time = end_time - start_time
print(f"Total running time: {total_time:.2f} seconds")

hgb.fit(X_train, y_train)

perm = PermutationImportance(hgb, scoring = "f1", random_state = 42).fit(X_test, y_test)
eli5.show_weights(perm, top = 26, feature_names = X_test.columns.tolist())

# %%
