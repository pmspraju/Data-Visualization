# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 17:36:49 2019

@author: C830587
"""
#import numpy and pandas
import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library

#read excel in to a data frame
df_raw = pd.read_csv('C:\Users\c830587\Installed\Data-Visualization\Data\Topic_Survey_Assignment.csv')
print(df_raw.columns[0])
#print(df_raw.head())
