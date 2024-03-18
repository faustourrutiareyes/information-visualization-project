library(tidyverse)

# World Bank Data Library
library("wbstats")

internet_pop <- read.csv("datafiles\\share-of-individuals-using-the-internet.csv")

internet_pop <- internet_pop[internet_pop$Code != "", ] %>% drop_na()

available_data_world_bank_gdp <- wb_search("GDP")
available_data_world_bank_employment <- wb_search("employment")
available_data_world_bank_internet <- wb_search("internet")

my_indicators <- c(
    "gdp_capita" = "NY.GDP.PCAP.CD",
    "employment_ratio" = "SL.EMP.TOTL.SP.ZS",
    "internet_users_ratio" = "IT.NET.USER.ZS"
)

wb_df <- wb_data(my_indicators, start_date = 1990, end_date = 2012)

write.csv(wb_df, "datafiles\\wb_df.csv")


