from kedro.io import DataCatalog
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(fraud_data: pd.DataFrame, ip_country_data: pd.DataFrame, credit_card_data: pd.DataFrame):
    return fraud_data, ip_country_data, credit_card_data


def preprocess_fraud_data(fraud_data: pd.DataFrame, ip_country_data: pd.DataFrame):
    # Handle missing values
    fraud_data = fraud_data.dropna()

    # Remove duplicates
    fraud_data = fraud_data.drop_duplicates()

    # Correct data types
    fraud_data['signup_time'] = pd.to_datetime(fraud_data['signup_time'])
    fraud_data['purchase_time'] = pd.to_datetime(fraud_data['purchase_time'])

    # Univariate analysis
    fraud_data.hist(bins=50, figsize=(20, 15))
    plt.show()

    # Bivariate analysis
    """  sns.pairplot(fraud_data, hue="class")
    plt.show() """

    # Feature Engineering
    # Convert IP addresses to integer format
    #fraud_data['ip_address_int'] = fraud_data['ip_address'].apply(ip_to_int)
     # Merge datasets
    fraud_data = fraud_data.merge(ip_country_data, how='left', left_on='ip_address', right_on='lower_bound_ip_address')

    # Transaction frequency and velocity
    fraud_data['transaction_count'] = fraud_data.groupby('user_id')['user_id'].transform('count')
    fraud_data['transaction_velocity'] = fraud_data['transaction_count'] / (fraud_data['purchase_time'] - fraud_data['signup_time']).dt.total_seconds()

    # Time-based features
    fraud_data['hour_of_day'] = fraud_data['purchase_time'].dt.hour
    fraud_data['day_of_week'] = fraud_data['purchase_time'].dt.dayofweek

    """   # Normalization and Scaling
    scaler = StandardScaler()
    fraud_data[['purchase_value', 'transaction_count', 'transaction_velocity', 'hour_of_day', 'day_of_week']] = \
        scaler.fit_transform(fraud_data[['purchase_value', 'transaction_count', 'transaction_velocity', 'hour_of_day', 'day_of_week']])

    # Encode Categorical Features
    encoder = OneHotEncoder()
    categorical_features = ['source', 'browser', 'sex']
    encoded_features = pd.DataFrame(encoder.fit_transform(fraud_data[categorical_features]), columns=encoder.get_feature_names_out(categorical_features))
    fraud_data = fraud_data.drop(columns=categorical_features).join(encoded_features) """

    return fraud_data


def preprocess_ip_country_data(ip_country_data: pd.DataFrame):
    return ip_country_data


def preprocess_credit_card_data(credit_card_data: pd.DataFrame):
    # Handle missing values
    credit_card_data = credit_card_data.dropna()

    # Remove duplicates
    credit_card_data = credit_card_data.drop_duplicates()

    # Normalization and Scaling
    scaler = StandardScaler()
    credit_card_data[['Amount']] = scaler.fit_transform(credit_card_data[['Amount']])

    return credit_card_data

def ip_to_int(ip):
    parts = ip.split('.')
    return int(parts[0]) * 256**3 + int(parts[1]) * 256**2 + int(parts[2]) * 256 + int(parts[3])

