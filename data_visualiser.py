import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

class DataVisualiser:
    '''
    Class to visualise insights from the data
    '''
    def __init__(self, df: pd.DataFrame):
        self.df = df


    def plot_correlation_matrix(self, columns:pd.DataFrame):
        '''
        Method to plot the correlation matrix of the given DataFrame
        '''
        # Convert non-numeric columns to numeric and drop columns with non-numeric values

        correlation_matrix = columns.corr() 
        
        fig = px.imshow(correlation_matrix, text_auto=True, aspect="auto", color_continuous_scale='RdBu_r')
        fig.update_layout(title='Correlation Matrix', width=800, height=800)
        fig.show()