import sqlite3

# Connect to the database file
conn = sqlite3.connect('data.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()
cursor.execute("SELECT * FROM your_table_name")

# Fetch all rows from the executed query
rows = cursor.fetchall()
for row in rows:
    print(row)
# Close the cursor and connection
cursor.close()
conn.close()
