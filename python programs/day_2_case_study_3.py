import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame with the given data
data = {
    'Date': ['01/01/2024', '02/01/2024', '03/01/2024', '04/01/2024', '05/01/2024', '06/01/2024'],
    'Station A Temperature': [25.0, 24.5, 26.2, 23.8, 25.5, 23.0],
    'Station A Precipitation': [0.1, 0.0, 0.3, 0.2, 0.1, 0.4],
    'Station B Temperature': [23.5, 22.8, 25.0, 22.5, 24.5, 21.8],
    'Station B Precipitation': [0.2, 0.3, 0.1, 0.0, 0.4, 0.2]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

# Plotting the time series
plt.figure(figsize=(12, 6))

# Temperature plot
plt.subplot(2, 1, 1)
plt.plot(df['Date'], df['Station A Temperature'], label='Station A')
plt.plot(df['Date'], df['Station B Temperature'], label='Station B')
plt.title('Temperature Time Series')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend()

# Precipitation plot
plt.subplot(2, 1, 2)
plt.plot(df['Date'], df['Station A Precipitation'], label='Station A')
plt.plot(df['Date'], df['Station B Precipitation'], label='Station B')
plt.title('Precipitation Time Series')
plt.xlabel('Date')
plt.ylabel('Precipitation (mm)')
plt.legend()

plt.tight_layout()
plt.show()
