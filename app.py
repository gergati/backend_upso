from flask import Flask, jsonify, request, redirect, url_for, flash
import mysql.connector
from flask.templating import render_template
from api.models.usuario import Usuario
from api.models.cliente import Cliente
from api.models.producto import Producto
from flask_cors import CORS
#from api import app

app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'AdminTotal'
app.config['MYSQL_PASSWORD'] = 'admintotal123!'
app.config['MYSQL_DB'] = 'AdminTotal'


mysql = mysql.connector.connect(
    host='localhost',
    user='AdminTotal',
    password='admintotal123!',
    database='AdminTotal'
)

@app.route('/')
def index():
    return redirect(url_for('login'))

# LLamar a los usuarios
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



# LLamar a los clientes por su id
@app.route('/clientes/<int:usuario_id>', methods=['GET'])
def get_all_client_by_id(usuario_id):
    cur = mysql.cursor()
    cur.execute('SELECT apellido, nombre, dni, email, telefono, fechaNac FROM Cliente WHERE usuario_id = {}'.format(usuario_id))
    datas = cur.fetchall()
    print(datas)

    
    return render_template('/clientes.html', datas=datas)

# LLama a los productos
@app.route('/login', methods=['GET', 'POST'])
def get_all_products():
    if request.method == 'POST':
        username = request.form['nombre']
        password = request.form['contraseña']

        cur = mysql.cursor()
        cur.execute("SELECT usuario_id FROM Usuario WHERE nombre = %s AND contraseña = %s", (username, password,))
        user_data = cur.fetchone()

        if user_data:
            # Usuario autenticado correctamente
            user_id = user_data[0]

            cur.execute("SELECT * FROM Cliente WHERE usuario_id = {}".format(user_id))
            data_client = cur.fetchall()
            print(data_client)

            if data_client:
                # Cliente encontrado
                cur.execute("SELECT * FROM Producto WHERE cliente_id = {}".format(data_client))
                productos = cur.fetchall()

                product_list = []
                for producto_row in productos:
                    objProducto = Producto(producto_row)
                    product_list.append(objProducto.to_json())

                return jsonify(product_list)
            else:
                return jsonify({"error": "Usuario autenticado, pero no se encontró el cliente."})
        else:
            # Usuario no autenticado
            return jsonify({"error": "Nombre de usuario o contraseña incorrectos"})

    return render_template('auth/login.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)