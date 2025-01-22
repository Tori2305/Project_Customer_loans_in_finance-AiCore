from sqlalchemy import create_engine
import psycopg2
import pandas as pd
import yaml


class RDSDatabaseConnector: 
    def __init__(self, credentials:dict):
        '''
        Initialises the RDSDatabaseConnector with the AiCore provided details
        '''
        self.credentials = credentials
        self.engine = None
    
    def initialise_engine(self):
        '''
        Initialises a SQLAlchemy engine using the provided credentials
        '''
        try:
            engine_url = (f"postgresql://{self.credentials['RDS_USER']}:{self.credentials['RDS_PASSWORD']}@{self.credentials['RDS_HOST']}/{self.credentials['RDS_DATABASE']}")
            self.engine=create_engine(engine_url)
            print("SQLAlchemy engine initialized successfully.")
        except Exception as e:
            print(f"Error initializing SQLAlchemy engine: {e}")

    def extract_data(self, query:str) -> pd.DataFrame:
        '''
        extracts data from engine if it's been initialised correctly 
        '''
        if self.engine is None: 
            raise ValueError ("Engine is not initialised. Call initialise_engine() first")
        return pd.read_sql(query,self.engine)
        
    def save_to_csv (self, data: pd.DataFrame, filename: str):
        data.to_csv(filename, index=False)

    def disconnect(self):
        '''
        Closes the SQLAlchemy engine connection if one exists
        '''
        if self.engine:
            self.engine.dispose()
            print("SQLAlchemy engine connection is closed")
        else:
            print("No active connection to close.")

def load_credentials(filepath:str) -> dict:
    try:
        with open(filepath, "r") as f:
            credentials = yaml.safe_load(f)
            return credentials
    except Exception as e:
        print(f" Error loading in credentials: {e}")
        return {}

if __name__ == "__main__":
    credentials = load_credentials("credentials.yaml")

    connector = RDSDatabaseConnector(credentials)
    connector.initialise_engine()
    
    query = "SELECT * FROM loan_payments"
    data = connector.extract_data(query)

    if not data.empty:
        connector.save_to_csv(data,"loan_payments.csv")
    
    connector.disconnect()

