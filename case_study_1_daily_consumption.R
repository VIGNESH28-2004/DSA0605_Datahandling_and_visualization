# Install and load necessary packages
install.packages(c("ggplot2"))
library(ggplot2)

# Given data
data <- data.frame(
  Age = c("0-10", "11-30", "31-50", "51-80"),
  Dairy = c(50, 35, 25, 40),
  Staple_Food = c(30, 45, 55, 40),
  High_CalorieFood = c(10, 15, 13, 4),
  Supplements = c(10, 5, 7, 16)
)

# Reshape the data for plotting
data_long <- tidyr::gather(data, key = "Category", value = "Value", -Age)

# Stacked Bar Chart
ggplot(data_long, aes(x = Age, y = Value, fill = Category)) +
  geom_bar(stat = "identity", position = "stack") +
  labs(title = "Stacked Bar Chart", x = "Age Group", y = "Daily Consumption")

# Line Plot
ggplot(data_long, aes(x = Age, y = Value, color = Category, group = Category)) +
  geom_line() +
  labs(title = "Line Plot", x = "Age Group", y = "Daily Consumption")

# Scatter Plot
ggplot(data_long, aes(x = Age, y = Value, color = Category)) +
  geom_point() +
  labs(title = "Scatter Plot", x = "Age Group", y = "Daily Consumption")

# Histogram
ggplot(data_long, aes(x = Value, fill = Category)) +
  geom_histogram(binwidth = 5, position = "identity", alpha = 0.7) +
  labs(title = "Histogram", x = "Daily Consumption", y = "Frequency")
