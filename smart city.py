import matplotlib
import pandas as pd
pd.plotting.register_matplotlib_converters()
import numpy as np
import scipy
import math
import collections

import seaborn as sns
import matplotlib.pyplot as plt
matplotlib in line

file.columns
file.replace(" ", "")
file.columns=file.columns.str.replace(' ', '')
sci=file.drop(columns='Id')
sci=sci.drop(columns='SmartCity_Index_relative_Edmonton', ).sort_values('SmartCity_Index', ascending=False)
scimean = sci.groupby('Country').median().astype(int).sort_values('SmartCity_Index', ascending=False).head(10)
scimean.style.background_gradient(cmap="GnBu")
sci.describe()
plt.figure(figsize=(16,6))
sns.boxplot(data=sci, showmeans=True, palette='pastel')
sns.set_style('whitegrid')
plt.title('Boxplot of Smart City Subindexes', fontsize = 15)
scimean = sci.groupby('Country').median().astype(int).sort_values('SmartCity_Index', ascending=False)
sns.scatterplot(data=scimean)
sns.set_style('whitegrid')
plt.ylabel('Countries', fontsize = 10)
plt.title('Smart City Subindexes per Country', fontsize = 15)
ticks=plt.xticks(rotation=90)
sns.set_theme()
scihist=sci.hist(figsize=(20, 10))
scihist
fig = plt.figure()
res1 = scipy.stats.probplot(sci['SmartCity_Index'], plot=plt)
res2 = scipy.stats.probplot(sci['Smart_Living'], plot=plt)
res3 = scipy.stats.probplot(sci['Smart_Government'], plot=plt)
plt.show()
scicorr=sci.copy()
sns.set_theme()
plt.figure(figsize=(8, 10))
sns.pairplot(scicorr, kind='scatter', corner=True, height=1.5)
plt.show()
corr=sci.corr('spearman')
corrstyle=sci.corr('spearman').style.background_gradient(cmap="GnBu") #  copy of the dataframe to avoid problems with Styler object
corrstyle.format('{:.2f}')

res= scipy.stats.spearmanr(sci['SmartCity_Index'], sci['Smart_Living'])
print('Smart Living correlation to Smart City Index')
print('Spearman`s coefficient:', res[0])
print('p-value:', res[1])

res= scipy.stats.pearsonr(sci['SmartCity_Index'], sci['Smart_Government'])
print('Smart Government correlation to Smart City Index')
print('Spearman`s coefficient:', res[0])
print('p-value:', res[1])

res= scipy.stats.pearsonr(sci['SmartCity_Index'], sci['Smart_People'])
print('Smart People correlation to Smart City Index')
print('Spearman`s coefficient:', res[0])
print('p-value:', res[1])
res= scipy.stats.pearsonr(sci['SmartCity_Index'], sci['Smart_Environment'])
print('Smart Environment correlation to Smart City Index')
print('Spearman`s coefficient:', res[0])
print('p-value:', res[1])

# Plots
g = sns.PairGrid(sci, y_vars=['SmartCity_Index'], x_vars=['Smart_People', 'Smart_Government', 'Smart_Living', 'Smart_Environment'])
g.map(sns.regplot)
g.set()