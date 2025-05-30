from flask import Flask, jsonify
from flask_cors import CORS 
import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="RIDERS"
)
mycursor = mydb.cursor()

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    mycursor.execute("SELECT * FROM RIDERS.motogp")
    myresult = mycursor.fetchall()
    column_names = [desc[0] for desc in mycursor.description]
    result = []
    for row in myresult:
        row_dict = dict(zip(column_names, row))
        result.append(row_dict)
    return jsonify(result)

@app.route("/MostPole/<int:numero>")
def mostPole(numero):
    mycursor.execute(f"SELECT Driver,Pole_Positions FROM RIDERS.motogp ORDER BY Pole_Positions DESC LIMIT {numero};")
    myresult = mycursor.fetchall()
    column_names = [desc[0] for desc in mycursor.description]
    result = []
    for row in myresult:
        row_dict = dict(zip(column_names, row))
        result.append(row_dict)
    return jsonify(result)

@app.route("/MostWin/<int:numero>")
def mostWin(numero):
    mycursor.execute(f"SELECT Driver,Victories FROM RIDERS.motogp ORDER BY Victories DESC LIMIT {numero};")
    myresult = mycursor.fetchall()
    column_names = [desc[0] for desc in mycursor.description]
    result = []
    for row in myresult:
        row_dict = dict(zip(column_names, row))
        result.append(row_dict)
    return jsonify(result)

@app.route("/MostWin_Championship/<int:numero>")
def mostWin_Champio(numero):
    mycursor.execute(f"SELECT Driver,World_Championships FROM RIDERS.motogp ORDER BY World_Championships DESC LIMIT {numero};")
    myresult = mycursor.fetchall()
    column_names = [desc[0] for desc in mycursor.description]
    result = []
    for row in myresult:
        row_dict = dict(zip(column_names, row))
        result.append(row_dict)
    return jsonify(result)

@app.route("/Nations/<nazione>")
def nation(nazione):
    mycursor.execute("SELECT * FROM RIDERS.motogp WHERE Nationality = %s;", (nazione,))
    myresult = mycursor.fetchall()
    column_names = [desc[0] for desc in mycursor.description]
    result = []
    for row in myresult:
        row_dict = dict(zip(column_names, row))
        result.append(row_dict)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug = True)