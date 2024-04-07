# World Bank Data Library
library("wbstats")

# Set up the indicators 
my_indicators <- c(
    "gdp_capita" = "NY.GDP.PCAP.CD",
    "employment_ratio" = "SL.EMP.TOTL.SP.ZS",
    "internet_users_ratio" = "IT.NET.USER.ZS",
    "gdp_capita_growth" = "NY.GDP.PCAP.KD.ZG"
)

# Set up the years
start_year <- 1990
end_year <- 2024

# Download the data
wb_df <- wb_data(my_indicators, start_date = start_year, end_date = end_year)

# Create back-up of data
write.csv(wb_df, "datafiles\\wb_df.csv")
