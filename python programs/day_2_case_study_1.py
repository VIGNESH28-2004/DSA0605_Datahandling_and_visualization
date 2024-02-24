import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Create a DataFrame with the given data
data = {
    'Month': ['Jan', 'Feb', 'March', 'April', 'May', 'Jun', 'July', 'August', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Economic Condition': ['Good', 'Good', 'Good', 'Good', 'Fair', 'Fair', 'Good', 'Bad', 'Fair', 'Good', 'Bad', 'Fair'],
    'Unemployment Rate': [10.7, 9.8, 10.2, 11.2, 15.75, 17.8, 19.4, 25.6, 18.6, 15.6, 26.7, 19.5]
}

df = pd.DataFrame(data)

# Convert 'Month' to datetime format for proper time-series analysis
df['Month'] = pd.to_datetime(df['Month'], format='%b', errors='coerce')

# Set 'Month' as the index
df.set_index('Month', inplace=True)

# Time-series decomposition with a shorter seasonal period
result = seasonal_decompose(df['Unemployment Rate'], model='multiplicative', period=6)

# Visualize the original time series
plt.figure(figsize=(12, 6))
plt.subplot(4, 1, 1)
plt.plot(df['Unemployment Rate'], label='Original Time Series')
plt.title('Original Time Series')
plt.legend()

# Visualize the trend component
plt.subplot(4, 1, 2)
plt.plot(result.trend, label='Trend Component', color='orange')
plt.title('Trend Component')
plt.legend()

# Visualize the seasonal component
plt.subplot(4, 1, 3)
plt.plot(result.seasonal, label='Seasonal Component', color='green')
plt.title('Seasonal Component')
plt.legend()

# Visualize the residual component
plt.subplot(4, 1, 4)
plt.plot(result.resid, label='Residual Component', color='red')
plt.title('Residual Component')
plt.legend()

plt.tight_layout()
plt.show()
