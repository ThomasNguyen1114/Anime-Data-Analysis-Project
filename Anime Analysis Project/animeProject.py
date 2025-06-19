import pandas as pd
import numpy as np
import scipy.stats as sp
import statsmodels.stats.multicomp as stats
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

#1
animeData = pd.read_csv('anime.csv')
animeData.fillna(0, inplace = True)

#2
print(animeData.describe(), "\n")
ratingFrequency = animeData['rating'].value_counts()
print("Frequency: ", "\n", ratingFrequency)
ratingMean = animeData['rating'].mean()
print("Mean: ", round(ratingMean, 2))
ratingMode = animeData['rating'].mode()[0]
print("Mode: ", ratingMode)
ratingMedian = animeData['rating'].median()
print("Median: ", ratingMedian)
ratingStandardDeviation = animeData['rating'].std()
print("Standard Deviation: ", round(ratingStandardDeviation, 2), "\n")

#3
#a) Correlation
#b) I need 2 variables - Rating & Members
    #i) N0: There is no correlation between rating and members.
    #i) NA: There is a correlation between rating and members.
#c)
animeDataCorr = sp.pearsonr(animeData['rating'], animeData['members'])
print("Correlation Coefficient: ", round(animeDataCorr[0], 2))
print("P-Value: \t\t ", round(animeDataCorr[1], 2), "\n")

#4
#Correlation Coefficient = .31 - this tells us that there is a positive linear relationship between rating and members - the higher the rating, then higher the amount of members there are - Moderate Positive Correlation.
#P-Value = 0 - this tells us there is a significant relationship between rating and members - We reject the null hypothesis and accept the alternative hypothesis.

#5
plt.figure(figsize=(10, 6))
sns.scatterplot(x='rating', y='members', data=animeData, color='blue')
plt.title('Rating vs. Number of Members', fontsize=16)
plt.xlabel('Rating', fontsize=12)
plt.ylabel('Number of Members', fontsize=12)
plt.yticks([0, 200000, 400000, 600000, 800000, 1000000], ['0', '200K', '400K', '600K', '800K', '1M'])
plt.show()


