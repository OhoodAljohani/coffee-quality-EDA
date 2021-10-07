# %%
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt 
import numpy as np
import os 
import pandas as pd # 
# %%
df=pd.read_csv("https://raw.githubusercontent.com/jldbc/coffee-quality-database/master/data/arabica_data_cleaned.csv")
# 
'''
dataset shape and info
'''
print("The data has "+str(df.shape[0])+" Rows and "+str(df.shape[1])+" Columns")
# %%
df.info()
# %%
'''
helper function to plot the data : 
1- plot_ColumnDistribution to plot data columns
2- plotCorr to plot corr 
'''
def plot_ColumnDistribution(df, nGraphShown, nGraphPerRow):
    nunique = df.nunique()
    df = df[[col for col in df if nunique[col] > 1 and nunique[col] < 50]] # For displaying purposes, pick columns that have between 1 and 50 unique values
    nRow, nCol = df.shape
    columnNames = list(df)
    nGraphRow = (nCol + nGraphPerRow - 1) / nGraphPerRow
    plt.figure(num = None, figsize = (6 * nGraphPerRow, 8 * nGraphRow), dpi = 80, facecolor = 'w', edgecolor = 'k')
    for i in range(min(nCol, nGraphShown)):
        plt.subplot(nGraphRow, nGraphPerRow, i + 1)
        columnDf = df.iloc[:, i]
        if (not np.issubdtype(type(columnDf.iloc[0]), np.number)):
            valueCounts = columnDf.value_counts()
            valueCounts.plot.bar()
        else:
            columnDf.hist()
        plt.ylabel('counts')
        plt.xticks(rotation = 90)
        plt.title(f'{columnNames[i]} (column {i})')
    plt.tight_layout(pad = 1.0, w_pad = 1.0, h_pad = 1.0)
    plt.show()
def plotCorr(df, graphWidth):
    df = df.dropna('columns') # drop columns with NaN
    df = df[[col for col in df if df[col].nunique() > 1]] # keep columns where there are more than 1 unique values
    if df.shape[1] < 2:
        print(f'No correlation plots shown: The number of non-NaN or constant columns ({df.shape[1]}) is less than 2')
        return
    corr = df.corr()
    plt.figure(num=None, figsize=(graphWidth, graphWidth), dpi=80, facecolor='w', edgecolor='k')
    corrMat = plt.matshow(corr, fignum = 1)
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.gca().xaxis.tick_bottom()
    plt.colorbar(corrMat)

    plt.show()
# %%
df.head()
plot_ColumnDistribution(df, 10, 5)
# %%
plotCorr(df, 10)
# %%
df.isna().sum()
# %%
df =df.drop(["Lot.Number","Unnamed: 0"],axis=1)
# %%
plot_ColumnDistribution(df, 10, 5)
plotCorr(df, 10)
# %%
print("The data has "+str(df.shape[0])+" Rows and "+str(df.shape[1])+" Columns")
# %%
#df = df.dropna(how='any',axis=0)
# %%
print("The data has "+str(df.shape[0])+" Rows and "+str(df.shape[1])+" Columns")
# %%
## Some EDA on Processing.Method and Flavor
from plotnine import ggplot, aes, geom_line ,geom_point,geom_histogram,geom_boxplot
ggplot(df) + aes(x="Processing.Method", y="Flavor")+ geom_boxplot()
