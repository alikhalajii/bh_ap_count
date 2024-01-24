"""
Freq_dist_result_stadt_merger_gesamt_calc.py "fdrsmgc"

This script generates theexel file Niederlassung_Projekt_Mapper.

This script generates a bar chart to visualize the frequency distribution of NL occurrences
over different project numbers. The input is a dictionary where keys represent project numbers, and values represent
the corresponding NL occurrences.


The resulting plot is saved as an image file in the 'results' directory.

"""
import pandas as pd
import os
import datetime
from datetime import date
from matplotlib import pyplot as plt

def fdrsmgc(freqdist_df, nl_df):
    #This function takes two DataFrames as input and merges them on the 'Niederlassung' column.
    
    
    # Convert the 'Niederlassung' column in DataFrames to 'object' type
    freqdist_df['Niederlassung'] = freqdist_df['Niederlassung'].astype(str)
    
    # Convert the 'Niederlassung' column in the 'nl_df' DataFrame to 'object' type and pad with leading zeros
    nl_df['Niederlassung'] = nl_df['Niederlassung'].astype(str).str.zfill(3)
    
    # Perform the merge operation between the two DataFrames on the 'Niederlassung' column
    nl_mapper_output = freqdist_df.merge(nl_df, on='Niederlassung', how='left')
    
    # Reorder the columns so 'Niederlassung' and 'Stadt' are the first two columns
    nl_mapper_output = nl_mapper_output.reindex(columns=['Niederlassung', 'Stadt'] + list(nl_mapper_output.columns[:-2]))
    
    # Drop any duplicate 'Niederlassung' column that might have been created during the merge
    nl_mapper_output = nl_mapper_output.loc[:, ~nl_mapper_output.columns.duplicated()]
    
    # Add a 'Sum' row to the dataframe by summing up all columns except the first two
    nl_mapper_output.loc['Gesamt'] = nl_mapper_output.iloc[:, 2:].sum(axis=0)
    nl_mapper_output.loc['Gesamt', 'Niederlassung'] = 'Gesamt'

    # Add a 'Sum' column to the dataframe by summing up all rows except the 'Niederlassung' and 'Stadt' columns.
    nl_mapper_output['Gesamt AP'] = nl_mapper_output.iloc[:, 2:].sum(axis=1)
    
    return nl_mapper_output
