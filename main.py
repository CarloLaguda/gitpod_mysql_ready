import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

#CREATE E SHOW DATABASE
mycursor.execute("CREATE DATABASE mydatabase")
mycursor.execute("SHOW DATABASES")

#CREATE TABLE
mycursor.execute("CREATE TABLE IF NOT EXISTS customers (name VARCHAR(255), address VARCHAR(255))")

#PROCEDURA PER INSERT
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
mydb.commit()

#PROCEDURA PER SELECT
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()


for x in mycursor:
  print(x)
##