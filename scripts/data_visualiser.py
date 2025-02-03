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

    def loan_indicators(self):
        # Subset of users who have stopped paying (charged off) and those currently behind on payments
        risk_statuses = ['Late (31-120 days)', 'Late (16-30 days)', 'Charged Off']
        risk_customers = self.df[self.df['loan_status'].isin(risk_statuses)]

        # Add a new column to distinguish between those already charged off and those at risk
        risk_customers.loc[:, 'risk_category'] = risk_customers['loan_status'].apply(lambda x: 'Charged Off' if x == 'Charged Off' else 'At Risk')

        fig_grade = px.histogram(risk_customers, x='grade', color='risk_category', barmode='group', title='Effect of Loan Grade on Payment Status')
        fig_grade.show()

        # Purpose effect
        fig_purpose = px.histogram(risk_customers, x='purpose', color='risk_category', barmode='group', title='Effect of Loan Purpose on Payment Status')
        fig_purpose.show()

        # Home ownership effect
        fig_home_ownership = px.histogram(risk_customers, x='home_ownership', color='risk_category', barmode='group', title='Effect of Home Ownership on Payment Status')
        fig_home_ownership.show()

        # Analysis results
        print("Analysis Results:")
        print("Grade distribution for Charged Off and At Risk loans:")
        print(risk_customers.groupby(['grade', 'risk_category']).size())

        print("\nPurpose distribution for Charged Off and At Risk loans:")
        print(risk_customers.groupby(['purpose', 'risk_category']).size())

        print("\nHome Ownership distribution for Charged Off and At Risk loans:")
        print(risk_customers.groupby(['home_ownership', 'risk_category']).size())
        