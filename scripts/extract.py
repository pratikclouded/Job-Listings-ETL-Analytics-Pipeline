# extract.py

import pandas as pd

def extract_data():
    df = pd.read_csv('data/linkedin-jobs-usa.csv')
    print(df.head())
    return df