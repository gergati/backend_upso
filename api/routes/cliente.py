from api import app
from api.db.db import mysql
from flask import request, jsonify
from api.models.cliente import Cliente


# TRAER TODOS LOS CLIENTES
@app.route('/clientes', methods=['GET'])
def client():
    cur = mysql.cursor()
    cur.execute("SELECT * FROM Cliente")
    user_data = cur.fetchall()
    clientList = []
    for row in user_data:
        objecClient = Cliente(row)
        clientList.append(objecClient.to_json())
    
    return jsonify(clientList)


@app.route('/login/clientes/<int:cliente_id>', methods=['GET'])
def get_client_by_id(cliente_id):
    cur = mysql.cursor()
    cur.execute('SELECT * FROM Cliente WHERE cliente_id = %s', (cliente_id))
    data = cur.fetchone()
    clientList = []
    for row in data:
        objecClient = Cliente(row)
        clientList.append(objecClient.to_json())
    
    return jsonify(clientList)


@app.route('/login/cliente/<int:cliente_id>', methods=['PUT'])
def update_cliente_by_id(cliente_id):
    nombre = request.get_json()["nombre"]
    apellido = request.get_json()["apellido"]
    dni = request.get_json()["dni"]
    email = request.get_json()['email']
    telefono = request.get_json()['telefono']

    cur = mysql.cursor()
    cur.execute('UPDATE Cliente SET nombre = %s, apellido = %s, dni = %s, email = %s, telefono = %s WHERE cliente_id = %s', (nombre, apellido, dni, email, telefono, cliente_id))
    mysql.commit()
    return jsonify({'nombre': nombre, 'apellido': apellido, "dni": dni, "email": email, "telefono": telefono})


# LLAMAR A LOS CLIENTES POR SU ID
@app.route('/clientes/<int:usuario_id>', methods=['GET'])
def get_all_client_by_id(usuario_id):
    cur = mysql.cursor()
    cur.execute('SELECT apellido, nombre, dni, email, telefono, fechaNac FROM Cliente WHERE usuario_id = {}'.format(usuario_id))
    datas = cur.fetchone()
    print(datas)

    
    return jsonify({'Bien'})