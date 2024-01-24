"""
nl_project_mapper.py

This script generates theexel file Niederlassung_Projekt_Mapper.

This script generates a bar chart to visualize the frequency distribution of NL occurrences
over different project numbers. The input is a dictionary where keys represent project numbers, and values represent
the corresponding NL occurrences.


The resulting plot is saved as an image file in the 'results' directory.

"""
import os
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

def nl_project_mapper(nl_projext_dict):


    # Generate the exel file Niederlassung_Projekt_Mapper
    dev_nl_proj_mapper = pd.DataFrame(nl_projext_dict.items(), columns=['Niederlassung', 'Projekt'])
    os.makedirs('results', exist_ok=True)
    dev_nl_proj_mapper.to_excel('results/Niederlassung_Projekt_Mapper.xlsx', sheet_name='dev_excel', index=False)


    # Create a Counter object to get frequency distribution of NL over Project number
    values = list(nl_projext_dict.values())
    freq_dist = Counter(values)
    
    # Sort the keys (x-axis) in ascending order
    sorted_keys = sorted(freq_dist.keys())
    # Plot the frequency distribution with sorted keys and add bar labels
    bars = plt.bar(sorted_keys, [freq_dist[key] for key in sorted_keys])
    plt.bar_label(bars, padding=3)  # Add labels with padding


    # Add labels and title
    plt.xlabel('ProjektNr')
    plt.ylabel('NL')
    plt.title('Anzahl der NL/Projekt')
    
    # Set the limit of the y-axis to 50
    plt.ylim(0, 50)

    # Save the plot as an image file
    plot_filename = 'results/Plot_NL-Projekt'
    plt.savefig(plot_filename)



