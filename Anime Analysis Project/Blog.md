# 🌸 Exploring Anime Ratings and Popularity: What Drives Viewer Interest?

## ✨ Introduction

Anime has become a global phenomenon, captivating fans with rich stories and unique art styles. But what makes an anime popular? In this project, I analyzed a dataset of anime ratings and membership counts to understand how viewer ratings relate to the size of the anime’s fanbase.

## 🔍 Objective

The goal was to:
- Clean and explore the anime dataset.
- Calculate key statistics for anime ratings.
- Examine the correlation between anime ratings and number of members.
- Visualize the relationship with a scatter plot.
- Gain insights about how rating influences popularity.

## 🗂 Dataset Overview

The `anime.csv` dataset includes:
- `rating`: Viewer rating of each anime.
- `members`: Number of members (fans) following the anime.
- Other metadata fields (not the main focus here).

## 🧹 Step 1: Data Cleaning

I handled missing values by filling `NaN`s with zeros for a clean analysis:

```python
animeData.fillna(0, inplace=True)
```

## 📊 Step 2: Descriptive Statistics
Calculated key statistics for the ratings column:

- **Mean rating**
- **Mode rating**
- **Median rating**
- **Standard deviation**

These numbers help summarize how viewers generally rate anime.

## 🔍 Step 3: Correlation Analysis
Using Pearson’s correlation coefficient, I tested the hypothesis:

- **Null Hypothesis (H0): No correlation between rating and membership count.**
- **Alternative Hypothesis (HA): There is a correlation between rating and membership count.**

Results:
```
Correlation Coefficient: 0.31
P-Value: 0.00
```
This shows a moderate positive correlation between higher ratings and more members. The low p-value indicates the correlation is statistically significant.

## 📈 Step 4: Visualization
I created a scatter plot of rating vs. members to visualize the relationship:

```
sns.scatterplot(x='rating', y='members', data=animeData, color='blue')
```

The plot shows that higher-rated anime generally attract more members, though the relationship isn’t perfectly linear.

## 🧰 Tools Used
- **Python (with pandas, numpy, scipy, statsmodels, seaborn, matplotlib)**
- **Visual Studio Code**

## 📎 How to Run
1. Download the dataset and script.
2. Make sure both are in the same folder.
3. Install dependencies:
```
pip install pandas matplotlib seaborn
```
4. Run the script:
```
python animeProject.py
```

## 🎯 Conclusion
This analysis confirms that anime ratings have a moderate but significant impact on fan membership size. It also demonstrates important data science techniques like statistical testing, correlation analysis, and visual storytelling with data.