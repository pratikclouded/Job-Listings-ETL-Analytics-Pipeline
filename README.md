# Job Listings ETL & Analytics Pipeline

A beginner-friendly Data Engineering project built using Python, Pandas, SQLite, SQLAlchemy, and Matplotlib. This project demonstrates the complete ETL (Extract, Transform, Load) workflow by processing job listings data and generating analytical insights through SQL queries and visualizations.

## Project Overview

This pipeline:
- Extracts job listings data from a CSV dataset
- Cleans and transforms raw data using Pandas
- Loads processed data into a SQLite database
- Performs SQL-based analysis
- Visualizes hiring trends using Matplotlib

The project is designed to simulate a real-world ETL workflow used in Data Engineering and Data Analytics roles.

## Tech Stack

- Python
- Pandas
- SQLite
- SQLAlchemy
- Matplotlib
- VS Code

## Project Structure

```bash
Job_ETL_Project/
│
├── data/
│   └── linkedin-jobs-usa.csv
│
├── database/
│   └── jobs.db
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── analysis.py
│
├── main.py
├── requirements.txt
└── README.md


ETL Workflow
Extract
Reads raw job listings data from CSV files

Transform
Removes duplicate records
Handles missing values
Cleans and standardizes data
Converts data types safely

Load
Loads transformed data into a SQLite database using SQLAlchemy
Analysis & Visualization
Executes SQL queries for business insights
Visualizes top hiring locations using Matplotlib

Features
Modular ETL architecture
SQL database integration
Data cleaning and preprocessing
Analytical SQL queries
Visualization of hiring trends
Beginner-friendly and resume-ready project

Sample Insights
Top hiring locations
Most active hiring companies
Most common job titles
Hiring trend analysis

How to Run
Clone Repository
git clone <your-repo-link>
cd Job_ETL_Project

Create Virtual Environment
python -m venv venv
Activate Environment

Windows
venv\Scripts\activate

Install Dependencies
pip install -r requirements.txt

Run ETL Pipeline
python main.py
Run Analysis

cd scripts
python analysis.py

Future Improvements
Live job scraping using BeautifulSoup or Selenium
PostgreSQL/MySQL integration
Automated ETL scheduling
Power BI dashboard integration
API-based data extraction

Author
Pratik Bhul