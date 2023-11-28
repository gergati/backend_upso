from api import app
import mysql.connector
from api.models.usuario import Usuario
from flask import jsonify, render_template, request, flash

# LLAMAR A TODOS LOS USUARIOS
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['nombre']
        password = request.form['contraseña']
        

        cur = mysql.cursor()
        cur.execute("SELECT usuario_id FROM Usuario WHERE nombre = %s AND contraseña = %s", (username, password,))
        user_data = cur.fetchone()
        print(user_data)


        cur = mysql.cursor()
        cur.execute('SELECT apellido, nombre, dni, email, telefono, fechaNac FROM Cliente WHERE usuario_id = {}'.format(user_data[0]))
        data_client = cur.fetchall()
        print(data_client)

        if user_data:
            # Usuario autenticado correctamente
            
            return render_template('/dashboard.html', user_data=user_data, data_client=data_client)
        else:
            # Usuario no autenticado
            
            return render_template('auth/login.html')

    return render_template('auth/login.html')

# CREAR NUEVOS USUARIOS
@app.route('/usuarios', methods=['POST'])
def create_user():
    nombre = request.get_json()['nombre']
    apellido = request.get_json()['apellido']
    dni = request.get_json()['dni']
    email = request.get_json()['email']
    telefono = request.get_json()['telefono']
    contraseña = request.get_json()['contraseña']

    cur = mysql.cursor()
    cur.execute('SELECT * FROM Usuario WHERE email = %s',(email))
    row = cur.fetchone()
    if row:
        return jsonify({'Message': 'Email ya registrado'})
    
    cur.execute('INSERT INTO Usuario (nombre,apellido,dni,email,telefono, contraseña) VALUES (%s,%s,%s,%s,%s)', (nombre, apellido, dni, email, telefono, contraseña))
    mysql.commit()
    nuevo = cur.fetchone()
    id = nuevo[0]
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


# LLAMAR A LOS CLIENTES POR SU ID
@app.route('/clientes/<int:usuario_id>', methods=['GET'])
def get_all_client_by_id(usuario_id):
    cur = mysql.cursor()
    cur.execute('SELECT apellido, nombre, dni, email, telefono, fechaNac FROM Cliente WHERE usuario_id = {}'.format(usuario_id))
    datas = cur.fetchone()
    print(datas)

    
    return render_template('/clientes.html', datas=datas)
