# First, let's create a data frame with the given data
data <- data.frame(
  Year = c(2019, 2020, 2022, 2023, 2024),
  Job_Sector = c("IT", "Government Job", "Customer care", "Bank", "Games"),
  Job_Seekers_Rate = c(95, 97, 98, 82, 74),
  Selection_Rate = c(25, 12, 45, 20, 35)
)

# Now, let's create a bar plot showing the Job Sectors over the years
library(ggplot2)

ggplot(data, aes(x = as.factor(Year), y = Job_Seekers_Rate, fill = Job_Sector)) +
  geom_bar(stat = "identity", position = "dodge") +
  labs(title = "Most Common Jobs by State Over 5 Years",
       x = "Year",
       y = "Job Seekers Rate") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))