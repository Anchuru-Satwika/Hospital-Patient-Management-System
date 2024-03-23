import pandas as pd
import openpyxl
from sqlalchemy import create_engine


# Database connection string
conn_string = 'postgresql://postgres:password@localhost/Hospital_Patient_Management_System'
db = create_engine(conn_string)
conn = db

files = ['Doctors', 'Patients', 'Medical_Reports']

for file in files:
    # Read Excel file into DataFrame
    df = pd.read_excel(f'C:\\Users\\Admin\\Desktop\\projects\\Hospital_Patient_Management_System\\{file}.xlsx')
    # Insert data into PostgreSQL
    df.to_sql(file, con=conn, if_exists='replace', index=False)

print("Data loaded successfully into PostgreSQL.")
