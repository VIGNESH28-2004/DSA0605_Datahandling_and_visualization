library(ggplot2)

# Create a dataframe with the provided data
data <- data.frame(
  Date = as.Date(c("01/01/2024", "02/01/2024", "03/01/2024", "04/01/2024", "05/01/2024", "06/01/2024"), format="%m/%d/%Y"),
  Station_A_Temperature = c(25.0, 24.5, 26.2, 23.8, 25.5, 23.0),
  Station_A_Precipitation = c(0.1, 0.0, 0.3, 0.2, 0.1, 0.4),
  Station_B_Temperature = c(23.5, 22.8, 25.0, 22.5, 24.5, 21.8),
  Station_B_Precipitation = c(0.2, 0.3, 0.1, 0.0, 0.4, 0.2)
)

# Reshape the data for plotting
data_long <- tidyr::gather(data, key = "Variable", value = "Value", -Date)

# Create a time series plot
ggplot(data_long, aes(x = Date, y = Value, color = Variable, linetype = Variable)) +
  geom_line() +
  geom_point() +
  labs(title = "Temperature and Precipitation Over Time",
       x = "Date",
       y = "Value",
       color = "Variable",
       linetype = "Variable") +
  theme_minimal()