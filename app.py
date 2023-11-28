from flask import Flask, jsonify, request, redirect, url_for, flash
import mysql.connector
from flask.templating import render_template
from api.models.usuario import Usuario
from api.models.cliente import Cliente
from api.models.producto import Producto
from flask_cors import CORS
#from api import app

app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'AdminTotal'
app.config['MYSQL_PASSWORD'] = 'admintotal123!'
app.config['MYSQL_DB'] = 'AdminTotal'


mysql = mysql.connector.connect(
    host='localhost',
    user='AdminTotal',
    password='admintotal123!',
    database='AdminTotal'
)


if __name__ == '__main__':
    app.run(debug=True, port=5000)