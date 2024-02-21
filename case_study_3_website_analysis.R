# Install and load necessary packages
if (!requireNamespace("ggplot2", quietly = TRUE)) {
  install.packages("ggplot2")
}
library(ggplot2)

# Given data
analytics_data <- data.frame(
  Date = as.Date(c("2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05")),
  Page_Views = c(1500, 1600, 1400, 1650, 1800),
  Click_Through_Rate = c(2.3, 2.7, 2.0, 2.4, 2.6)
)

# Stacked Bar Chart
ggplot(analytics_data, aes(x = Date, y = Page_Views, fill = factor(Click_Through_Rate))) +
  geom_bar(stat = "identity") +
  labs(title = "Website Analytics - Stacked Bar Chart", x = "Date", y = "Page Views")

# Line Plot
ggplot(analytics_data, aes(x = Date, y = Page_Views)) +
  geom_line() +
  labs(title = "Website Analytics - Line Plot", x = "Date", y = "Page Views")

# Scatter Plot
ggplot(analytics_data, aes(x = Date, y = Click_Through_Rate)) +
  geom_point() +
  labs(title = "Website Analytics - Scatter Plot", x = "Date", y = "Click-through Rate")

# Pie Plot
ggplot(analytics_data, aes(x = "", y = Page_Views, fill = factor(Click_Through_Rate))) +
  geom_bar(stat = "pie", width = 1) +
  coord_polar(theta = "y") +
  labs(title = "Website Analytics - Pie Plot", x = NULL, y = NULL)

# Histogram
ggplot(analytics_data, aes(x = Page_Views)) +
  geom_histogram(binwidth = 100, position = "identity", alpha = 0.7) +
  labs(title = "Website Analytics - Histogram", x = "Page Views", y = "Frequency")
