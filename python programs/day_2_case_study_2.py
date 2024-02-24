import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic
from scipy.stats import chi2_contingency

# Create a DataFrame with the given data
data = {
    'SCHOOL': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'D', 'D', 'D'],
    'GRADE LEVEL': ['Grade 1', 'Grade 2', 'Grade 3'] * 4,
    'NUMBER OF STUDENTS': [25, 30, 20, 22, 28, 18, 20, 25, 15, 28, 32, 24]
}

df = pd.DataFrame(data)

# Create a contingency table for the mosaic plot
contingency_table = pd.pivot_table(df, values='NUMBER OF STUDENTS', index='SCHOOL', columns='GRADE LEVEL', fill_value=0)

# Mosaic Plot
plt.figure(figsize=(10, 6))
mosaic(contingency_table.unstack(), title='Mosaic Plot')
plt.show()

# Chi-squared test for independence
chi2, p, _, _ = chi2_contingency(contingency_table)

# Analyze efficiency
if p < 0.05:
    print(f"The mosaic plot suggests an association between SCHOOL and GRADE LEVEL (p-value: {p:.4f}).")
else:
    print("The mosaic plot does not provide strong evidence of an association between SCHOOL and GRADE LEVEL.")

print(f"Chi-squared statistic: {chi2:.4f}")
