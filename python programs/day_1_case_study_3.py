import matplotlib.pyplot as plt
import pandas as pd

# Create a DataFrame with the given data
data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'Page Views': [1500, 1600, 1400, 1650, 1800],
    'Click-through Rate': [2.3, 2.7, 2.0, 2.4, 2.6]
}

df = pd.DataFrame(data)

# Stacked Bar Chart
df.set_index('Date').plot(kind='bar', stacked=True)
plt.title('Website Analytics - Stacked Bar Chart')
plt.xlabel('Date')
plt.ylabel('Metrics')
plt.show()

# Line Plot
df.set_index('Date')['Page Views'].plot(kind='line', marker='o', label='Page Views')
df.set_index('Date')['Click-through Rate'].plot(secondary_y=True, marker='o', linestyle='--', label='Click-through Rate')
plt.title('Website Analytics - Line Plot')
plt.xlabel('Date')
plt.ylabel('Page Views')
plt.legend(loc='upper left')
plt.show()

# Scatter Plot
plt.scatter(df['Date'], df['Page Views'], label='Page Views', color='blue')
plt.scatter(df['Date'], df['Click-through Rate'], label='Click-through Rate', color='red')
plt.title('Website Analytics - Scatter Plot')
plt.xlabel('Date')
plt.ylabel('Metrics')
plt.legend()
plt.show()

# Pie Plot
plt.pie(df['Page Views'], labels=df['Date'], autopct='%1.1f%%', startangle=90)
plt.title('Website Analytics - Pie Plot (Page Views)')
plt.show()

# Histogram
df.plot(kind='bar', x='Date', y=['Page Views', 'Click-through Rate'])
plt.title('Website Analytics - Histogram')
plt.xlabel('Date')
plt.ylabel('Metrics')
plt.show()
