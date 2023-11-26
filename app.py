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
        cur.execute("SELECT * FROM Usuario WHERE nombre = %s AND contraseña = %s", (username, password))
        user_data = cur.fetchone()

        if user_data:
            # Usuario autenticado correctamente
            
            return render_template('/dashboard.html', user_data=user_data)
        else:
            # Usuario no autenticado
            
            return render_template('auth/login.html')

    return render_template('auth/login.html')

@app.route('/home')  
def home():
    return render_template('/home.html')

# LLamar a los clientes
@app.route('/clientes', methods=['GET'])
def get_all_client():
    cur = mysql.cursor()
    cur.execute('SELECT * FROM Cliente')
    data = cur.fetchall()
    print(cur.rowcount)
    print(data)
    personList = []
    for row in data:
        objPerson = Cliente(row)
        personList.append(objPerson.to_json())
    #Acceso a BD -> SELECT FROM
    return jsonify(personList)

# LLama a los productos
@app.route('/productos', methods=['GET'])
def get_all_products():
    cur = mysql.cursor()
    cur.execute('SELECT * FROM Producto')
    data = cur.fetchall()
    print(cur.rowcount)
    print(data)
    personList = []
    for row in data:
        objPerson = Producto(row)
        personList.append(objPerson.to_json())
    #Acceso a BD -> SELECT FROM
    return jsonify(personList)



if __name__ == '__main__':
    app.run(debug=True, port=5000)