import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from statsmodels.graphics.mosaicplot import mosaic

# Create a DataFrame with the given data
data = {
    'Age': ['0-10', '11-30', '31-50', '51-80'],
    'Dairy': [50, 35, 25, 40],
    'Staple Food': [30, 45, 55, 40],
    'High-Calorie Food': [10, 15, 13, 4],
    'Supplements': [10, 5, 7, 16]
}

df = pd.DataFrame(data)

# Stacked Bar Chart
df.set_index('Age').plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart')
plt.xlabel('Age Group')
plt.ylabel('Daily Consumption')
plt.show()

# Line Plot
df.set_index('Age').plot(kind='line', marker='o')
plt.title('Line Plot')
plt.xlabel('Age Group')
plt.ylabel('Daily Consumption')
plt.show()

# Scatter Plot
plt.scatter(df['Age'], df['Dairy'], label='Dairy')
plt.scatter(df['Age'], df['Staple Food'], label='Staple Food')
plt.scatter(df['Age'], df['High-Calorie Food'], label='High-Calorie Food')
plt.scatter(df['Age'], df['Supplements'], label='Supplements')
plt.title('Scatter Plot')
plt.xlabel('Age Group')
plt.ylabel('Daily Consumption')
plt.legend()
plt.show()

# Mosaic Plot
mosaic_df = pd.melt(df, id_vars=['Age'], value_vars=['Dairy', 'Staple Food', 'High-Calorie Food', 'Supplements'])
plt.figure(figsize=(10, 6))
mosaic(mosaic_df, ['Age', 'variable'], title='Mosaic Plot')
plt.xlabel('Age Group')
plt.ylabel('Variable')
plt.show()

# Histogram
df.plot(kind='bar', x='Age', y=['Dairy', 'Staple Food', 'High-Calorie Food', 'Supplements'], stacked=True)
plt.title('Histogram')
plt.xlabel('Age Group')
plt.ylabel('Daily Consumption')
plt.show()
