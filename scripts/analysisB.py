import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to SQLite database
conn = sqlite3.connect('../database/jobs.db')

# SQL query for top 10 locations
query = """
SELECT location, COUNT(*) AS total_jobs
FROM job_listings
GROUP BY location
ORDER BY total_jobs DESC
LIMIT 10
"""

# Load query result into dataframe
df = pd.read_sql(query, conn)

# Print top 10 locations
print(df)

# Create visualization
plt.figure(figsize=(12,6))

plt.bar(df['location'], df['total_jobs'])

plt.title("Top 10 Job Locations")
plt.xlabel("Location")
plt.ylabel("Number of Jobs")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()