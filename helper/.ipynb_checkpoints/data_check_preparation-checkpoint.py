import pandas as pd
import numpy as np

def read_data(PATH):
    '''
    Read data from dataset from path
   
    Parameters
    ----------
    PATH : str
        path source of training data, csv.
    
    Returns
    -------
    data : pd.DataFrame
        Data for modeling
    '''
    data = pd.read_csv(PATH,encoding='latin-1')
    
    return data

def check_read_data_success(data_input):
    '''
    Sanity check for data success
    
    Parameters
    ----------
    data
    
    '''
    if not data_input.notnull().sum().sum() > 0:
        with open("warning_msg.txt", "a") as writer:
            writer.write("You have missing values in full in at least one column")
            
    return data_input

def rename_column(data_input, column):
    data_input.rename(columns = column, inplace = True)
    return data_input

def set_datetime_column(data_input, datetime_column):
    '''
    Convert column into datetime
    
    Parameters
    ----------
    data
    
    '''
    for col in datetime_column:
        data_input[col] = pd.to_datetime(data_input[col])
    return data_input

def read_and_check_data(path, column, datetime_column):
    """Read and checking data."""
    print("start import data")
    df = read_data(path)
    print("done import data")
    print("start renaming columns")
    df = rename_column(df, column)
    print("done renaming columns")
    print("start convert specific columns to datetime")
    df = set_datetime_column(df, datetime_column)
    print("done convert specific columns to datetime")
    print("start checking read data success")
    df = check_read_data_success(df)
    print("done checking read data success")
    
    return df