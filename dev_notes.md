**Introduction**
Creating with Python an Excel workbook that takes data 
from other Excel files in a directory path whose sheets contain the string 'Final'.
The columns of Excel workbook to be created contains the number of occurrences of each element 
either in the columns 'C' of the Excel files of the sheets containing 'Final' if project_number >= 14 
or  in the columns 'H' of the Excel files of the sheets containing 'AP-Liste' if project_number < 14

Each row of Excel file to be created corresponds to a three-digit number, which is found in names of source Excel files stored as nl_number. A dict of each nl_number and dataframe sheet will be generated, which be take out to frequency distribution module to achieve the freq_dist of values of dataframes.

At the end, some normaliation of outputed dataframe be done to the excel_reults would have the desired form.

******************************************
For Generating the right requirement file:
 ! pip3 freeze > requirements.txt 

installing all requirements needed in project:
! pip install -r requirements.txt