import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "Animali"
)

mycursor = mydb.cursor()

#select
mycursor.execute("SELECT * FROM Mammiferi")

#STAMPA
for x in mycursor:
    print(x)

#Chiudi la connessione
mycursor.close()
mydb.close()