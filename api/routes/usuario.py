from flask import jsonify, request
from api import app
from api.db.db import mysql
from api.models.usuario import Usuario


# LLAMAR A TODOS LOS USUARIOS
@app.route('/', methods=['GET'])
def login():

    cur = mysql.cursor()
    cur.execute('SELECT * FROM Usuario')
    data_client = cur.fetchall()
    print(data_client)

    if data_client:
            # Usuario autenticado correctamente
            
        return jsonify(data_client)
    else:
            # Usuario no autenticado
            
        return jsonify('No correcto')


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
    
    cur.execute('INSERT INTO Usuario (nombre,apellido,dni,email,telefono, contraseña, tipo) VALUES (%s,%s,%s,%s,%s,%s, %s)', (nombre, apellido, dni, email, telefono, contraseña, tipo))
    mysql.commit()
    nuevo = cur.fetchone()
    id = nuevo
    return jsonify({'usuario creado correctamente:', id})


# CAMBIAR DATOS DE USUARIO
@app.route('/usuarios/<int:usuario_id>', methods=['PUT'])
def update_person(usuario_id):
    nombre = request.get_json()["nombre"]
    apellido = request.get_json()["apellido"]
    dni = request.get_json()["dni"]
    email = request.get_json()["email"]
    telefono = request.get_json()['telefono']

    #UPDATE SET .... WHERE .....
    cur = mysql.cursor()
    cur.execute('UPDATE Usuario SET nombre = %s, apellido = %s, dni= %s, email = %s, telefono = %s WHERE usuario_id = %s', (nombre, apellido, dni, email, telefono, usuario_id))
    mysql.commit()
    return jsonify({'name': nombre, 'surname': apellido, "dni": dni, "email": email, 'telefono': telefono})

