import pandas as pd

class DataFrameInfo:

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def describe_columns(self) -> pd.DataFrame:
        return self.df.dtypes
    
    def extract_statistical_values(self) -> pd.DataFrame:
        return self.df.agg(['median','std','mean'])
    
    def count_distinct_values(self) -> pd.DataFrame:
        categorical_columns = self.df.select_dtypes(
            include=['category','object']).columns
        return self.df[categorical_columns].nunique()
    
    def print_shape(self) -> tuple:
        return self.df.shape

    def count_null_values(self) -> pd.DataFrame:
        null_counts = self.df.isnull().sum()
        null_percentage = (self.df.isnull().sum() / len(self.df)) * 100
        return pd.DataFrame({'null_count': null_counts, 'null_percentage': null_percentage})

    def get_summary(self) -> pd.DataFrame:
        return self.df.describe()

    def get_correlation_matrix(self) -> pd.DataFrame:
        return self
