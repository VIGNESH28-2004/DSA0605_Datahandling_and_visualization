import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame with the given data
data = {
    'Year': [2019, 2020, 2022, 2023, 2024],
    'Job Sector': ['IT', 'Government Job', 'Customer care', 'Bank', 'Games'],
    'Job Seekers Rate': [95, 97, 98, 82, 74],  # in percentage
    'Selection Rate': [25, 12, 45, 20, 35]  # in percentage
}

df = pd.DataFrame(data)

# Plotting the data
plt.figure(figsize=(10, 6))

# Bar plot for Job Seekers Rate
plt.subplot(2, 1, 1)
plt.bar(df['Year'], df['Job Seekers Rate'], color='blue', alpha=0.7)
plt.title('Job Seekers Rate Over 5 Years')
plt.xlabel('Year')
plt.ylabel('Job Seekers Rate (%)')

# Bar plot for Selection Rate
plt.subplot(2, 1, 2)
plt.bar(df['Year'], df['Selection Rate'], color='green', alpha=0.7)
plt.title('Selection Rate Over 5 Years')
plt.xlabel('Year')
plt.ylabel('Selection Rate (%)')

plt.tight_layout()
plt.show()
