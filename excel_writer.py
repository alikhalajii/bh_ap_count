import pandas as pd
import numpy as np
import os
import xlsxwriter
import matplotlib.pyplot as plt
from datetime import date
import openpyxl
from openpyxl.utils import get_column_letter

def excel_writer_dict(df_sheets_dict, output_file):
    """
    Writes a dictionary of dataframes to separate sheets in an Excel file.

    Args:
        df_sheets_dict (dict): A dictionary of dataframes.
        output_file (str): The path of the output Excel file.

    Returns:
        None
    """
    # Create a Pandas Excel writer using the output file path
    writer = pd.ExcelWriter(output_file)

    # Loop through the df_sheets dictionary and write each value (dataframe) to a separate sheet
    for key, value in df_sheets_dict.items():
        value.to_excel(writer, sheet_name=key)

    writer.close()

#************************************************

def df_visualizer(df):
    """
    Visualizes a dataframe by creating a bar chart.

    Args:
        df (pd.DataFrame): The dataframe to be visualized.

    Returns:
        matplotlib.figure.Figure: The figure object representing the bar chart.
    """
    columns_to_plot = df.columns[2:]

    # Extract the labels from the first row of the dataframe
    labels = df.columns[2:]

    # Extract the values from the 'Gesamt' row and convert them to floats
    values = df.loc['Gesamt', columns_to_plot].astype(float)

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(5, 4))  # Adjust the figure size as per your preference

    # Create a bar chart using the extracted labels and values
    bars = ax.bar(labels, values)

    # Add labels and title to the chart
    ax.set_xlabel('AP-Typ')
    ax.set_ylabel('Anzahl')
    ax.set_title('Anzahl der APs')

    # Rotate the x-axis labels by 30 degrees and adjust font size
    ax.set_xticklabels(labels, rotation=30, ha='right', fontsize=6)

    # Set the y-axis tick locations and labels
    y_ticks = np.arange(0, max(values) + 500, 500)  # Adjust the interval as per your preference
    ax.set_yticks(y_ticks)
    ax.set_yticklabels(y_ticks.astype(int), fontsize=6)  # Convert to integers and adjust the font size of the y-axis tick labels

    # Add value labels on top of each bar with reduced font size
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, str(int(height)), ha='center', va='bottom', fontsize=6)

    # Return the figure object
    return fig

#************************************************


def df_plot_output(df, figure):
    """
    Saves a dataframe and a corresponding figure as an Excel file.

    Args:
        df (pd.DataFrame): The dataframe to be saved.
        figure (matplotlib.figure.Figure): The figure object representing the chart.

    Returns:
        None
    """
    # Get the current date for the file name
    today = date.today().strftime('%Y-%m-%d')
    file_name = f'results/{today} Gesamtaufstellung Bauhaus APs.xlsx'  # Specify the folder path in the file name

    # Create the "results" directory if it doesn't exist
    os.makedirs('results', exist_ok=True)

    # Create a Pandas Excel writer
    writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
    workbook = writer.book
    worksheet_df = workbook.add_worksheet('Aufgeteilt nach NL')
    worksheet_plot = workbook.add_worksheet('AP-Typen-Visualisierung')

    # Write the DataFrame to the worksheet
    df.to_excel(writer, index=False, sheet_name='Aufgeteilt nach NL')

    # Autofit the column width for the first sheet
    autofit_column_width(worksheet_df, df)

    # Freeze the first row
    worksheet_df.freeze_panes(1, 0)  # Freeze the first row

    # Save the plot as an image file
    plot_filename = 'results/Plot_AP-Types.png'
    figure.savefig(plot_filename)

    # Insert the plot image into the worksheet
    image_width = 3  # Width in inches, adjust as needed
    image_height = 3  # Height in inches, adjust as needed

    # Get the dpi value from the figure object
    dpi = figure.dpi

    # Calculate the image scale while maintaining the aspect ratio
    scale = min(image_width / figure.get_figwidth(), image_height / figure.get_figheight())
    image_width = scale * figure.get_figwidth() * dpi
    image_height = scale * figure.get_figheight() * dpi

    worksheet_plot.insert_image('A1', plot_filename, {'x_offset': 10, 'y_offset': 10, 'x_scale': image_width / dpi, 'y_scale': image_height / dpi})

    # Save the Excel file
    writer.close()

    # Open the Excel file using the default application
    abs_file_path = os.path.abspath(file_name)
    os.startfile(abs_file_path)

#************************************************


def autofit_column_width(worksheet, df):
    """
    Autofits the column width for a worksheet based on the content of a DataFrame.

    Args:
        worksheet (xlsxwriter.worksheet.Worksheet): The worksheet object to autofit the column width.
        df (pd.DataFrame): The DataFrame containing the content.

    Returns:
        None
    """
    # Iterate over the columns and calculate the maximum length of each cell value
    for i, col in enumerate(df.columns):
        max_len = max(
            df[col].astype(str).map(len).max(),
            len(col)
        ) + 2  # Add some padding

        # Set the column width
        worksheet.set_column(i, i, max_len)

#************************************************


def get_column_widths(df):
    """
    Calculates the maximum width of each column in a DataFrame based on the content.

    Args:
        df (pd.DataFrame): The DataFrame for which to calculate the column widths.

    Returns:
        list: A list of column widths.
    """
    widths = []
    for col in df.columns:
        column_width = max(df[col].astype(str).str.len().max(), len(col))
        widths.append(column_width)
    return widths
