# Install and load ggplot2 package
if (!requireNamespace("ggplot2", quietly = TRUE)) {
  install.packages("ggplot2")
}
library(ggplot2)

# Create the data
inventory_data <- data.frame(
  ProductID = c(1, 2, 3, 4, 5),
  ProductName = c("Product A", "Product B", "Product C", "Product D", "Product E"),
  QuantityAvailable = c(250, 175, 300, 200, 220)
)

# Stacked Bar Chart
ggplot(inventory_data, aes(x = ProductName, y = QuantityAvailable, fill = ProductName)) +
  geom_bar(stat = "identity") +
  labs(title = "Product Inventory - Stacked Bar Chart", x = "Product Name", y = "Quantity Available")

# Line Plot
ggplot(inventory_data, aes(x = ProductName, y = QuantityAvailable, group = 1)) +
  geom_line() +
  labs(title = "Product Inventory - Line Plot", x = "Product Name", y = "Quantity Available")

# Scatter Plot
ggplot(inventory_data, aes(x = ProductName, y = QuantityAvailable, color = ProductName)) +
  geom_point() +
  labs(title = "Product Inventory - Scatter Plot", x = "Product Name", y = "Quantity Available")

# Pie Plot
ggplot(inventory_data, aes(x = "", y = QuantityAvailable, fill = ProductName)) +
  geom_bar(stat = "pie", width = 1) +
  coord_polar(theta = "y") +
  labs(title = "Product Inventory - Pie Plot", x = NULL, y = NULL)

# Histogram
ggplot(inventory_data, aes(x = QuantityAvailable, fill = ProductName)) +
  geom_histogram(binwidth = 20, position = "identity", alpha = 0.7) +
  labs(title = "Product Inventory - Histogram", x = "Quantity Available", y = "Frequency")