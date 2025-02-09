import numpy as np
import pandas as pd

def create_1d_array():
    """
    Create a 1D NumPy array with values [1, 2, 3, 4, 5]
    Returns:
        numpy.ndarray: 1D array
    """
    arr = np.array([1, 2, 3, 4, 5])
    return arr

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

    return mean_value, std_dev, max_value

def read_csv_file(filepath):
    """
    Read a CSV file using Pandas
    Args:
        filepath (str): Path to CSV file
    Returns:
        pandas.DataFrame: Loaded dataframe
    """
    df = pd.read_csv('sample-data.csv')
    return df

def handle_missing_values(df):
    """
    Handle missing values in the DataFrame
    1. Identify number of missing values
    2. Fill missing values with appropriate method
    Returns:
        pandas.DataFrame: Cleaned dataframe
    """
    for column in df.columns:
        if df[column].dtype == "Object":
            df[column].fillna(method="ffill", inplace=True)
        else:
            df[column].fillna(df[column].mean(), inplace=True)

    return df

def select_data(df):
    """
    Select specific columns and rows from DataFrame
    Returns:
        pandas.DataFrame: Selected data
    """
    selected_df_data = df.iloc[0:3,0:3]
    return selected_df_data

def rename_columns(df):
    """
    Rename columns of the DataFrame
    Returns:
        pandas.DataFrame: DataFrame with renamed columns
    """
    column_mapping = {
        "Name": "Full Name",
        "Age": "Employee Age",
        "Salary": "Annual Salary",
        "Department": "Work Department",
        "Experience": "Years of Experience",
        "Education": "Education Level",
    }
    
    df.rename(columns=column_mapping, inplace=True)
    return df
