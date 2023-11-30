from api import app
from api.db.db import mysql
from flask import request, jsonify
from datetime import datetime
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


# BUSCAR CLIENTES POR ID
@app.route('/clientes/<int:cliente_id>', methods=['GET'])
def get_client_by_id(cliente_id):
    cur = mysql.cursor()
    cur.execute('SELECT * FROM Cliente WHERE cliente_id = {}'.format(cliente_id))
    data = cur.fetchone()

    if data == None:
        return jsonify({'No existe el cliente con id': cliente_id})
    else:
        return jsonify({
            "cliente_id": data[0],
            "usuario_id": data[1],
            "apellido": data[2],
            "nombre": data[3],
            "dni": data[4],
            "email": data[5],
            "telefono": data[6],
            "contraseña": data[7],
            "fechaNac": data[8].strftime('%Y-%m-%d')
        })

# CREAR NUEVOS USUARIOS
@app.route('/clientes', methods=['POST'])
def crear_clientes():
    usuario_id = request.get_json()['usuario_id']
    apellido = request.get_json()['apellido']
    nombre = request.get_json()['nombre']
    dni = request.get_json()['dni']
    email = request.get_json()['email']
    telefono = request.get_json()['telefono']
    contraseña = request.get_json()['contraseña']
    fechaNac = request.get_json()['fechaNac']

    cur = mysql.cursor()
    cur.execute('SELECT * FROM Cliente WHERE email = %s',(email,))
    row = cur.fetchone()
    if row:
        return jsonify({'Message': 'El email del cliente ya registrado'})
    
    else:
        cur.execute('INSERT INTO Cliente (usuario_id,nombre,apellido,dni,email,telefono, contraseña, fechaNac) VALUES (%s,%s,%s,%s,%s,%s,%s, %s)', (usuario_id,apellido, nombre, dni, email, telefono, contraseña, fechaNac))
        mysql.commit()
        cur.fetchone()
        return jsonify({'nombre': nombre, 'apellido': apellido, "dni": dni, "email": email, 'telefono': telefono, 'fechaNac': fechaNac})



# CAMBIAR DATOS DEL CLIENTE POR ID
@app.route('/clientes/<int:cliente_id>', methods=['PUT'])
def update_cliente_by_id(cliente_id):
    apellido = request.get_json()["apellido"]
    nombre = request.get_json()["nombre"]
    dni = request.get_json()["dni"]
    email = request.get_json()['email']
    telefono = request.get_json()['telefono']
    contraseña = request.get_json()['contraseña']
    fechaNac = request.get_json()['fechaNac']

    cur = mysql.cursor()
    cur.execute('UPDATE Cliente SET nombre = %s, apellido = %s, dni = %s, email = %s, telefono = %s, contraseña = %s, fechaNac = %s WHERE cliente_id = %s', (nombre, apellido, dni, email, telefono, contraseña, fechaNac, cliente_id))
    mysql.commit()
    return jsonify({'nombre': nombre, 'apellido': apellido, "dni": dni, "email": email, "telefono": telefono, "contraseña": contraseña, "fechaNac": fechaNac})


# ELIMINAR UN CLIENTE POR SU ID
@app.route('/clientes/<int:cliente_id>', methods=['DELETE'])
def eliminar_cliente_por_id(cliente_id):
    cur = mysql.cursor()
    cur.execute('SELECT cliente_id FROM Cliente WHERE cliente_id = {}'.format(cliente_id))
    row = cur.fetchone()

    if row == None:
        return jsonify({'No existe el cliente con id': cliente_id})

    else:
        cur = mysql.cursor()
        cur.execute("DELETE FROM Cliente WHERE cliente_id = {}".format(cliente_id))
        mysql.commit()
        return jsonify({'Eliminamos el cliente con el id':  cliente_id})