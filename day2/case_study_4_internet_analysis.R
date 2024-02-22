# First, let's create a data frame with the given data
data <- data.frame(
  Year = c(2019, 2020, 2022, 2023, 2024),
  Browser = c("Chrome", "Chrome", "Chrome", "Chrome", "Chrome"),
  Users = c(22.7, 25.8, 28.7, 30.5, 35.2)  # Users in millions
)

# Load the plotly library
library(plotly)

# Create an interactive line plot
plot_ly(data, x = ~Year, y = ~Users, color = ~Browser, type = 'scatter', mode = 'lines+markers', name = 'Browser Users', text = ~paste(Browser, Users, "M"), hoverinfo = 'text') %>%
  layout(title = "Internet Users by Browser Over 5 Years",
         xaxis = list(title = "Year"),
         yaxis = list(title = "Users (Millions)"))