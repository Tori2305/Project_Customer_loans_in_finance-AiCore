from scipy.stats import boxcox
from scipy import stats
import pandas as pd
import numpy as np


class DataFrameTransform:
    '''
    Class to perform various data transformations on a DataFrame.
    '''
    def __init__(self,df:pd.DataFrame):
        '''
        Initialize with a DataFrame.
        
        Parameters:
        df (pd.DataFrame): The DataFrame to be transformed.
        '''
        self.df = df

    def count_null_values(self) -> pd.DataFrame:
        '''
        Method to count null values and calculate the percentage of null values in columns.
        
        Returns:
        pd.DataFrame: A DataFrame containing the count and percentage of null values for each column.
        '''
        null_counts = self.df.isnull().sum()
        null_percentage = round((self.df.isnull().sum() / len(self.df)) * 100, 2)
        null_df = pd.DataFrame({'null_count': null_counts, 'null_percentage': null_percentage})
        return null_df[null_df['null_count'] > 0]
    
    def drop_columns(self, columns: list) -> pd.DataFrame:
         '''
        Method to drop specified columns from the DataFrame.
        
        Parameters:
        columns (list): List of columns to be dropped.
        
        Returns:
        pd.DataFrame: A DataFrame with the specified columns dropped.
        '''
        new_df = self.df.drop(columns=columns)
        return new_df

    def impute_missing_values(self, df: pd.DataFrame, strategy: str = 'median') -> pd.DataFrame:
        '''
        Method to impute missing values in the DataFrame.
        
        Parameters:
        df (pd.DataFrame): The DataFrame in which to impute missing values.
        strategy (str): Strategy to impute missing values ('median', 'mean', or 'mode'). Defaults to 'median'.
        
        Returns:
        pd.DataFrame: A DataFrame with missing values imputed.
        '''
        for column in df.columns:
            if df[column].isnull().sum() > 0:
                if df[column].dtype in ['float64','int64']:
                    if strategy == 'median':
                        df[column]=df[column].fillna(self.df[column].median())
                    elif strategy == 'mean':
                        df[column]=df[column].fillna(self.df[column].mean())
                else:
                    df[column] = self.df[column].fillna(self.df[column].mode()[0])
        return df

    def transform_skewed_cols(self, columns:list) -> pd.DataFrame:
        '''
        Method to transform skewed columns using log, sqrt, or Box-Cox transformations.
        
        Parameters:
        columns (list): List of columns to be transformed.
        
        Returns:
        pd.DataFrame: A DataFrame with skewed columns transformed.
        '''
        for column in columns:
            print(f"\nProcessing column: {column}")

            if (self.df[column] <= 0).any():
                self.df[column] = self.df[column] - self.df[column].min() + 1

            #Apply log transformation
            log_transformed = np.log1p(self.df[column])
            log_skewness = log_transformed.skew()
            print(f"Log skewness for {column}: {log_skewness}")

            # Apply square root transformation
            sqrt_transformed = np.sqrt(self.df[column])
            sqrt_skewness = sqrt_transformed.skew()
            print(f"Sqrt skewness for {column}: {sqrt_skewness}")

            # Apply Box-Cox transformation (requires positive values)
            try:
                boxcox_transformed, _ = boxcox(self.df[column])
                boxcox_skewness = pd.Series(boxcox_transformed).skew()
                print(f"Box-Cox skewness for {column}: {boxcox_skewness}")
            except ValueError as e:
                print(f"Error applying Box-Cox transformation to column {column}: {e}")
                continue

            # Determine the best transformation
            transformations = {
                'log': log_skewness,
                'sqrt': sqrt_skewness,
                'boxcox': boxcox_skewness
            }
            best_transformation = min(transformations, key=transformations.get)
            print(f"\nBest transformation for {column}: {best_transformation}")

            # Apply the best transformation
            if best_transformation == 'log':
                self.df[column] = log_transformed
            elif best_transformation == 'sqrt':
                self.df[column] = sqrt_transformed
            elif best_transformation == 'boxcox':
                self.df[column] = boxcox_transformed

        return self.df 


    def remove_outliers(self, columns: list, method: str = 'both') -> pd.DataFrame:
        '''
        Method to remove outliers from specified columns using IQR or Z-score methods.
        
        Parameters:
        columns (list): List of columns from which to remove outliers.
        method (str): Method to remove outliers ('IQR', 'Z-score', or 'both'). Defaults to 'both'.
        
        Returns:
        pd.DataFrame: A DataFrame with outliers removed.
        '''
        for column in columns:
            if method == 'IQR'or method == 'both':
                Q1 = self.df[column].quantile(0.25)
                Q3 = self.df[column].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                self.df = self.df[(self.df[column] >= lower_bound) & (self.df[column] <= upper_bound)]
            elif method == 'Z-score' or method == 'both':
                self.df = self.df[(np.abs(stats.zscore(self.df[column])) < 3)]
        return self.df


    def find_highly_correlated_pairs(self, correlation_matrix: pd.DataFrame, threshold: float = 0.8) -> list:
       '''
        Method to find pairs of highly correlated features.
        
        Parameters:
        correlation_matrix (pd.DataFrame): Correlation matrix of the DataFrame.
        threshold (float): Correlation threshold to identify highly correlated pairs. Defaults to 0.8.
        
        Returns:
        list: A list of tuples containing pairs of highly correlated features and their correlation coefficient.
        '''
        highly_correlated_pairs = []
        for i in range(len(correlation_matrix.columns)):
            for j in range(i):
                if abs(correlation_matrix.iloc[i, j]) > threshold:
                    highly_correlated_pairs.append((correlation_matrix.columns[i], correlation_matrix.columns[j], correlation_matrix.iloc[i, j]))
        return highly_correlated_pairs

    def drop_highly_correlated_columns(self, columns_to_drop: list) -> pd.DataFrame:
      '''
        Method to drop specified columns from the DataFrame.
        
        Parameters:
        columns_to_drop (list): List of columns to be dropped.
        
        Returns:
        pd.DataFrame: The DataFrame with the specified columns dropped.
        '''
        self.df.drop(columns=columns_to_drop, inplace=True)
        return self.df


    def get_cleaned_dataframe(self) -> pd.DataFrame:
         '''
        Method to get the cleaned DataFrame after transformations.
        
        Returns:
        pd.DataFrame: The cleaned DataFrame.
        '''
        return self.df


