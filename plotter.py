import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

class Plotter:
    '''
    Class to visualise insights from the data
    '''
    def __init__ (self, df:pd.DataFrame):
        self.df = df

    def plot_null_values(self):
        null_counts = self.df.isnull().sum()
        null_counts = null_counts[null_counts > 0]
        null_df = pd.DataFrame({'Columns': null_counts.index, 'Null Values': null_counts.values})
        fig = px.bar(null_df, x='Columns', y='Null Values', title='Null Values in Each Column')
        fig.show()