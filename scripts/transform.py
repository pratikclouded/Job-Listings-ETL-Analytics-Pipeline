import pandas as pd

def transform_data(df):

    # Remove duplicates
    df = df.drop_duplicates()

    # Fill missing values
    df = df.fillna('Not Available')

    # Salary cleaning
    if 'salary' in df.columns:

        df['salary'] = (
            df['salary']
            .replace('Not Available', 0)
        )

        df['salary'] = (
            df['salary']
            .astype(str)
            .str.replace(',', '')
        )

        df['salary'] = (
            pd.to_numeric(
                df['salary'],
                errors='coerce'
            )
            .fillna(0)
            .astype(int)
        )

    return df