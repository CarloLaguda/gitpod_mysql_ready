import mysql.connector

#Connessione al database MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Animali"  #Seleziona il database Animali
)
mycursor = mydb.cursor()
mycursor.execute("USE Animali")

def chiedi_integro(prompt):
    while True:
        try:
            # Chiedi l'input e prova a convertirlo in intero
            valore = int(input(prompt))
            return valore
        except ValueError:
            print("Errore: per favore inserisci un numero intero valido.")

for _ in range(1):  #Ripeti per 5 volte
        print("\nInserisci i dettagli per un nuovo animale:")

        # Chiedi all'utente di inserire i dati per ogni animale
        nome_proprio = input("Nome proprio: ")
        razza = input("Razza: ")

        peso = chiedi_integro("Peso (in kg): ")  # Verifica che il peso sia un intero
        eta = chiedi_integro("Età (in anni): ")   # Verifica che l'età sia un intero

        # Esegui l'inserimento nel database
        mycursor.execute("""
            INSERT INTO Mammiferi (nome_proprio, razza, peso, eta)
            VALUES (%s, %s, %s, %s)
        """, (nome_proprio, razza, peso, eta))


"""
mycursor.close()
mydb.close()
"""