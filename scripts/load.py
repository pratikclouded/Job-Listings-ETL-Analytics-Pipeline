from sqlalchemy import create_engine
import os

def load_data(df):

    # Get project root directory
    base_dir = os.path.dirname(os.path.dirname(__file__))

    # Create database folder path
    db_path = os.path.join(
        base_dir,
        'database',
        'jobs.db'
    )

    # Create SQLite engine
    engine = create_engine(f'sqlite:///{db_path}')

    # Load data into SQL table
    df.to_sql(
        'job_listings',
        con=engine,
        if_exists='replace',
        index=False
    )

    print("Data loaded successfully.")