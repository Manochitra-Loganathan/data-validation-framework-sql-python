
import pyodbc
import pandas as pd

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=server;DATABASE=db;UID=user;PWD=pwd')

# Compare staging and reporting totals
staging = pd.read_sql("SELECT COUNT(*) AS count FROM staging.sales_data", conn)
reporting = pd.read_sql("SELECT COUNT(*) AS count FROM reporting.sales_summary", conn)

if staging.iloc[0, 0] != reporting.iloc[0, 0]:
    print("❌ Row count mismatch!")
else:
    print("✅ Row count match.")
