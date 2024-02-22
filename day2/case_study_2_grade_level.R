# Install and load the vcd package
install.packages("vcd")
library(vcd)

# Create a data frame from the given dataset
data <- data.frame(SCHOOL = rep(c("A", "B", "C", "D"), each = 3),
                   GRADE_LEVEL = rep(c("Grade 1", "Grade 2", "Grade 3"), 4),
                   NUMBER_OF_STUDENTS = c(25, 30, 20, 22, 28, 18, 20, 25, 15, 28, 32, 24))

# Create a contingency table from the data frame
table_data <- table(data$SCHOOL, data$GRADE_LEVEL)

# Add the number of students to the contingency table
table_data <- addmargins(table_data, FUN = sum)

# Create a mosaic plot from the contingency table
mosaicplot(table_data, main = "Mosaic Plot: Number of Students by School and Grade Level")