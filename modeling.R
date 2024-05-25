library(tidyverse)
library(estimatr)

data <- read.csv("data111_cleaned.csv")

data$internet_usage <- data$X3months_use_per_week

model <- lm(life_satisfaction_0to10 ~ internet_usage, data = data)
summ <- summary(model)
print(summ$coefficients[8])

for(age in unique(data$age_range)){
    data_filter <- data[data$age_range == age,]
    model <- lm(life_satisfaction_0to10 ~ internet_usage, data = data_filter)
    summ <- summary(model)
    print(summ$coefficients[8])}  
