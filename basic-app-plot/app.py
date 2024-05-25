import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import ticker

# Import data from shared.py
from shared import df_mean, line_mean
from shiny.express import input, render, ui

# Page title (with some additional top padding)
ui.page_opts(
    title=ui.h2(
        "A Study of The Relationship Between Screen Time And Life Satisfaction of Different Age Groups In Taiwan"
    )
)

with ui.sidebar(width="40%"):
    ui.input_checkbox_group(
        "checkbox_age_group",
        "Age group",
        {
            1: "12-14 years old",
            2: "15-19 years old",
            3: "20-29 years old",
            4: "30-39 years old",
            5: "40-49 years old",
            6: "50-59 years old",
            7: "60-69 years old",
            8: "70-79 years old",
        }
    )

    


with ui.card(height="100%"):

    ui.h4("Life Satisfaction from 0 to 10")
    
    @render.plot
    def hist():
        # Create the plot and axes
        fig, ax = plt.subplots()

        ages_dict = {
            1: "12-14 years old",
            2: "15-19 years old",
            3: "20-29 years old",
            4: "30-39 years old",
            5: "40-49 years old",
            6: "50-59 years old",
            7: "60-69 years old",
            8: "70-79 years old",
        }
        
        color_dict = {
            1: "#90b9f5",
            2: "#62a1fc",
            3: '#3885f2',
            4: '#78f8ff',
            5: '#1cdbe6',
            6: '#ffb0fb',
            7: '#e6c5e4',
            8: '#cc97c8'
        }

        ax.grid(which="major", axis="y", color="#758D99", alpha=0.2)
        ax.spines["bottom"].set_linewidth(2)

        # Define the gray palette
        gray_palette = [(0.5, 0.5, 0.5, 0.3)] * df_mean["age_range"].nunique()

        

        average = sns.lineplot(
            x="3months_use_per_week",
            y="life_satisfaction_0to10",
            data=line_mean,
            legend=False,
            color="gray",
            linestyle="--",
            linewidth=4,
            ax=ax,  # Specify the ax parameter here
        )
        
        handles = [average.get_lines()[0]]
        labels = ['Average']

        sns.lineplot(
            x="3months_use_per_week",
            y="life_satisfaction_0to10",
            hue="age_range",
            palette=gray_palette,
            data=df_mean,
            legend=False,
            linewidth=3,
            ax=ax,  # Specify the ax parameter here
        )

        for i in input.checkbox_age_group():
            i = int(i)
            line = sns.lineplot(
                x="3months_use_per_week",
                y="life_satisfaction_0to10",
                data=df_mean[df_mean["age_range"] == i],
                color=color_dict.get(i, "black"),
                legend=True,
                linewidth=6,
                ax=ax
            )
            handle = line.get_lines()[-1]
            handles.append(handle)  # Collect handle for the line
            labels.append(f"{ages_dict[i]}")  # Collect label for the legend

        ax.spines[["top", "right", "left"]].set_visible(False)

        ax.set_ylim(4.5, 9.5)
        ax.xaxis.set_tick_params(labelsize=15)

        # Customize the grid
        ax.grid(axis="y", visible=True)  # Turn off vertical grid lines
        ax.grid(axis="x", visible=False)

        ax.yaxis.set_tick_params(
            pad=4,  # Pad tick labels so they don't go over y-axis
            labeltop=False,  # Put x-axis labels on top
            labelbottom=True,  # Set no x-axis labels on bottom
            bottom=False,  # Set no ticks on bottom
            labelsize=11,
            color=(0.5, 0.5, 0.5, 0.01),
        )  # Set tick label size

        # Define your x-axis tick positions
        x = [5, 4, 3, 2, 1]  # Adjust as needed based on your data

        # Define your x-axis tick labels
        xticks_labels = [
            "Once a week",
            "2-3 times a week",
            "4-6 times a week",
            "Everyday infrequent",
            "Everyday frequent",
        ]

        if handles:
            ax.legend(
                handles=handles,
                labels=labels,
                loc="upper right",
                bbox_to_anchor=(1.2, 1),
            )

        # Set the x-axis ticks and labels
        plt.xticks(x, xticks_labels, rotation=60, ha="right")

        ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
        ax.invert_xaxis()

        plt.tick_params(axis="x", labelsize=11)
        plt.xlabel("")
        plt.ylabel("")

        return fig
    
    
    source_tag = ui.div("Source: Academia Sinica (2022)")
    source_tag.add_style('font-size: 12px; color: #758D99;')
