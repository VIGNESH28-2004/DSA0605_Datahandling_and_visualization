# Install and load necessary packages
install.packages("ggplot2")
library(ggplot2)

# Given data
traffic_data <- data.frame(
  Date = as.Date(c("2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05")),
  Page_Views = c(1500, 1600, 1400, 1650, 1800),
  Click_Through_Rate = c(2.3, 2.7, 2.0, 2.4, 2.6)
)

# Line Plot for Page Views
ggplot(traffic_data, aes(x = Date, y = Page_Views)) +
  geom_line() +
  labs(title = "Page Views Over Time", x = "Date", y = "Page Views")

# Bar Plot for Click-through Rate
ggplot(traffic_data, aes(x = Date, y = Click_Through_Rate)) +
  geom_bar(stat = "identity", fill = "skyblue") +
  labs(title = "Click-through Rate Over Time", x = "Date", y = "Click-through Rate")

# Scatter Plot for Page Views and Click-through Rate
ggplot(traffic_data, aes(x = Page_Views, y = Click_Through_Rate)) +
  geom_point() +
  labs(title = "Scatter Plot: Page Views vs. Click-through Rate", x = "Page Views", y = "Click-through Rate")
