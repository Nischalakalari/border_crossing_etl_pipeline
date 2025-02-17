import pandas as pd 
import psycopg2
from datetime import datetime 

#Load the data 
csv_path = '/Users/nischalakalari/Desktop/GitHub Projects/etl_pipeline/Border_Crossing_Entry_Data.csv'
df = pd.read_csv(csv_path)

#cleaning the data 
df.drop_duplicates(inplace=True)
df.fillna('unknown', inplace=True)

#Funtion to convert date fromates 
def convert_date(date_str):
    try:
        return datetime.strptime(date_str, '%b %Y').date()
    except ValueError:
        return None
    
#connecting to the Postgresql 
conn = psycopg2.connect(
    dbname='border_data',
    user='postgres',
    password='Luffy@123',
    port='5432'
)
cur = conn.cursor()

#Create table 
cur.execute("""
            CREATE TABLE IF NOT EXISTS border_crossings(
                port_name VARCHAR(255),
                state VARCHAR(255),
                port_code INT,
                border VARCHAR(50),
                date DATE,
                measure VARCHAR(255),
                value INT
                );
                """)

#  Insert data 
for _, row in df.iterrows():
    cur.execute("""
                INSERT INTO border_crossings (port_name, state, port_code, border, date, measure, value)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (
                    str(row['Port Name']),
                    str(row['State']),
                    int(row['Port Code']) if pd.notnull(row['Port Code']) else None,
                    str(row['Border']),
                    convert_date(row['Date']),
                    str(row['Measure']),
                    int(row['Value']) if pd.notnull(row['Value']) else 0
                    ))
#Commit and close connection 
conn.commit()
cur.close()
conn.close()

print("Data successfully inserted into PostgreSQL!")
    
