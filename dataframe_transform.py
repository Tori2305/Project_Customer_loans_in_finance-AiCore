import pandas as pd

class DataFrameTransform:
    def __init__(self,df:pd.DataFrame):
        self.df = df

    def count_null_values(self) -> pd.DataFrame:
        null_counts = self.df.isnull().sum()
        null_percentage = round((self.df.isnull().sum() / len(self.df)) * 100, 2)
        null_df = pd.DataFrame({'null_count': null_counts, 'null_percentage': null_percentage})
        return null_df[null_df['null_count'] > 0]
    
    def drop_columns(self, columns: list) -> pd.DataFrame:
        self.df = self.df.drop(columns=columns)
        return self.df

    def impute_missing_values(self, strategy: str = 'median') -> pd.DataFrame:
        for column in self.df.columns:
            if self.df[column].isnull().sum() > 0:
                if self.df[column].dtype in ['float64','int64']:
                    if strategy == 'median':
                        self.df[column].fillna(self.df[column].median())
                    elif strategy == 'mean':
                        self.df[column].fillna(self.df[column].mean())
                else:
                    self.df[column] = self.df[column].fillna(self.df[column].mode()[0])
        return self.df

    def get_cleaned_dataframe(self) -> pd.DataFrame:
        return self.df