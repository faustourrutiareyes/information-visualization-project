library(tidyverse)

df <- read_csv("data111_renamed_cols.csv")

df_quickgraph <- df[c("3months_use_per_week", "health_info_lookup")]

df_quickgraph <- df_quickgraph[!df_quickgraph$"3months_use_per_week" %in% c(98, 99), ]

lapply(df_quickgraph, unique)

df_quickgraph$"3months_use_per_week" <- as.factor(df_quickgraph$"3months_use_per_week")

table_plot <- as.data.frame(table(df_quickgraph$"3months_use_per_week", df_quickgraph$"health_info_lookup"))
table_plot

ggplot() +
    geom_col(data = table_plot, aes(x = Var1, y = Freq, fill = Var2), position = "dodge") +
    labs(
        title = "Health Information Lookup by Frequency of Internet Use",
        x = "Frequency of Internet Use",
        y = "Number of Participants",
        fill = "Health Information Lookup"
    )
