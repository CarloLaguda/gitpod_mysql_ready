from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

mydb = None
mycursor = None

def connect_to_db():
    global mydb, mycursor
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="RIDERS"
        )
        mycursor = mydb.cursor()
        print("Connessione al database MySQL stabilita con successo!")
        return True
    except mysql.connector.Error as err:
        print(f"Errore durante la connessione a MySQL: {err}")
        mydb = None
        mycursor = None
        return False

if not connect_to_db():
    print("Connessione al database fallita all'avvio. Le route API potrebbero non funzionare.")

@app.route("/")
def home():
    if not mydb or not mycursor:
        return jsonify({"error": "Connessione al database non stabilita"}), 500
    try:
        mycursor.execute("SELECT * FROM RIDERS.motogp")
        myresult = mycursor.fetchall()
        column_names = [desc[0] for desc in mycursor.description]
        result = []
        for row in myresult:
            row_dict = dict(zip(column_names, row))
            result.append(row_dict)
        return jsonify(result)
    except mysql.connector.Error as err:
        print(f"Errore durante l'esecuzione della query nella route home: {err}")
        return jsonify({"error": "Errore nella query del database"}), 500

@app.route("/MostPole/<int:numero>")
def mostPole(numero):
    if not mydb or not mycursor:
        return jsonify({"error": "Connessione al database non stabilita"}), 500
    try:
        mycursor.execute("SELECT Driver,Pole_Positions, Nationality FROM RIDERS.motogp WHERE Pole_Positions >= %s ORDER BY Pole_Positions DESC;", (numero,))
        myresult = mycursor.fetchall()
        column_names = [desc[0] for desc in mycursor.description]
        result = []
        for row in myresult:
            row_dict = dict(zip(column_names, row))
            result.append(row_dict)
        return jsonify(result)
    except mysql.connector.Error as err:
        print(f"Errore durante l'esecuzione della query nella route MostPole: {err}")
        return jsonify({"error": "Errore nella query del database"}), 500

@app.route("/MostWin/<int:numero>")
def mostWin(numero):
    if not mydb or not mycursor:
        return jsonify({"error": "Connessione al database non stabilita"}), 500
    try:
        mycursor.execute("SELECT Driver,Victories, Nationality FROM RIDERS.motogp WHERE Victories >= %s ORDER BY Victories DESC;", (numero,))
        myresult = mycursor.fetchall()
        column_names = [desc[0] for desc in mycursor.description]
        result = []
        for row in myresult:
            row_dict = dict(zip(column_names, row))
            result.append(row_dict)
        return jsonify(result)
    except mysql.connector.Error as err:
        print(f"Errore durante l'esecuzione della query nella route MostWin: {err}")
        return jsonify({"error": "Errore nella query del database"}), 500

@app.route("/MostWin_Championship/<int:numero>")
def mostWin_Champio(numero):
    if not mydb or not mycursor:
        return jsonify({"error": "Connessione al database non stabilita"}), 500
    try:
        mycursor.execute("SELECT Driver,World_Championships, Nationality FROM RIDERS.motogp WHERE World_Championships >= %s ORDER BY World_Championships DESC;", (numero,))
        myresult = mycursor.fetchall()
        column_names = [desc[0] for desc in mycursor.description]
        result = []
        for row in myresult:
            row_dict = dict(zip(column_names, row))
            result.append(row_dict)
        return jsonify(result)
    except mysql.connector.Error as err:
        print(f"Errore durante l'esecuzione della query nella route MostWin_Championship: {err}")
        return jsonify({"error": "Errore nella query del database"}), 500

@app.route("/Nations/<nazione>")
def nation(nazione):
    if not mydb or not mycursor:
        return jsonify({"error": "Connessione al database non stabilita"}), 500
    try:
        mycursor.execute("SELECT * FROM RIDERS.motogp WHERE Nationality = %s;", (nazione,))
        myresult = mycursor.fetchall()
        column_names = [desc[0] for desc in mycursor.description]
        result = []
        for row in myresult:
            row_dict = dict(zip(column_names, row))
            result.append(row_dict)
        return jsonify(result)
    except mysql.connector.Error as err:
        print(f"Errore durante l'esecuzione della query nella route Nations: {err}")
        return jsonify({"error": "Errore nella query del database"}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)