from flask import jsonify, request
from api import app
import jwt
import datetime
from api.db.db import mysql
from api.utils import token_required



# HACER LOGIN CON UN USUARIO
@app.route('/login', methods=['GET'])
def usuario():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return jsonify({'Message': 'No autorizado'}), 401 
    cur = mysql.cursor()
    cur.execute('SELECT * FROM Usuario WHERE nombre = %s AND contraseña = %s', (auth.username, auth.password))
    data_usuario = cur.fetchone()
    if not data_usuario:
        return jsonify({'Message': 'No autorizado'}), 401
    
    token = jwt.encode({
        'id': data_usuario[0],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=100)
    }, app.config['SECRET_KEY'])
    return jsonify({'token': token, 'nombre': auth.username, 'usuario_id': data_usuario[0]})


# TRAER USUARIOS SEGUN EL ID
@app.route('/usuario/<int:usuario_id>', methods=['GET'])
@token_required
def traer_usuarios_por_id(usuario_id):
    cur = mysql.cursor()
    cur.execute('SELECT * FROM Usuario WHERE usuario_id = %s', (usuario_id,))
    data = cur.fetchall()
    return jsonify({
        'usuario': data
    })


# CREAR NUEVOS USUARIOS
@app.route('/usuario', methods=['POST'])
def crear_usuario():
    nombre = request.get_json()['nombre']
    apellido = request.get_json()['apellido']
    dni = request.get_json()['dni']
    email = request.get_json()['email']
    telefono = request.get_json()['telefono']
    contraseña = request.get_json()['contraseña']
    tipo = request.get_json()['tipo']

    cur = mysql.cursor()
    cur.execute('SELECT * FROM Usuario WHERE email = %s',(email,))
    row = cur.fetchone()
    if row:
        return jsonify({'Message': 'Email ya registrado'})
    
    else:
        cur.execute('INSERT INTO Usuario (nombre,apellido,dni,email,telefono, contraseña, tipo) VALUES (%s,%s,%s,%s,%s,%s, %s)', (nombre, apellido, dni, email, telefono, contraseña, tipo))
        mysql.commit()
        cur.fetchone()
        return jsonify({'nombre': nombre, 'apellido': apellido, "dni": dni, "email": email, 'telefono': telefono, 'tipo': tipo})


# CAMBIAR DATOS DE USUARIO SEGUN SU ID
@app.route('/usuario/<int:usuario_id>', methods=['PUT'])
@token_required
def actualizar_usuario(usuario_id):
    nombre = request.get_json()["nombre"]
    apellido = request.get_json()["apellido"]
    dni = request.get_json()["dni"]
    email = request.get_json()["email"]
    telefono = request.get_json()['telefono']
    tipo = request.get_json()['tipo']

    cur = mysql.cursor()
    cur.execute('SELECT * FROM Usuario WHERE email = %s',(email,))
    row = cur.fetchone()
    if row:
        return jsonify({'Message': 'Email ya registrado'})
    
    else:
        cur = mysql.cursor()
        cur.execute('UPDATE Usuario SET nombre = %s, apellido = %s, dni= %s, email = %s, telefono = %s, tipo = %s WHERE usuario_id = %s', (nombre, apellido, dni, email, telefono, tipo, usuario_id))
        mysql.commit()
        return jsonify({'name': nombre, 'surname': apellido, "dni": dni, "email": email, 'telefono': telefono, 'tipo': tipo})

# ELIMINAR UN USUARIO SEGUN EL ID
@app.route('/usuario/<int:usuario_id>', methods=['DELETE'])
@token_required
def eliminar_usuario_por_id(usuario_id):
    cur = mysql.cursor()
    cur.execute('SELECT usuario_id FROM Usuario WHERE usuario_id = {}'.format(usuario_id))
    row = cur.fetchone()
    if row == None:
        return jsonify({'No existe el usuario con id': usuario_id})
    else:
        cur = mysql.cursor()
        cur.execute("DELETE FROM Usuario WHERE usuario_id = {}".format(usuario_id))
        mysql.commit()
        return jsonify({'Eliminamos el usuario con el id':  usuario_id})