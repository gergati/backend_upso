from flask import jsonify, request
from api import app
from api.db.db import mysql
from api.models.servicio import Servicio
from datetime import datetime 
from api.utils import user_resources, token_required


# TRAER TODOS LOS SERVICIOS 
@app.route('/usuario/<int:usuario_id>/servicios', methods=['GET'])
@token_required
@user_resources
def traer_servicios(usuario_id):
    cur = mysql.cursor()
    cur.execute('SELECT * fROM servicio WHERE usuario_id = %s', (usuario_id,))
    data = cur.fetchall()
    mysql.commit()
    clientList = []
    for row in data:
        objecClient = Servicio(row)
        clientList.append(objecClient.to_json())
    return jsonify(clientList)

# TRAER UN SERVICIO POR ID
@app.route('/usuario/<int:usuario_id>/servicios/<int:servicio_id>', methods=['GET'])
@token_required
@user_resources
def servicio_por_id(usuario_id,servicio_id):
    cur = mysql.cursor()
    cur.execute('SELECT * FROM servicio WHERE servicio_id = %s AND usuario_id = %s',(servicio_id, usuario_id))
    data = cur.fetchone()
    mysql.commit()
    if data == None:
        return jsonify({'No existe el servicio con el id': servicio_id})
    else:
        return jsonify({
            'Id del servicio': data[0],
            'Id del usuario': data[1],
            'Servicio realizado': data[2],
            'fecha': data[3].strftime('%Y-%m-%d'),
            'hora': str(data[4])
            })

# CAMBIAR DATOS DE UN SERVICIO POR ID
@app.route('/usuario/<int:usuario_id>/servicios/<int:servicio_id>', methods=['PUT'])
@token_required
@user_resources
def cambiar_servicio_por_id(usuario_id, servicio_id):
    usuario_id = request.get_json()['usuario_id']
    nombreServicio = request.get_json()['nombreServicio']
    fecha = request.get_json()['fecha']
    hora = request.get_json()['hora']

    cur = mysql.cursor()
    cur.execute('UPDATE Servicio SET usuario_id = %s, nombreServicio = %s, fecha = %s, hora = %s WHERE servicio_id = %s',(usuario_id, nombreServicio, fecha, hora ,servicio_id))
    mysql.commit()
    return jsonify({
        'Id del servicio': servicio_id,
        'Id del usuario': usuario_id,
        'Servicio realizado': nombreServicio,
        'fecha': fecha,
        'hora': hora,
    })

# CREAR NUEVOS SERVICIOS
@app.route('/servicios', methods=['POST'])
def crear_servicios():
    usuario_id = request.get_json()['usuario_id']
    nombreServicio = request.get_json()['nombreServicio']
    fecha = request.get_json()['fecha']
    hora = request.get_json()['hora']

    cur = mysql.cursor()
    cur.execute('INSERT INTO Servicio (usuario_id, nombreServicio, fecha, hora) VALUES (%s, %s, %s, %s)',(usuario_id, nombreServicio, fecha, hora))
    mysql.commit()
    return jsonify({
        'Id del usuario': usuario_id,
        'Servicio realizado': nombreServicio,
        'fecha': fecha,
        'hora': hora,
    })


# ELIMINAR UN SERVICIO POR ID
@app.route('/usuario/<int:usuario_id>/servicios/<int:servicio_id>', methods=['DELETE'])
@token_required
@user_resources
def eliminar_servicio(usuario_id,servicio_id):
    cur = mysql.cursor()
    cur.execute('DELETE FROM Servicio WHERE servicio_id = %s AND usuario_id = %s', (servicio_id,usuario_id))
    mysql.commit()
    return jsonify({'Servicio eliminado con id': servicio_id})



    