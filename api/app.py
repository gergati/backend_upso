from flask import Flask, jsonify
import mysql.connector
from models.cliente import Cliente
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


@app.route('/clientes', methods=['GET'])
def get_all_persons():
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


if __name__ == '__main__':
    app.run(debug=True, port=5000)