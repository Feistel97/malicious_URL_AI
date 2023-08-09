#%%
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('url_info.csv',encoding='latin1')

feature_columns = list(data.columns.difference(['url_type']))

X = data[feature_columns]
y = data['url_type']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=0)

classifiers = [
    ('GradientBoost', GradientBoostingClassifier(random_state=0)),
    ('RandomForest', RandomForestClassifier(random_state=0)),
    ('ExtraTree', ExtraTreesClassifier(random_state=0)),
    ('HistGradientBoost', HistGradientBoostingClassifier(random_state=0)),
    ('Bagging', BaggingClassifier(random_state=0)),
    ('DecisionTree', DecisionTreeClassifier(random_state=0)),
    ('AdaBoost_DT', AdaBoostClassifier(DecisionTreeClassifier(max_depth=1), n_estimators=100, random_state=42)),
    ('AdaBoost_ET', AdaBoostClassifier(ExtraTreesClassifier(max_depth=1), n_estimators=100, random_state=42))
]

results = {}
for i in range(len(classifiers)):
    for j in range(i+1, len(classifiers)):
        for k in range(j+1, len(classifiers)):
            clf1_name, clf1 = classifiers[i]
            clf2_name, clf2 = classifiers[j]
            clf3_name, clf3 = classifiers[k]
            voting_clf = VotingClassifier(estimators=[(clf1_name, clf1), (clf2_name, clf2), (clf3_name, clf3)])
            voting_clf.fit(X_train, y_train)
            score = voting_clf.score(X_test, y_test)
            results[clf1_name + '+' + clf2_name + '+' + clf3_name] = score

top_10 = sorted(results.items(), key=lambda x: x[1], reverse=True)[:10]
for name, score in top_10:
    print(f'{name}: {score:.3f}')
# %%
