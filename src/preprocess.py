import pandas as pd

def clean_data(df):
    # Drop or fill missing values
    df = df.dropna()  # or df.fillna(0)
    return df
