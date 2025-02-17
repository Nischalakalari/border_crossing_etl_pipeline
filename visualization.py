import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname='border_data',
    user='postgres',
    password='Luffy@123',
    host='localhost',
    port='5432'
)

# SQL query to fetch data
query = """
SELECT port_name, SUM(value) AS total_crossings
FROM border_crossings
GROUP BY port_name
ORDER BY total_crossings DESC
LIMIT 10;
"""

# Read data into a pandas DataFrame
df = pd.read_sql(query, conn)

# Display the data
print(df)

# Plot the data using seaborn
plt.figure(figsize=(10, 6))
sns.barplot(x='total_crossings', y='port_name', data=df)
plt.title('Top 10 Ports by Border Crossings')
plt.xlabel('Total Crossings')
plt.ylabel('Port Name')
plt.show()

# Close the database connection
conn.close()
