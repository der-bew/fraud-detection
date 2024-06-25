from kedro.pipeline import Pipeline, node
from .nodes import (
    load_data, preprocess_fraud_data, preprocess_ip_country_data, preprocess_credit_card_data
)

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=load_data,
                inputs=["fraud_data", "ip_country_data", "credit_card_data"],
                outputs=["raw_fraud_data", "raw_ip_country_data", "raw_credit_card_data"],
                name="load_data_node"
            ),
            node(
                func=preprocess_fraud_data,
                inputs=["raw_fraud_data", "raw_ip_country_data"],
                outputs="preprocessed_fraud_data",
                name="preprocess_fraud_data_node"
            ),
            node(
                func=preprocess_ip_country_data,
                inputs="raw_ip_country_data",
                outputs="preprocessed_ip_country_data",
                name="preprocess_ip_country_data_node"
            ),
            node(
                func=preprocess_credit_card_data,
                inputs="raw_credit_card_data",
                outputs="preprocessed_credit_card_data",
                name="preprocess_credit_card_data_node"
            )
        ]
    )

