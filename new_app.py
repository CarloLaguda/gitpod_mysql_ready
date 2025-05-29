import mysql.connector
from flask import Flask, jsonify
from flask_cors import CORS 

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="CLASH_ROYALE"
)
mycursor = mydb.cursor()

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/getAllDataInHtml")
def getAllData():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit")
    myresult = mycursor.fetchall()
    column_names = [desc[0] for desc in mycursor.description]
    result = []
    for row in myresult:
        row_dict = dict(zip(column_names, row))
        result.append(row_dict)
    return jsonify(result)

@app.route("/getAirTransport")
def AirTransport():
    mycursor.execute('''SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE Transport = "Air"''')
    myresult = mycursor.fetchall()
    column_names = [desc[0] for desc in mycursor.description]
    result = []
    for row in myresult:
        row_dict = dict(zip(column_names, row))
        result.append(row_dict)
    return jsonify(result)

@app.route("/getEpic_units")
def Epic_units():
    mycursor.execute('''SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE Rarity = "Epic"''')
    myresult = mycursor.fetchall()
    column_names = [desc[0] for desc in mycursor.description]
    result = []
    for row in myresult:
        row_dict = dict(zip(column_names, row))
        result.append(row_dict)
    return jsonify(result)

@app.route("/getTarget")
def Target():
    mycursor.execute('''SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE Target = "Buildings"''')
    myresult = mycursor.fetchall()
    column_names = [desc[0] for desc in mycursor.description]
    result = []
    for row in myresult:
        row_dict = dict(zip(column_names, row))
        result.append(row_dict)
    return jsonify(result)

@app.route("/getCost")
def Cost():
    mycursor.execute('''SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE Cost > 3''')
    myresult = mycursor.fetchall()
    column_names = [desc[0] for desc in mycursor.description]
    result = []
    for row in myresult:
        row_dict = dict(zip(column_names, row))
        result.append(row_dict)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
