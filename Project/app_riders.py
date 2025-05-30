import mysql.connector
import pandas as pd

# Connect to MySQL database
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
        Victories INTEGER NOT NULL,
        Second_Places INTEGER NOT NULL,
        Third_Places INTEGER NOT NULL,
        Pole_Positions INTEGER NOT NULL,
        Race_Fastest_Laps INTEGER NOT NULL,
        World_Championships INTEGER NOT NULL,
        Nationality VARCHAR(100) NOT NULL
    );
""")

# Delete data from the table before inserting new data
mycursor.execute("DELETE FROM RIDERS.motogp")
mydb.commit()

# Read data from a CSV file
riders = pd.read_csv('./motogp_allriders.csv', delimiter=',')
print(riders)

#Fill the table
for i,row in riders.iterrows():
    cursor = mydb.cursor()
    #here %S means string values 
    sql = "INSERT INTO RIDERS.motogp VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit()

#Check if the table has been filled
mycursor.execute("SELECT * FROM RIDERS.motogp")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
