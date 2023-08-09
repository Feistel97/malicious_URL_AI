#%%
import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

data = pd.read_csv('../url_info2.csv', encoding='latin1')

feature_columns = list(data.columns.difference(['url_type']))

X = data[feature_columns]
y = data['url_type']

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(random_state=0, max_depth=20)
model.fit(X_train, y_train)

y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# Classification report for label 1
report_label_1 = classification_report(y_train, y_train_pred, labels=[1], target_names=['Label 1'])
print("Classification report for Label 1:")
print(report_label_1)

# Classification report for label 0
report_label_0 = classification_report(y_train, y_train_pred, labels=[0], target_names=['Label 0'])
print("Classification report for Label 0:")
print(report_label_0)


# %%
