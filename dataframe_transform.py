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
        new_df = self.df.drop(columns=columns)
        return new_df

    def impute_missing_values(self, df: pd.DataFrame, strategy: str = 'median') -> pd.DataFrame:
        for column in df.columns:
            if df[column].isnull().sum() > 0:
                if df[column].dtype in ['float64','int64']:
                    if strategy == 'median':
                        df[column].fillna(self.df[column].median())
                    elif strategy == 'mean':
                        df[column].fillna(self.df[column].mean())
                else:
                    df[column] = self.df[column].fillna(self.df[column].mode()[0])
        return df

    def transform_skewed_cols(self, columns:list) -> pd.DataFrame:
        for column in columns:
            #Apply log transformation
            log_transformed = np.log1p(self.df[column])
            log_skewness = log_transformed.skew()

            # Apply square root transformation
            sqrt_transformed = np.sqrt(self.df[column])
            sqrt_skewness = sqrt_transformed.skew()

            # Apply Box-Cox transformation (requires positive values)
            boxcox_transformed, _ = boxcox(self.df[column] + 1)
            boxcox_skewness = pd.Series(boxcox_transformed).skew()

            # Determine the best transformation
            transformations = {
                'log': log_skewness,
                'sqrt': sqrt_skewness,
                'boxcox': boxcox_skewness
            }
            best_transformation = min(transformations, key=transformations.get)

            # Apply the best transformation
            if best_transformation == 'log':
                self.df[column] = log_transformed
            elif best_transformation == 'sqrt':
                self.df[column] = sqrt_transformed
            elif best_transformation == 'boxcox':
                self.df[column] = boxcox_transformed

        return self.df 

    def get_cleaned_dataframe(self) -> pd.DataFrame:
        return self.df
