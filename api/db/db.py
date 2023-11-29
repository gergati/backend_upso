from api import app
import mysql.connector


""" app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'adminTotal'
app.config['MYSQL_PASSWORD'] = 'upso123'
app.config['MYSQL_DB'] = 'admintotal'
 """

mysql = mysql.connector.connect(
    host='localhost',
    user='NicoAdministraciones',
    password='nico123',
    database='nicoadministraciones'
)