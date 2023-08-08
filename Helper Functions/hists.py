import pandas as pd 
import matplotlib.pyplot as plt

def plot_histograms(dataframe, heading):
    # Get the number of columns
    num_cols = dataframe.shape[1]

    # Calculate the number of rows and columns for the subplots
    num_rows = int(num_cols**0.5)
    num_cols = (num_cols // num_rows) + int(num_cols % num_rows > 0)

    # Create figure, subplots
    fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(25, 15))
    fig.suptitle(heading, fontsize=28)

    # Flatten the axes array (in case num_cols != num_rows)
    axes = axes.ravel()

    # Loop through each column and plot a histogram
    for i, column in enumerate(dataframe.columns):
        axes[i].hist(dataframe[column], bins=20)
        axes[i].set_title(column)
        axes[i].set_xlabel('Value')
        axes[i].set_ylabel('Frequency')

    # Hide empty subplots
    for i in range(len(dataframe.columns), len(axes)):
        axes[i].axis('off')

    plt.tight_layout()
    plt.show()