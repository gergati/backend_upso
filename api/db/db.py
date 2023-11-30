from api import app
import mysql.connector

mysql = mysql.connector.connect(
    host='localhost',
    user='NicoAdministraciones',
    password='nico123',
    database='nicoadministraciones'
)