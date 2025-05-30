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

if __name__ == "__main__":
    app.run(debug = True)