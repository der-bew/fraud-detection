from kedro.io import DataCatalog
import pandas as pd

def load_data(fraud_data: pd.DataFrame, ip_country_data: pd.DataFrame, credit_card_data: pd.DataFrame):
    return fraud_data, ip_country_data, credit_card_data


def preprocess_fraud_data(fraud_data: pd.DataFrame):
    # Data preprocessing steps for fraud_data
    # Handle missing values, outliers, feature engineering, etc.
    return fraud_data


def preprocess_ip_country_data(ip_country_data: pd.DataFrame):
    return ip_country_data

def preprocess_credit_card_data(credit_card_data: pd.DataFrame):
    # Data preprocessing steps for credit_card_data
    return credit_card_data