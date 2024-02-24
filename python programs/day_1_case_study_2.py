import matplotlib.pyplot as plt
import pandas as pd

# Create a DataFrame with the given data
data = {
    'Product ID': [1, 2, 3, 4, 5],
    'Product Name': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],
    'Quantity Available': [250, 175, 300, 200, 220]
}

df = pd.DataFrame(data)

# Stacked Bar Chart
df.set_index('Product Name')['Quantity Available'].plot(kind='bar', stacked=True)
plt.title('Product Inventory - Stacked Bar Chart')
plt.xlabel('Product Name')
plt.ylabel('Quantity Available')
plt.show()

# Line Plot
df.set_index('Product Name')['Quantity Available'].plot(kind='line', marker='o')
plt.title('Product Inventory - Line Plot')
plt.xlabel('Product Name')
plt.ylabel('Quantity Available')
plt.show()

# Scatter Plot
plt.scatter(df['Product Name'], df['Quantity Available'], label='Quantity Available', color='blue')
plt.title('Product Inventory - Scatter Plot')
plt.xlabel('Product Name')
plt.ylabel('Quantity Available')
plt.legend()
plt.show()

# Pie Plot
plt.pie(df['Quantity Available'], labels=df['Product Name'], autopct='%1.1f%%', startangle=90)
plt.title('Product Inventory - Pie Plot')
plt.show()

# Histogram
df.plot(kind='bar', x='Product Name', y='Quantity Available')
plt.title('Product Inventory - Histogram')
plt.xlabel('Product Name')
plt.ylabel('Quantity Available')
plt.show()
