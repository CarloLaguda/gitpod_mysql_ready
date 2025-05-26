import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
)

mycursor = mydb.cursor()

# CREATE E SHOW DATABASE
mycursor.execute("CREATE DATABASE IF NOT EXISTS Animali")
"""
mycursor.execute("SHOW DATABASES")

# Fetch the results of SHOW DATABASES to clear the result set
for db in mycursor.fetchall():
    print(db)
"""
# Select the 'Animali' database before creating the table
mycursor.execute("USE Animali")

# CREATE TABLE
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS Mammiferi (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome_proprio VARCHAR(255),
        razza VARCHAR(255),
        peso INT,
        eta INT
    )
""")

# Show the tables in the current database
mycursor.execute("SHOW TABLES")

# Fetch the results of SHOW TABLES to see the created tables
for table in mycursor:
    print(table)

# Close the cursor and connection
mycursor.close()
mydb.close()
