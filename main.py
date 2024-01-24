import os
import re
import time
import pandas as pd
import excel_writer
import freq_dist as fd
import pd_normalizer
import warnings
from  nl_project_mapper import nl_project_mapper
import freq_dist_result_stadt_merger_gesamt_calc

start_time = time.time()

# Define the path to the project directories
projects_dir = 'projects_directory'
nl_pattern = '\D*(\d{3})'

sheetname_pattern_14 = '.*FINAL.*'
sheetname_pattern = '.*AP-Liste.*'

df_sheets = {}
nl_project_dict = {}

warnings.filterwarnings("ignore")

# Loop over all subdirectories and files in the top directory
for root, dirs, files in os.walk(projects_dir):
    for dir_name in sorted(dirs, reverse=True):
        dir_path = os.path.join(root, dir_name)
        for dirpath, dirnames, filenames in os.walk(dir_path):
            project_nl_count = 0
            project_number = os.path.basename(dirpath)
            print(f"\n \n Das Project {project_number} wird bearbeitet.")
           
            for file_name in filenames:
                if file_name.endswith(".xls") or file_name.endswith(".xlsx"):
                    match = re.search(nl_pattern, file_name)
                    file_name_to_nl = match.group(1)
                    
                if file_name_to_nl not in df_sheets.keys():
                #Add the Niederlassung to the dictionary(nl, project_number) and add the matching sheet to the dictionary(nl, sheet)
                    
                    project_nl_count += 1
                    nl_project_dict[file_name_to_nl] = project_number
                    
                    for sheet in pd.ExcelFile(os.path.join(dir_path, file_name)).sheet_names:
                        if re.match(sheetname_pattern, sheet):
                            df = pd.read_excel(os.path.join(dir_path, file_name), sheet_name=sheet, usecols=[7])
                            df_sheets[file_name_to_nl] = df
                            break

                        elif re.match(sheetname_pattern_14, sheet):
                            df = pd.read_excel(os.path.join(dir_path, file_name), sheet_name=sheet, usecols=[2])
                            df_sheets[file_name_to_nl] = df
                            break      
            
            print(project_nl_count, " neue Niederlassungen wurden gefunden.")
            ###print(all_accepted_nl)

# Normalize the dataframes in the dictionary
pd_normalized_dict = pd_normalizer.pd_normalizer(df_sheets)

# Send the dictionary of dataframes to the excel_writer function if debuggig needed
output_file = 'nl_sheets.xlsx'  # AP-types columns of NL
excel_writer.excel_writer_dict(pd_normalized_dict, output_file)


freq_dist_df = fd.freq_dist(pd_normalized_dict)

# Send the frequency distribution dataframe to the nl_mapper function
nl_stadt_excel = pd.read_excel('nl_stadt_mapper.xlsx')
nl_mapper_output = freq_dist_result_stadt_merger_gesamt_calc.fdrsmgc(freq_dist_df, nl_stadt_excel)

# Generate a bar chart to visualize the frequency distribution of NL occurrences over different project numbers
nl_project_mapper(nl_project_dict)

# Send the output of the nl_mapper function to the excel_writer function to create the output file
output_file = excel_writer.df_plot_output(nl_mapper_output, excel_writer.df_visualizer(nl_mapper_output))

# Print the bold text to the terminal
BOLD = '\033[1m'
RESET = '\033[0m'
text = "Öffnen Sie den 'results'Ordner, um alle Ergebnisse abzurufen."
print(f"\n {BOLD + text + RESET} \n")

warnings.filterwarnings("default")

end_time = time.time()
runtime = end_time - start_time
print(f"Skript wurde in {runtime:.3f} Sekunden ausgeführt")
