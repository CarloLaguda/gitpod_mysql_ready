import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "Animali"
)

mycursor = mydb.cursor()

mycursor.execute("USE Animali")


# CONSEGNA
animali = [
    ("Leo", "Leone", 190, 8),
    ("Rex", "Pastore Tedesco", 40, 5),
    ("Milo", "Bulldog", 25, 4),
    ("Luna", "Gatto", 4, 2),
    ("Coco", "Cane", 30, 3)
]

mycursor.executemany("""
    INSERT INTO Mammiferi (nome_proprio, razza, peso, eta)
    VALUES (%s, %s, %s, %s)
""", animali)


mydb.commit()

# Verifica inserimento: selezioniamo tutti gli animali
mycursor.execute("SELECT * FROM Mammiferi")

# Mostra i risultati
for x in mycursor:
    print(x)

# Chiudi la connessione
mycursor.close()
mydb.close()