#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: salama
"""

import pandas as pd

import matplotlib.pyplot as plt
import sklearn as sk
import seaborn as sns
from warnings import filterwarnings
import numpy as np
sns.set_style('whitegrid')
filterwarnings(action='ignore')
# load data


df = pd.read_csv('Salary_Data.csv')
df.columns = df.columns.str.lower()

df.head(3)
df.iloc[2]  # to show index one row
df.iloc[2:10]  # to retrive index specific rows
df.iloc[2:10, 0:2]  # retrive specific col and row
df.info()  # information about data object or strin or int
df.shape
df.index
len(df)
df.count()
df.describe()
df.gender.unique()  # or df.col.value_counts
df[df.gender == 'Male']  # to retrive specific according to Male
df[(df.gender == 'Female') & (df.age > 20)]

df[df.age >= 25 and df.gender == 'Male']
# df[(df.age >= 25]) and df[(df.gender=='Male'])

df[(df.gender == 'Male') and (df[df.salary] < 90000.0)]

df.loc[(df.gender == 'Male') | (df.age < 25)].plot()
plt.show()

df.loc[(df.gender == 'Female') | (df.age < 25)].plot()
plt.show()

df.columns = df.columns.str.replace(' ', "_")
# retrieve data accroding to the specific query
df.loc[(df.salary == 90000.0) | (df.years_of_experience < 7.0)]

df.head()
df.job_title
df.columns
df.groupby(['job_title', 'gender'])['age'].median().plot()
plt.show()

df.groupby(['gender'])['age'].median().plot()
plt.show()

df.groupby(['gender'])['salary'].agg(['min', 'max', 'median']).plot()
plt.show()


stic_value = df.groupby(['gender'])['salary'].agg(['min', 'max', 'median'])

print(f'{stic_value:,.1f}')

v = 1000000
print(f'{v:,.1f}')
# --------------------------------------------------------
df.job_title.value_counts().count()  # number of quigery
# to select specific value in columns
df['job_title'].isin(['Software Engineer'])
# value wheather existing on this col or not
df['job_title'].isin(['Software Engineer']).any()
# how me only data that belog to softwaree engineer
df[df['job_title'] == 'Software Engineer']
df[df['job_title'] == 'Software Engineer'].agg(['min', 'max', 'median'])
soft_eng = df[df['job_title'] == 'Software Engineer']
# if columns incluing Nan value you can ignore this columns/ age col has Nan value only check
soft_eng[soft_eng['age'].notna()]
df.dropna(inplace=True)

soft_eng = df[df['job_title'] == 'Software Engineer']

soft_eng.groupby('gender')['salary'].agg(['min', 'max', 'median'])

df.isin(['software_engineer']).any()

df.head(5)

df[(df.gender == 'Male') & (df.salary > 90000)]
df['gender'].value_counts().plot(kind='pie', explode=[0.1, 0, 0])
plt.show()


df.head(5)


df.groupby('gender')['salary'].count().plot(kind='pie', explode=[.1, 0, 0])
plt.show()

plt.hist(x=df['salary'], bins=30, edgecolor='black')
plt.show()


sns.histplot(x=df['salary'], kde=True, bins=30, edgecolor='red')
plt.show()

sns.histplot(x=df['salary'], bins=40, edgecolor='red', hue=df['gender'])
plt.show()

sns.histplot(x=df['salary'], bins=15, hue=df['gender'])
plt.show()


# sns.histplot(data=df,x='salary',discrete=True,stat='probability')
# plt.show()

df.head(5)

min_salary = df.groupby('gender')['salary'].agg('min')
mean_salary   =df.groupby('gender')['salary'].agg('mean')
max_salary    = df.groupby('gender')['salary'].agg('max')
median_salary = df.groupby('gender')['salary'].agg('median') 
print(f'Min:{min_salary} \n Mean:{mean_salary} \n Max:{max_salary} \n Median:{median_salary}')



df.groupby('age')['salary'].agg('median').plot()
plt.show()
df.groupby('age')['salary'].agg('mean').plot()
plt.show()
df.groupby('age')['salary'].agg('min').plot()
plt.show()
df.groupby('age')['salary'].agg(['max','min','mean','median']).plot()
plt.show()

df.groupby('age')['salary'].agg('min')












