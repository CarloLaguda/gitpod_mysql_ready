import mysql.connector

#Connessione al database MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Animali"  #Seleziona il database Animali
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Mammiferi WHERE peso > 20")

#STAMPA
for x in mycursor:
    print(x)

#Chiudi la connessione
mycursor.close()
mydb.close()