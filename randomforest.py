#%%
import os 
import pandas as pd 
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import eli5
from eli5.sklearn import PermutationImportance
import time

start_time = time.time()
data = pd.read_csv('../url_info.csv',encoding='latin1')

nCar = data.shape[0] # 데이터 개수
nVar = data.shape[1] # 변수 개수
print('nCar: %d' % nCar, 'nVar: %d' % nVar )

feature_columns = list(data.columns.difference(['url_type']))

X = data[feature_columns]
y = data['url_type']

train_x, test_x, train_y, test_y = train_test_split(X, y, test_size = 0.2, random_state = 42)
print(train_x.shape, test_x.shape, train_y.shape, test_y.shape)

rf = RandomForestClassifier(n_estimators=45, max_depth=35,random_state=0)
rf.fit(train_x,train_y)

predict1 = rf.predict(test_x)
print(accuracy_score(test_y,predict1))

end_time = time.time()
total_time = end_time - start_time
print(f"Total running time: {total_time:.2f} seconds")

perm = PermutationImportance(rf, scoring = "f1", random_state = 42).fit(test_x, test_y)
eli5.show_weights(perm, top = 26, feature_names = test_x.columns.tolist())
# %%
