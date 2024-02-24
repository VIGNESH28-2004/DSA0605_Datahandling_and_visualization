import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from statsmodels.graphics.mosaicplot import mosaic

# Create a DataFrame with the given data
data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'Page Views': [1500, 1600, 1400, 1650, 1800],
    'Click-through Rate': [2.3, 2.7, 2.0, 2.4, 2.6]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])  # Convert 'Date' column to datetime format

# Line Plot
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Page Views'], marker='o', label='Page Views')
plt.plot(df['Date'], df['Click-through Rate'], marker='o', label='Click-through Rate')
plt.title('Website Traffic Analysis - Line Plot')
plt.xlabel('Date')
plt.ylabel('Metrics')
plt.legend()
plt.show()

# Scatter Plot
plt.figure(figsize=(10, 5))
plt.scatter(df['Date'], df['Page Views'], label='Page Views', color='blue')
plt.scatter(df['Date'], df['Click-through Rate'], label='Click-through Rate', color='red')
plt.title('Website Traffic Analysis - Scatter Plot')
plt.xlabel('Date')
plt.ylabel('Metrics')
plt.legend()
plt.show()

# Stacked Bar Chart
df.set_index('Date').plot(kind='bar', stacked=True)
plt.title('Website Traffic Analysis - Stacked Bar Chart')
plt.xlabel('Date')
plt.ylabel('Metrics')
plt.show()

# Histogram
df.plot(kind='bar', x='Date', y=['Page Views', 'Click-through Rate'])
plt.title('Website Traffic Analysis - Histogram')
plt.xlabel('Date')
plt.ylabel('Metrics')
plt.show()

# Pie Plot
plt.figure(figsize=(8, 8))
plt.pie(df['Page Views'], labels=df['Date'], autopct='%1.1f%%', startangle=90)
plt.title('Website Traffic Analysis - Pie Plot (Page Views)')
plt.show()

#Mosaic plot
plt.figure(figsize=(10, 6))
mosaic_df = pd.melt(df, id_vars=['Date'], value_vars=['Page Views', 'Click-through Rate'])
mosaic(mosaic_df, ['variable', 'Date'], title='Website Traffic Analysis - Mosaic Plot', gap=0.05)
plt.show()