import pandas as pd

class DataTransform:

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def convert_employment_length(self, column:str) -> pd.DataFrame: 
        self.df[column] = self.df[column].str.replace('< 1 year', '0')
        self.df[column] = self.df[column].str.replace('10+ years', '10')
        self.df[column] = self.df[column].str.extract(r'(\d+)')
        self.df[column] = self.df[column].astype(float)
        return self.df

    def convert_multiple_to_datetime(self, columns: list, date_format: str = None) -> pd.DataFrame:
        for column in columns: 
            if date_format:
                self.df[column] = pd.to_datetime(self.df[column], format=date_format)
            else: 
                self.df[column] = pd.to_datetime(self.df[column])
        return self.df

    def convert_to_category(self, column: str) -> pd.DataFrame:
        self.df[column] = self.df[column].astype('category')
        return self.df
    
    def get_dataframe(self) -> pd.DataFrame:
        return self.df