# Install and load necessary packages
install.packages("ggplot2")
library(ggplot2)

# Given data
data <- data.frame(
  Month = c("January", "February", "March", "April", "May"),
  Sales = c(15000, 18000, 22000, 20000, 23000)
)

# Line Plot
ggplot(data, aes(x = Month, y = Sales, group = 1)) +
  geom_line() +
  labs(title = "Line Graph of Monthly Sales", x = "Month", y = "Sales (in $)")

#scatter plot
ggplot(data, aes(x = Month, y = Sales)) +
  geom_point() +
  labs(title = "Scatter Plot of Monthly Sales", x = "Month", y = "Sales (in $)")