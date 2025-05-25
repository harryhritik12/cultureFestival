import os
import pandas as pd
from datetime import datetime
import snowflake.connector
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Establish connection
conn = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA")
)
cursor = conn.cursor()

# === LOAD AND INSERT festivals.csv ===
df1 = pd.read_csv("c:/Users/hriti/OneDrive/Desktop/cultureFestival/snowflake/festivals.csv")

# Create table
cursor.execute("""
    CREATE OR REPLACE TABLE festivals_2022 (
        Id NUMBER,
        Day VARCHAR,
        Date DATE,
        Year NUMBER,
        Festival_Name VARCHAR
    )
""")

# Insert rows with corrected date format
for _, row in df1.iterrows():
    try:
        # Convert "January 1" + year => YYYY-MM-DD
        month_day = row['Date']
        year = int(row['Year'])
        full_date = datetime.strptime(f"{month_day} {year}", "%B %d %Y").date()
        
        cursor.execute("""
            INSERT INTO festivals_2022 (Id, Day, Date, Year, Festival_Name)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            int(row['Id']),
            row['Day'],
            full_date,  # converted date
            year,
            row['Festival_name']
        ))
    except Exception as e:
        print(f"Error inserting row {row['Id']}: {e}")

print("Uploaded festivals_2022")

# === LOAD AND INSERT Data.csv ===
df2 = pd.read_csv("c:/Users/hriti/OneDrive/Desktop/cultureFestival/snowflake/Data.csv")

# Confirm columns (optional debug)
print("Columns in Data.csv:", df2.columns)

# Create table (optional: rename if columns are different)
cursor.execute("""
    CREATE OR REPLACE TABLE raw_festival_data (
        Month VARCHAR,
        Value_2021 NUMBER,
        Value_2022 NUMBER,
        Growth_2022_21 FLOAT
    )
""")

# Insert values into the second table
for _, row in df2.iterrows():
    try:
        cursor.execute("""
            INSERT INTO raw_festival_data (Month, Value_2021, Value_2022, Growth_2022_21)
            VALUES (%s, %s, %s, %s)
        """, (
            row['Month'],
            float(row['2021']),
            float(row['2022']),
            float(row['Growth 2022/21'])
        ))
    except Exception as e:
        print(f"Error inserting month {row['Month']}: {e}")

print("Uploaded Data.csv")

# Cleanup
cursor.close()
conn.close()
