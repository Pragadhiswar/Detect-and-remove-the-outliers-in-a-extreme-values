# -*- coding: utf-8 -*-
"""Detect and remove the outliers of extreme value.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qwZCjorbRdaUmvc3YyalYvqJ-ZHo68R3
"""

import sklearn
from sklearn.datasets import load_diabetes
import pandas as pd
import numpy as np
diabetes = load_diabetes()
column_name = diabetes.feature_names
df_diabetes = pd.DataFrame(diabetes.data)
df_diabetes.columns = column_name
df_diabetes.head()
print("OLD SHAPE:",df_diabetes.shape)
Q1 = df_diabetes['bmi'].quantile(0.25)
Q3 = df_diabetes['bmi'].quantile(0.75)
IQR = Q3 - Q1
Lower = Q1-1.5*IQR
Upper = Q3=1.5*IQR
upper_arrays = np.where(df_diabetes['bmi']>=Upper)[0]
lower_arrays = np.where(df_diabetes['bmi']<=Lower)[0]
df_diabetes.drop(df_diabetes.index[upper_arrays],inplace=True)
df_diabetes.drop(df_diabetes.index[lower_arrays],inplace=True)
print("NEW SHAPE:",df_diabetes.shape)