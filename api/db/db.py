#import app
from app import app
import mysql.connector


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'api_ventas_upso'
app.config['MYSQL_PASSWORD'] = 'upso123'
app.config['MYSQL_DB'] = 'AdminTotal'


mysql = mysql.connector.connect(
    host='localhost',
    user='api_ventas_upso',
    password='upso123',
    database='AdminTotal'
)