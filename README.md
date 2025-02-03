# Project_Customer_loans_in_finance-AiCore

## Table of Contents
- [Introduction](#Introduction)
- [Learnings](#Learnings)
- [Installation](#Installation)
- [Usage](#Usage)
- [Structure](#Structure)
- [License](#License)


## Introduction

This project is part of the AiCore curriculum. The goal of the project is to perform exploratory data analysis (EDA) using various statistical and data visualisation techniques to uncover patterns, relationships, and anomalies in the loan data. This analysis enables informed decisions about loan approvals, pricing, and risk management, ultimately improving the performance and profitability of the loan portfolio.

## Learnings
- **Data Analysis:** Techniques for exploring and understanding large datasets.
- **Statistical Methods:** Applying statistical methods to identify patterns and relationships.
- **Data Visualisation:** Creating insightful visualisations to communicate findings effectively.
- **Risk Management:** Understanding the risk and return associated with loans.
- **Decision-Making:** Providing data-driven insights for better business decisions.

## Installation
1. clone the repo to your local machine:

        Bash:
           git clone https://github.com/yourusername/CUSTOMER_LOANS_IN_FINANCE_PROJECT_2.git
           cd CUSTOMER_LOANS_IN_FINANCE_PROJECT_2

2. Set up a virtual environment (optional but recommended): 

        python -m venv env
        source env/bin/activate  # On Windows use `env\Scripts\activate`


3. Install the required dependencies using the following command:

        Bash:
           pip install -r requirements.txt

4. Configure the necessary credentials in the `config/credentials.yaml` file.
   

## Usage

**Load Credentials:**

- Ensure config/credentials.yaml contains the necessary credentials.
  

**Run EDA Notebooks:**

- Execute EDA_Analysis.ipynb and EDA_loan_portfolio.ipynb in notebooks/.
- 

**Transform and Clean Data:**

- Run scripts in scripts/ directory for data transformation.

**Extract Data from Database:**

- Use RDSDatabaseConnector class to connect and extract data.

**Review Results:**

- Check results/ directory for analysis outputs.

**Generate Visualisations:**

- Run plotter.py in scripts/ for visualisations.

## Structure

**config**

`credentials.yaml`: Contains configuration settings and credentials required for the project.

**data**

`final_df.csv`: The final dataset used for analysis.

`loan_payments_copy.csv`: A copy of the loan payments dataset.

`loan_payments.csv`: The original loan payments dataset.

**notebooks**

`EDA_Analysis.ipynb`: Jupyter notebook for exploratory data analysis (EDA).

`EDA_loan_portfolio.ipynb`: Jupyter notebook for EDA focused on the loan portfolio.

`Personal_Learnings.ipynb`: Jupyter notebook documenting personal learnings and insights gained during the project.

**results**

`correlation_matrix.html`: HTML file containing the correlation matrix visualization.

**scripts**

`data_transform.py`: Script for transforming the data.

`data_visualiser.py`: Script for visualizing the data.

`dataframe_info.py`: Script for extracting information from dataframes.

`dataframe_transform.py`: Script for transforming dataframes.

`db_utils.py`: Utility script for database operations.

`plotter.py`: Script for plotting data visualizations.

**other files**

`.gitignore`: Specifies files and directories to be ignored by Git.

`README.md`: This file, providing an overview of the project.

`requirements.txt`: Lists the dependencies and packages required for the project.


##License
This project is licensed under the MIT License.
