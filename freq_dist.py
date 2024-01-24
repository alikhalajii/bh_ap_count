import pandas as pd
import os

def freq_dist(df_dict):
    """
    This function takes in a dictionary of dataframes where each dataframe contains a single column of data. 
    The function performs a frequency distribution on each column and 
    outputs the results to an Excel file.
    """

    # Create a dictionary to store the frequency distribution results for each sheet
    freq_dict = {}

    # Loop through each sheet in the dataframe
    for sheet_name, sheet_data in df_dict.items():
        col_name = sheet_data.columns[0]
        freq_dist = sheet_data[col_name].value_counts(normalize=False, dropna=True)
        freq_dict[sheet_name] = freq_dist

    # Combine the frequency distributions for each sheet into a single dataframe
    freq_dist_df = pd.concat(freq_dict, axis=1)

    # Transpose the output dataframe to have the row names as sheet names and column index as unique values
    freq_dist_df = freq_dist_df.transpose()

    # Sort the columns in the dataframe
    sorted_columns = sorted(freq_dist_df.columns)
    freq_dist_df = freq_dist_df[sorted_columns]

    # Set the name of the first cell to 'Niederlassung'
    freq_dist_df.insert(0, 'Niederlassung', freq_dist_df.index.values)
    freq_dist_df = freq_dist_df.sort_values(by="Niederlassung",)
    
    # Reset the index of the dataframe
    freq_dist_df.reset_index(drop=True, inplace=True)

    # Rename the columns to strings
    freq_dist_df.columns = freq_dist_df.columns.astype(str)

    #Add a column for 'Leer' to the dataframe to error handle for missing values returned to nl_mapper.py
    freq_dist_df['Leer'] = 0
    
    # Generate freqdist output for debugging
    os.makedirs('debug', exist_ok=True)
    freq_dist_df.to_excel('debug/freq_dist_df.xlsx')


    return freq_dist_df
