import os
import pandas as pd
import snowflake.connector
from dotenv import load_dotenv

load_dotenv()

conn = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA")
)

def get_festivals_by_month(month):
    cur = conn.cursor()
    query = f"""
        SELECT * FROM festivals_2022
        WHERE TO_CHAR(Date, 'Month') ILIKE '{month}%'
    """
    cur.execute(query)
    rows = cur.fetchall()
    return pd.DataFrame(rows, columns=[col[0] for col in cur.description])

def get_tourist_data():
    cur = conn.cursor()
    query = "SELECT * FROM raw_festival_data"
    cur.execute(query)
    rows = cur.fetchall()
    return pd.DataFrame(rows, columns=[col[0] for col in cur.description])
