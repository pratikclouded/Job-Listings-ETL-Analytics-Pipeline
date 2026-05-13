# analysis.py

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
conn = sqlite3.connect('../database/jobs.db')

query = """
SELECT location, COUNT(*) as total_jobs
FROM job_listings
GROUP BY location
ORDER BY total_jobs DESC
"""

df = pd.read_sql(query, conn)

print(df)# analysis.py

import sqlite3
import pandas as pd

conn = sqlite3.connect('../database/jobs.db')

query = """
SELECT location, COUNT(*) as total_jobs
FROM job_listings
GROUP BY location
ORDER BY total_jobs DESC
"""

df = pd.read_sql(query, conn)

print(df)

# Create chart
plt.figure(figsize=(12,6))

plt.bar(df['location'], df['total_jobs'])

plt.xlabel("Location")
plt.ylabel("Number of Jobs")
plt.title("Top Job Locations")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()