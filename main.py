# main.py

from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data

df = extract_data()

cleaned_df = transform_data(df)

load_data(cleaned_df)

print("ETL Pipeline Completed.")