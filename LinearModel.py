#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 13:56:16 2019

@author: maggiedube
"""
#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt #Data Visualization Libraries
import seaborn as sns
#%matplotlib inline

#defining predictors as the pre-set feature names
dd = pd.read_csv("~/desktop/DSCData.csv")
dd.head()
dd.info()
dd.describe()
dd['Glucose Level'][0]
sns.pairplot(dd)
dd.corr()

X = dd[['Glucose Level', 'Minutes passed', 'Carbohydrate Intake', 'Insulin Injected', 'Sick?', 'Menstrual Cycle?']]
y = dd['Insulin Injected']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
#X_test.fillna(X_test.mean())
#X_test = X_test.fillna(X_train.mean())

from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X_train, y_train)
predictions = lm.predict(X_test)
plt.scatter(y_test, predictions)
plt.show()

"""
from sklearn.metrics import mean_squared_error
print("Mean Squared Error: %.2f" % mean_squared_error(y_test, predictions))
"""
