from api import app
from api.db.db import mysql
from flask import request, jsonify
from api.utils import token_required, user_resources, client_resource
import datetime
from api.models.cliente import Cliente


# TRAER TODOS LOS CLIENTES
@app.route('/usuario/<int:usuario_id>/clientes', methods=['GET'])
@token_required
@user_resources
def client(usuario_id):
    cur = mysql.cursor()
    cur.execute("SELECT * FROM Cliente WHERE usuario_id = %s", (usuario_id,))
    user_data = cur.fetchall()
    clientList = []
    for row in user_data:
        objecClient = Cliente(row)
        clientList.append(objecClient.to_json())
    return jsonify(clientList)


# BUSCAR CLIENTES POR ID
@app.route('/usuario/<int:usuario_id>/clientes/<int:cliente_id>', methods=['GET'])
@token_required
@user_resources
@client_resource
def get_client_by_id(usuario_id, cliente_id):
    cur = mysql.cursor()
    cur.execute('SELECT c.cliente_id, c.usuario_id, c.apellido, c.nombre, c.dni, c.email, c.telefono, c.contraseña, c.fechaNac, u.nombre, u.apellido, u.dni, u.email, u.telefono, u.contraseña, u.tipo FROM Cliente c JOIN Usuario u ON c.usuario_id = u.usuario_id WHERE c.cliente_id = %s AND u.usuario_id = %s', (cliente_id, usuario_id))
    data = cur.fetchone()
    print(data)
    if data is not None:
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
    else:
        return jsonify({'Message': 'Cliente no encontrado'}), 404 

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
@app.route('/usuario/<int:usuario_id>/clientes/<int:cliente_id>', methods=['PUT'])
@token_required
@user_resources
@client_resource
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
    return jsonify({
        'nombre': nombre, 
        'apellido': apellido, 
        'dni': dni, 
        "email": email, 
        "telefono": telefono, 
        "contraseña": contraseña, 
        "fechaNac": fechaNac
        })


# ELIMINAR UN CLIENTE POR SU ID
@app.route('/usuario/<int:usuario_id>/clientes/<int:cliente_id>', methods=['DELETE'])
@token_required
@user_resources
@client_resource
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