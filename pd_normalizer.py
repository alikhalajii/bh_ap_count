import pandas as pd
import re

def pd_normalizer(df_dict):
    """
    This function takes a dictionary of dataframes as input and returns a dictionary of dataframes 
    with all values uppercased and NaN values excluded. Values containing '9120' will be replaced 
    with 'C9120AX'.
    """
    

    normalized_dict = {}


    geschlossene_nl = ['190', '255', '313', '320', '341', '368', '370', '380',
                        '405', '475', '482', '497', '501', '504', '511', '517',
                          '522', '524', '526', '529', '533', '549', '554', '563',
                            '582', '660', '764', '779', '781', '786', '792', '801',
                              '816', '881', '895','959', '6264', '6269',]
    # Remove all dataframes with keys in geschlossene_nl
    [df_dict.pop(key, None) for key in geschlossene_nl]
    
    for key, df in df_dict.items():
         
        # Convert all values to upper case, exclude NaN values, and replace values containing '9120'
        df = df.apply(lambda x: x.astype(str).str.upper().replace('NAN', pd.NA))

        pattern = re.compile('.*9120.*')
        df = df.apply(lambda x: x.str.replace(pattern, 'C9120AX', regex=True))
        
        pattern = re.compile('.*1542I.*')
        df = df.apply(lambda x: x.str.replace(pattern, 'CAP1542I', regex=True))

        pattern = re.compile('.*AIR-CAP1532I.*')
        df = df.apply(lambda x: x.str.replace(pattern, 'CAP1532I', regex=True))
        
        pattern = re.compile('.*AIR-AP1830I.*')
        df = df.apply(lambda x: x.str.replace(pattern, 'AP1830I', regex=True))
        
        pattern = re.compile('.*AIR-CAP1602E.*')
        df = df.apply(lambda x: x.str.replace(pattern, 'CAP1602E.', regex=True))
        
        pattern = re.compile('.*AIR-CAP1702I.*')
        df = df.apply(lambda x: x.str.replace(pattern, 'CAP1702I', regex=True))
        
        pattern = re.compile('.*AIR-CAP1602I.*')
        df = df.apply(lambda x: x.str.replace(pattern, 'CAP1602I', regex=True))

        normalized_dict[key] = df


    return normalized_dict




