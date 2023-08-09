#%%
import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
import eli5
from eli5.sklearn import PermutationImportance
import time

start_time = time.time()

data = pd.read_csv('../url_info.csv',encoding='latin1')

feature_columns = list(data.columns.difference(['url_type']))

X = data[feature_columns]
y = data['url_type']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=0)

gbrt = GradientBoostingClassifier(random_state=0, max_depth=12)
gbrt.fit(X_train, y_train)

print("훈련 세트 정확도: {:.3f}".format(gbrt.score(X_train, y_train)))
print("테스트 세트 정확도: {:.3f}".format(gbrt.score(X_test, y_test)))

end_time = time.time()
total_time = end_time - start_time
print(f"Total running time: {total_time:.2f} seconds")

perm = PermutationImportance(gbrt, scoring = "f1", random_state = 42).fit(X_test, y_test)
eli5.show_weights(perm, top = 26, feature_names = X_test.columns.tolist())
# %%
