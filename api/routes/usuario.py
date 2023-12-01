from flask import jsonify, request
from api import app
from api.db.db import mysql
from api.models.usuario import Usuario


# LLAMAR A TODOS LOS USUARIOS
@app.route('/', methods=['GET'])
def usuario():
    cur = mysql.cursor()
    cur.execute('SELECT * FROM Usuario')
    data_usuario = cur.fetchall()
    usuarioLista = []
    for row in data_usuario:
        objectUsuario = Usuario(row)
        usuarioLista.append(objectUsuario.to_json())
        # Usuario autenticado correctamente
    return jsonify(usuarioLista)

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