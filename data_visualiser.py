import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
import webbrowser
import os

class DataVisualiser:
    '''
    Class to visualise insights from the data
    '''
    def __init__(self, df: pd.DataFrame):
        '''
        Initialise with a DataFrame.

        Parameters
        df(pd.DataFrame): The DataFrame to be transformed.
        '''
        self.df = df

    def plot_correlation_matrix(self, columns: list , save_as_html : bool =False, file_name: str ='correlation_matrix.html'):
        '''
        Method to plot the correlation matrix of the given columns in the DataFrame.
        
        Parameters:
        columns (list): List of columns to include in the correlation matrix.
        save_as_html (bool): Whether to save the plot as an HTML file. Defaults to False.
        file_name (str): The file name for saving the HTML plot. Defaults to 'correlation_matrix.html'.
        
        Returns:
        None
        '''
        selected_df = self.df[columns]

        correlation_matrix = selected_df.corr() 

        fig = px.imshow(correlation_matrix, text_auto=True, aspect="auto", color_continuous_scale='RdBu_r')
        fig.update_layout(title='Correlation Matrix', width=800, height=800)
        fig.show()

        if save_as_html:
            fig.write_html(file_name)
            webbrowser.open('file://' + os.path.realpath(file_name))
        else:
            pio.show(fig, renderer='browser') 