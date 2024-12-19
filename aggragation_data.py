#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 11:54:28 2024

@author: salama
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from warnings import filterwarnings
import sklearn as sk
sns.set_style('whitegrid')
filterwarnings(action='ignore')


dt = pd.read_csv('Salary_Data.csv')
df = dt.copy()

df.dropna(inplace=True)
df.isnull().sum()
df.shape
df.info()
df.describe()
df.columns =df.columns.str.lower()
#----------------------------------------------------

df[df['gender'].isin('Male')]
df[df['gender'] == 'Male'].count()

# this how select value in quatiery columns
qt = df.gender.value_counts().index.tolist()

# To retrive specific data from columns
df.isin(['Male','PhD']).any() 
#-----------------------------------------------------

df.groupby('gender')['salary'].plot()
plt.show()

df.gender.value_counts().plot(kind='bar')
plt.show()

df.head()
df.columns
df['job title'].value_counts().plot()
plt.show()
#plot age col
df.age.plot()
plt.show()
#--------------------------------------------------------
# aggrigation by groupby
df.groupby(['education level'])['salary'].agg(['min','mean','max','median']).plot(kind='bar',edgecolor='black', kde=True)
plt.xlabel('Category')
plt.ylabel('Salary')
plt.show()

# sort data columsn by Medain
df.groupby(['education level'])['salary'].agg(['min','mean','max','median']).sort_values(by='median')





