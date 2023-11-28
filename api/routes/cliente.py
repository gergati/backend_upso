import mysql.connector
from flask import render_template, request, flash, jsonify
from api import app
from api.models.cliente import Cliente


# TRAER TODOS LOS CLIENTES
@app.route('/login/clientes', methods=['GET'])
def client():
    
    cur = mysql.cursor()
    cur.execute("SELECT * FROM Cliente")
    user_data = cur.fetchall()
    clientList = []
    for row in user_data:
        objecClient = Cliente(row)
        clientList.append(objecClient.to_json())
    
    return jsonify(clientList)


