import pandas as pd

class DataTransform:
    ''' Class to perform various data transformations on the DataFrame
    '''
    def __init__(self, df: pd.DataFrame):
        '''
        Initialise with a DataFrame.

        Parameters
        df(pd.DataFrame): The DataFrame to be transformed.
        '''
        self.df = df

    def convert_to_int(self, column: str) -> 'DataTransform':
        '''
        Convert a specified column's string values to integers.
        
        Parameters:
        column (str): The column to be converted.
        
        Returns:
        DataTransform: The instance of the DataTransform class.
        '''
        self.df[column] = self.df[column].str.extract(r'(\d+)')
        self.df[column] = self.df[column].fillna(0).astype(int)
        return self

    def convert_employment_length(self, column:str) -> 'DataTransform': 
        '''
        Convert employment length strings to float values.
        
        Parameters:
        column (str): The column to be converted.
        
        Returns:
        DataTransform: The instance of the DataTransform class.
        '''
        self.df[column] = self.df[column].str.replace('< 1 year', '0')
        self.df[column] = self.df[column].str.replace('10+ years', '10')
        self.df[column] = self.df[column].str.extract(r'(\d+)')
        self.df[column] = self.df[column].astype(float)
        return self.df

    def convert_multiple_to_datetime(self, columns: list, date_format: str = None) -> pd.DataFrame:
        '''
        Convert multiple columns to datetime format.
        
        Parameters:
        columns (list): List of columns to be converted.
        date_format (str, optional): The datetime format to be used. Defaults to None.
        
        Returns:
        pd.DataFrame: The updated DataFrame.
        '''
        
        for column in columns: 
            if date_format:
                self.df[column] = pd.to_datetime(self.df[column], format=date_format)
            else: 
                self.df[column] = pd.to_datetime(self.df[column])
        return self.df

    def convert_to_category(self, column: str) -> 'DataTransform':
        '''
        Convert a specified column to the 'category' datatype.
        
        Parameters:
        column (str): The column to be converted.
        
        Returns:
        DataTransform: The instance of the DataTransform class.
        '''
        self.df[column] = self.df[column].astype('category')
        return self.df

    def convert_to_date(self, columns:list) -> 'DataTransform':
        '''
        Convert specified columns to date format.
        
        Parameters:
        columns (list): List of columns to be converted.
        
        Returns:
        DataTransform: The instance of the DataTransform class.
        '''
        for column in columns:
            self.df[column]=pd.to_datetime(self.df[column]).dt.date
        return self.df
    
    def get_dataframe(self) -> pd.DataFrame:
        '''
        Get the transformed DataFrame.
        
        Returns:
        pd.DataFrame: The transformed DataFrame.
        '''
        return self.df