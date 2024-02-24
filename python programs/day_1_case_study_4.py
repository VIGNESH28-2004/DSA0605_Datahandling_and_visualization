import matplotlib.pyplot as plt
import pandas as pd

# Create a DataFrame with the given data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May'],
    'Sales': [15000, 18000, 22000, 20000, 23000]
}

df = pd.DataFrame(data)

# Scatter Plot
plt.scatter(df['Month'], df['Sales'], label='Sales', color='blue')
plt.title('Time Series Analysis - Scatter Plot')
plt.xlabel('Month')
plt.ylabel('Sales (in $)')
plt.legend()
plt.show()

# Line Graph
plt.plot(df['Month'], df['Sales'], marker='o', linestyle='-', color='green')
plt.title('Time Series Analysis - Line Graph')
plt.xlabel('Month')
plt.ylabel('Sales (in $)')
plt.show()
