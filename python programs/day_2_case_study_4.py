import pandas as pd
import plotly.express as px

# Create a DataFrame with the given data
data = {
    'Year': [2019, 2020, 2022, 2023, 2024],
    'Browser': ['Chrome', 'Chrome', 'Chrome', 'Chrome', 'Chrome'],
    'Users': [22.7, 25.8, 28.7, 30.5, 35.2]  
}

df = pd.DataFrame(data)

# Create an interactive line plot using Plotly
fig = px.line(df, x='Year', y='Users', color='Browser', markers=True,
              title='Internet Users Over 5 Years by Browser',
              labels={'Users': 'Number of Users (Millions)', 'Year': 'Year'},
              template='plotly_dark')

# Show the plot
fig.show()
