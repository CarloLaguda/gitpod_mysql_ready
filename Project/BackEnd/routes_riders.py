from flask import Flask, jsonify
from flask_cors import CORS 

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