import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

class Plotter:
    '''
    Class to visualise insights from the data
    '''
    def __init__ (self, original_df:pd.DataFrame, transformed_df:pd.DataFrame):
        self.original_df = original_df
        self.transformed_df = transformed_df

    def plot_null_values(self):
        #Plot null values in the original DataFrame
        null_counts_original = self.original_df.isnull().sum()
        null_counts_original = null_counts_original[null_counts_original > 0]
        null_df_original= pd.DataFrame({'Columns': null_counts_original.index, 'Null Values': null_counts_original.values})
        fig = px.bar(null_df_original, x='Columns', y='Null Values', title='Null Values in Each Column')
        fig.show()

        # Plot null values in the transformed DataFrame
        null_counts_transformed = self.transformed_df.isnull().sum()
        null_counts_transformed = null_counts_transformed[null_counts_transformed > 0]
        null_df_transformed = pd.DataFrame({'Columns': null_counts_transformed.index, 'Null Values': null_counts_transformed.values})
        fig = px.bar(null_df_transformed, x='Columns', y='Null Values', title='Null Values in Each Column (Transformed)')
        

    def plot_histogram(self, column: str):
        # Plot original data
        fig = px.histogram(self.original_df, x=column, nbins=30, title=f'Histogram of {column} (Original)')
        fig.update_layout(xaxis_title=column, yaxis_title='Frequency')
        fig.show()

        # Plot transformed data
        fig = px.histogram(self.transformed_df, x=column, nbins=30, title=f'Histogram of {column} (Transformed)')
        fig.update_layout(xaxis_title=column, yaxis_title='Frequency')
        fig.show()

    def plot_boxplot(self, column: str):
        # Plot original data
        fig = go.Figure()
        fig.add_trace(go.Box(y=self.original_df[column], name=f'{column} (Original)'))

        # Plot transformed data
        fig.add_trace(go.Box(y=self.transformed_df[column], name=f'{column} (Transformed)'))

        fig.update_layout(title=f'Boxplot of {column} (Original and Transformed)', yaxis_title='Values')
        fig.show()

    def plot_removed_outliers(self, column:str):
        fig = px.histogram(self.original_df, x=column, nbins=30, title=f'Histogram of {column} (Outliers Removed)')
        fig.update_layout(xaxis_title=column, yaxis_title='Frequency')
        fig.show()

