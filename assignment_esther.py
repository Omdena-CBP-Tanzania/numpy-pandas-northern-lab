import numpy as np
import pandas as pd

def create_1d_array():
    """
    Create a 1D NumPy array with values [1, 2, 3, 4, 5]
    Returns:
        numpy.ndarray: 1D array
    """
    onedimarr = np.array([1,2,3,4,5])
    return onedimarr


def create_2d_array():
    """
    Create a 2D NumPy array with shape (3,3) of consecutive integers
    Returns:
        numpy.ndarray: 2D array
    """
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    return arr

def array_operations(arr):
    """
    Perform basic array operations:
    1. Calculate mean
    2. Calculate standard deviation
    3. Find max value
    Returns:
        tuple: (mean, std_dev, max_value)
    """
    mean_value = np.mean(arr)
    std_dev = np.std(arr)
    max_value = np.max(arr)
    mytuple =(mean_value, std_dev, max_value)
    return mytuple

def read_csv_file(filepath):
    """
    Read a CSV file using Pandas
    Args:
        filepath (str): Path to CSV file
    Returns:
        pandas.DataFrame: Loaded dataframe
    """
    readfile = pd.read_csv('data/sample-data.csv')
    fileToread = readfile.head()
    return fileToread

def handle_missing_values(df):
    """
    Handle missing values in the DataFrame
    1. Identify number of missing values
    2. Fill missing values with appropriate method
    Returns:
        pandas.DataFrame: Cleaned dataframe
    """
    df = pd.read_csv("data/sample-data.csv")

    df.isnull().sum()
    for column in df.columns:
        if df[column].dtype in ['int64', 'float64']: # check if column is numeric
            df[column] = df[column].fillna(df[column].mean()) # fill missing values with mean

        else: # non-numeric columns
            df[column] = df[column].fillna(df[column].mode()[0]) # fill missing values with mode

    return df
    #print(missing_values)
    
    #return missing_values

#print(handle_missing_values("data/sample-data.csv"))

def select_data(df):
    """
    Select specific columns and rows from DataFrame
    Returns:
        pandas.DataFrame: Selected data
    """
    df =pd.read_csv("data/sample-data.csv", usecols =['Name','Age','Salary'])
    return df


def rename_columns(df):
    """
    Rename columns of the DataFrame
    Returns:
        pandas.DataFrame: DataFrame with renamed columns
    """
    df= pd.read_csv("data/sample-data.csv")
    df = pd.rename(column={'Name':'Full Name','Age':'Years','Salary':'Payments','Department':'WorkingArea','Experience':'WorkingYear','Education':'School'})
    return df
