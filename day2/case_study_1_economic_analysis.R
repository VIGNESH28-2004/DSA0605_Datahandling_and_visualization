# Create a dataframe with the provided data
data <- data.frame(
  Month = month.abb,
  Economic_Condition = c("Good", "Good", "Good", "Good", "Fair", "Fair", "Good", "Bad", "Fair", "Good", "Bad", "Fair"),
  Unemployment_Rate = c(10.7, 9.8, 10.2, 11.2, 15.75, 17.8, 19.4, 25.6, 18.6, 15.6, 26.7, 19.5)
)

# Convert Month to a factor with ordered levels
data$Month <- factor(data$Month, levels = month.abb, ordered = TRUE)

# Create a time series object
ts_data <- ts(data$Unemployment_Rate, frequency = 12, start = c(1, 1))

# Fit a linear model to capture the trend
trend_model <- lm(ts_data ~ as.numeric(time(ts_data)))

# Extract the trend component
trend_component <- as.vector(fitted(trend_model))

# Calculate the remainder component
remainder_component <- ts_data - trend_component

# Plot the original time series
plot(data$Month, data$Unemployment_Rate, type = "b", main = "Unemployment Rate Over Time", xlab = "Month", ylab = "Unemployment Rate")

# Plot the trend component
lines(data$Month, trend_component, col = "red")

# Plot the remainder (residual) component
lines(data$Month, remainder_component, col = "blue")

# Create a legend
legend("topright", legend = c("Original", "Trend", "Residual"), col = c("black", "red", "blue"), lty = 1:1, cex = 0.8)
