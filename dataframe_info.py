import pandas as pd

class DataFrameInfo:
    '''
    Class to provide insights and summary statistices for a DataFrame
    '''

    def __init__(self, df: pd.DataFrame):
        '''
        Initialize with a DataFrame.
        
        Parameters:
        df (pd.DataFrame): The DataFrame to be analyzed.
        '''
        self.df = df

    def describe_columns(self) -> pd.DataFrame:
        '''
        Method to describe the data types of columns in the DataFrame
        
        Returns:
        pd.DataFrame: A DataFrame containing the data types of each column.
        '''
        return self.df.dtypes
    
    def extract_statistical_values(self) -> pd.DataFrame:
        '''
        Method to extract statistical values (median, mean, std)
        for numerical columns

        Returns:
        pd.DataFrame: A DataFrame containing the median,
         standard deviation, and mean for numeric columns.
        '''
        numberic_cols=self.df.select_dtypes(include=['number']).columns
        return self.df[numberic_cols].agg(['median','std','mean'])
    
    def count_distinct_values(self) -> pd.Series:
        '''
        Method to count distinct values for categorical columns
        
        Returns:
        pd.Series: A Series containing the count of unique values for each categorical column.
        '''
        categorical_columns = self.df.select_dtypes(
            include=['category','object']).columns
        return self.df[categorical_columns].nunique()
    
    def print_shape(self) -> tuple:
        '''
        Method to get the shape of the DataFrame
        
        Returns:
        tuple: A tuple containing the number of rows and columns in the DataFrame.
        '''
        return self.df.shape

    def count_null_values(self) -> pd.DataFrame:
        '''
        Method to count the number of null values 
        and calculate the percentage of null values 
        within the DataFrame

        Returns:
        pd.DataFrame: A DataFrame containing the count and percentage of null values for each column.
        '''
        null_counts = self.df.isnull().sum()
        null_percentage = round((self.df.isnull().sum() / len(self.df)) * 100,2)
        return pd.DataFrame({'null_count': null_counts, 'null_percentage': null_percentage})

    def get_summary(self) -> pd.DataFrame:
        '''
        Method to get the summary statistics of the DataFrame
        
        Returns:
        pd.DataFrame: A DataFrame containing summary statistics for each numeric column.    
        '''
        return self.df.describe()
