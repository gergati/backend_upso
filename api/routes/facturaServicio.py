from flask import request, jsonify
from api import app
from api.db.db import mysql
from datetime import timedelta
from api.models.factura_servicio import FacturaServicio


# TRAER TODAS LAS FACTURAS DEL SERVICIO
@app.route('/usuario/<int:usuario_id>/facturaServicio', methods=['GET'])
def factura_servicio(usuario_id):
    cur = mysql.cursor()
    cur.execute('SELECT f.facturaServicio_id, f.servicio_id, s.servicio_id, s.nombreServicio, s.cliente_id s.hora, u.usuario_id, u.nombre, u.apellido, u.dni, u.email, u.telefono, u.tipo FROM FacturaServicio f JOIN Servicio s ON f.servicio_id = s.servicio_id JOIN Usuario u ON f.facturaServicio_id = u.usuario_id WHERE u.usuario_id = %s', (usuario_id,))
    data = cur.fetchall()
    productosLista = []
    for row in data:
        factura = {
        'facturaServicio_id': row[0],
            'servicio': {
                'servicio_id': row[1],
                'usuario_id': row[2],
                'nombreServicio': row[3],
                'cliente': row[4],
                'hora': str(row[5]),  # Convertir timedelta a string
            },
            'usuario': {
                'usuario_id': row[6],
                'nombre': row[7],
                'apellido': row[8],
                'dni': row[9],
                'email': row[10],
                'telefono': row[11],
                'tipo': row[12],
            },
        }
        productosLista.append(factura)
    return jsonify(productosLista)



@app.route('/facturaServicio/<int:facturaServicio_id>', methods=['GET'])
def buscar_prodServ_por_id(facturaServicio_id):
    cur = mysql.cursor()

    cur.execute('SELECT * FROM facturaservicio WHERE facturaServicio_id'.format(facturaServicio_id,))
    data = cur.fetchone()
    print(data)
    if data[0] == None:
        return jsonify({'No existe la factura con id': facturaServicio_id})
    
    """ else:
        cur.execute('SELECT f.facturaServicio_id, f.servicio_id, s.servicio_id, s.nombreServicio, s.hora, u.usuario_id, u.nombre, u.apellido, u.dni, u.email, u.telefono, u.tipo FROM FacturaServicio f JOIN Servicio s ON f.servicio_id = s.servicio_id JOIN Usuario u ON f.facturaServicio_id = u.usuario_id')
        data = cur.fetchone()
        productosLista = []
        for row in data:
            factura = {
            'facturaServicio_id': row[0],
                'servicio': {
                    'servicio_id': row[1],
                    'usuario_id': row[2],
                    'nombreServicio': row[3],
                    'hora': str(row[4]), 
                },
                'usuario': {
                    'usuario_id': row[5],
                    'nombre': row[6],
                    'apellido': row[7],
                    'dni': row[8],
                    'email': row[9],
                    'telefono': row[10],
                    'categoria de monotributo': row[11],
                },
            }
            productosLista.append(factura) """
    return jsonify(data)

# CREAR NUEVAS FACTURAS DE UN SERVICIO
@app.route('/facturaServicio', methods=['POST'])
def crear_factura_servicio():
    facturaServicio_id = request.get_json()['facturaServicio_id']
    servicio_id = request.get_json()['servicio_id']

    cur = mysql.cursor()
    cur.execute('INSERT INTO facturaservicio (facturaServicio_id,servicio_id) VALUES (%s, %s)', (facturaServicio_id,servicio_id,))
    cur.fetchone()
    return jsonify({'facturaServicio_id': facturaServicio_id,'servicio_id': servicio_id})



