# -*- coding: utf-8 -*-
"""visualize.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KlUGk3ZsPxsUPMBOnnZTVu4_cERbTgtz
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/Wholesale customers data.csv')

df

df.head()

df.tail()

df.shape

df.columns

df.dtypes

df.info()

df.duplicated().sum()

plt.figure(figsize=(5, 2))
sns.barplot(x='Region', y='Grocery', data=df)
plt.xlabel('Region')
plt.ylabel('Grocery Spending')
plt.title('Grocery Spending by Region')
plt.show()

plt.figure(figsize=(5, 2))
sns.histplot(data=df, x='Grocery', bins=20, kde=True, color='skyblue')
plt.xlabel('Grocery Spending')
plt.ylabel('Frequency')
plt.title('Grocery Spending Distribution')
plt.show()

fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(15, 15))
fig.suptitle('Bar Charts and Histograms for Wholesale Distributor Data', y=1.02)

# Flatten the 3x3 array of subplots into a 1D array
axes = axes.flatten()

# Loop through each column and create bar chart and histogram
for i, column in enumerate(df.columns):
    # Bar chart
    sns.barplot(x='Region', y=column, data=df, ax=axes[i])
    axes[i].set_title(f'Bar Chart - {column} by Region')

# Adjust layout for better spacing
plt.tight_layout()

# Display the plots
plt.show()

# Set up subplots
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(15, 15))
fig.suptitle('Histograms for Wholesale Distributor Data', y=1.02)

# Flatten the 3x3 array of subplots into a 1D array
axes = axes.flatten()

# Loop through each column and create histogram
for i, column in enumerate(df.columns):
    # Histogram
    sns.histplot(data=df, x=column, bins=20, kde=True, color='skyblue', ax=axes[i])
    axes[i].set_title(f'Histogram - {column} Distribution')

# Adjust layout for better spacing
plt.tight_layout()

# Display the plots
plt.show()

sns.pairplot(df)
plt.suptitle('Pair Plot of Wholesale Distributor Data', y=1.02)
plt.show()

columns_of_interest = ['Fresh', 'Milk', 'Grocery', 'Frozen', 'Detergents_Paper', 'Delicassen']
sns.pairplot(df[columns_of_interest])
plt.suptitle('Pair Plot of Selected Columns', y=1.02)
plt.show()