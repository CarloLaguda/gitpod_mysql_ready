import mysql.connector
import pandas as pd
import numpy as np # Import numpy to work with NaN values

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
mycursor = mydb.cursor()

# Create the DB (if not already exists)
mycursor.execute("CREATE DATABASE IF NOT EXISTS RIDERS")

mycursor.execute("""
    CREATE TABLE IF NOT EXISTS RIDERS.motogp (
        Driver VARCHAR(100) NOT NULL,
        Victories INT NOT NULL,
        Second_Places INT NOT NULL,
        Third_Places INT NOT NULL,
        Pole_Positions INT NOT NULL,
        Race_Fastest_Laps INT NOT NULL,
        World_Championships INT NOT NULL,
        Nationality VARCHAR(100) NOT NULL
    );
""")

# Delete data from the table before inserting new data
mycursor.execute("DELETE FROM RIDERS.motogp")
mydb.commit()

# Read data from a csv file
riders = pd.read_csv('./motogp_allriders.csv', delimiter=',')


#Gestione colonne nulle
numeric_cols = ['Victories', 'Second_Places', 'Third_Places', 'Pole_Positions', 'Race_Fastest_Laps', 'World_Championships']
for col in numeric_cols:
    # Convert column to numeric, coercing errors to NaN, then fill NaN with 0
    riders[col] = pd.to_numeric(riders[col], errors='coerce').fillna(0).astype(int)

# For string columns, fill NaN with empty string
string_cols = ['Driver', 'Nationality']
for col in string_cols:
    riders[col] = riders[col].fillna('')

print(riders)

# Fill the table
for i, row in riders.iterrows():
    cursor = mydb.cursor()
    sql = "INSERT INTO RIDERS.motogp VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values_to_insert = tuple(row.values)
    try:
        cursor.execute(sql, values_to_insert)
        mydb.commit()
    except mysql.connector.Error as err:
        print(f"Error inserting row {i}: {err}")
        print(f"Row data: {values_to_insert}")
        mydb.rollback() #Mantiene integrità dei dati

mycursor.execute("SELECT * FROM RIDERS.motogp")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# Close the cursor and connection
mycursor.close()
mydb.close()
