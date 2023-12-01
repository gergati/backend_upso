from flask import jsonify, request
from api import app
from api.db.db import mysql
from api.models.servicio import Servicio
from datetime import datetime 

# TRAER TODOS LOS SERVICIOS 
@app.route('/servicios', methods=['GET'])
def traer_servicios():
    cur = mysql.cursor()
    cur.execute('SELECT * fROM servicio')
    data = cur.fetchall()
    mysql.commit()
    clientList = []
    for row in data:
        objecClient = Servicio(row)
        clientList.append(objecClient.to_json())
    return jsonify(clientList)

# TRAER UN SERVICIO POR ID
@app.route('/servicios/<int:servicio_id>', methods=['GET'])
def servicio_por_id(servicio_id):
    cur = mysql.cursor()
    cur.execute('SELECT * FROM servicio WHERE servicio_id = {}'.format(servicio_id))
    data = cur.fetchone()
    mysql.commit()
    return jsonify({
        'Id del servicio': data[0],
        'Id del usuario': data[1],
        'Servicio realizado': data[2],
        'fecha': data[3].strftime('%Y-%m-%d'),
        'hora': str(data[4])
        })

# CAMBIAR DATOS DE UN SERVICIO POR ID
@app.route('/servicios/<int:servicio_id>', methods=['PUT'])
def cambiar_servicio_por_id(servicio_id):
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
@app.route('/servicios/<int:servicio_id>', methods=['DELETE'])
def eliminar_servicio(servicio_id):
    cur = mysql.cursor()
    cur.execute('DELETE FROM Servicio WHERE servicio_id = %s', (servicio_id,))
    return jsonify({'Servicio eliminado con id': servicio_id})



    