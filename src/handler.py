#!/usr/bin/env python3

import pandas as pd
import numpy as np


class Handler:
    def __init__(self, df):
        self.df = df

    def data_overview(self):
        print(f"Number of rows: {len(self.df)}")
        print(f"Number of columns: {len(self.df.columns)}")
        print("\nBasic Information:")
        print(self.df.info())

    def check_duplicate(self):
        # Identify and report duplicated values
        duplicates = self.df.duplicated()
        print("\nDuplicated values:")
        print(duplicates.sum(), "duplicated rows")

    def calculate_missing_percentage(self):
        # Calculate and return the percentage of missing values in each column
        self.df.replace({"None": np.nan}, inplace=True)

        missing_values = self.df.isnull().sum()
        total_rows = len(self.df)

        # Correctly calculate the percentage for each column
        missing_values_percentage = (missing_values / total_rows) * 100

        # Convert the percentages to string format with 2 decimal places
        missing_values_percentage_str = missing_values_percentage.apply(
            lambda x: f"{x:.2f}%"
        )

        # Concatenate the original missing values counts with their corresponding percentages
        new_df = pd.DataFrame(
            {
                "Missing Values": missing_values,
                "Percentage Missing": missing_values_percentage_str,
            }
        )

        print(new_df)

    def drop_duplicate(self):
        self.df.drop_duplicates(inplace=True)
        return self.df

    def drop_missing_values(self):
        """drop missing values"""
        self.df.dropna(inplace=True)

    def remove_iqr_outliers(self, col):
        """
        Removes outliers from a DataFrame column based on the Interquartile Range (IQR).

        Params:
        col (str): The name of the column to remove outliers from.
        df (DataFrame): The DataFrame to remove outliers from.

        Returns:
        DataFrame: The DataFrame with outliers removed.
        """
        # Calculate the first quartile (Q1) and third quartile (Q3)
        q1 = self.df[col].quantile(0.25)
        q3 = self.df[col].quantile(0.75)

        # Calculate the Interquartile Range (IQR)
        iqr = q3 - q1

        # Remove outliers by setting them to NaN
        self.df.loc[
            (self.df[col] < (q1 - 1.5 * iqr)) | (self.df[col] > (q3 + 1.5 * iqr)),
            col] = np.nan

        return self.df

    def stats(self):
        print("\nDescriptive Statistics:")
        print(self.df.describe())
    
    def create_date_features(self, col):
        """
        This function takes a DataFrame with a 'Date' column and adds new columns for 'Day', 'Week', 'Month', 'Year', and 'Season'.
        """
        # Extract 'Day', 'Month', and 'Year' from 'Date'
        self.df['hour_of_day'] = self.df[col].dt.hour
        self.df["day"] = self.df[col].dt.day
        self.df["day_of_week"] = self.df[col].dt.day_name()
        self.df["month"] = self.df[col].dt.month_name()
        self.df["year"] = self.df[col].dt.year
        return self.df


