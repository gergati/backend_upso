from flask import request, jsonify
from api import app
from api.db.db import mysql
from datetime import timedelta
from api.models.factura_servicio import FacturaServicio
from api.utils import token_required, user_resources


# TRAER TODAS LAS FACTURAS DEL SERVICIO
@app.route('/usuario/<int:usuario_id>/facturaServicio', methods=['GET'])
@token_required
@user_resources
def factura_servicio(usuario_id):
    cur = mysql.cursor()
    cur.execute('SELECT f.facturaServicio_id, f.servicio_id, s.nombreServicio,s.servicio_id, s.fecha, s.hora FROM FacturaServicio f JOIN Servicio s ON f.servicio_id = s.servicio_id WHERE s.usuario_id = %s', (usuario_id,))
    data = cur.fetchall()
    productosLista = []
    #return jsonify({'message': data[0]})
    for row in data:
        factura = {
            'facturaServicio_id': row[0],
            'servicio': {
                'servicio_id': row[1],
                'nombreServicio': row[2],
                'nombreServicio': row[3],
                'fecha': row[4],
                'hora': str(row[5]),
            }
        }
    productosLista.append(factura)

    return jsonify(productosLista)


# TRAER LAS FACTURAS DEL SERVICIO SEGUN ID
@app.route('/usuario/<int:usuario_id>/facturaServicio/<int:facturaServicio_id>', methods=['GET'])
@token_required
@user_resources
def buscar_prodServ_por_id(usuario_id,facturaServicio_id):
    cur = mysql.cursor()

    cur.execute('SELECT f.facturaServicio_id, f.servicio_id, s.nombreServicio,s.servicio_id, s.fecha, s.hora FROM FacturaServicio f JOIN Servicio s ON f.servicio_id = s.servicio_id WHERE s.usuario_id = %s AND f.facturaServicio_id = %s', (usuario_id,facturaServicio_id))
    data = cur.fetchone()
    print(data)
    if data is None:
        return jsonify({'No existe la factura con id': facturaServicio_id})

    productosLista = []
    factura = {
        'facturaServicio_id': data[0],
        'servicio': {
            'servicio_id': data[1],
            'nombreServicio': data[2],
            'cliente_id': data[3],  
            'fecha': data[4],
            'hora': str(data[5]),
        }
    }
    productosLista.append(factura)
    
    return jsonify(productosLista)

# CREAR NUEVAS FACTURAS DE UN SERVICIO
@app.route('/facturaServicio', methods=['POST'])
def crear_factura_servicio():
    facturaServicio_id = request.get_json()['facturaServicio_id']
    servicio_id = request.get_json()['servicio_id']

    cur = mysql.cursor()
    cur.execute('INSERT INTO facturaservicio (facturaServicio_id,servicio_id) VALUES (%s, %s)', (facturaServicio_id,servicio_id,))
    cur.fetchone()
    return jsonify({'facturaServicio_id': facturaServicio_id,'servicio_id': servicio_id})


# CAMBIAR DATOS DE UNA FACTURA DE SERVICIO CON EL ID
@app.route('/usuario/<int:usuario_id>/facturaServicio/<int:facturaServicio_id>', methods=['PUT'])
@token_required
@user_resources
def cambiar_datos_factura(usuario_id, facturaServicio_id):
    data = request.get_json()

    if not data or 'servicio_id' not in data:
        return jsonify({'error': 'Datos incompletos o incorrectos'}), 400

    usuario_id = data['usuario_id']

    cur = mysql.cursor()
    cur.execute('SELECT usuario_id FROM Producto WHERE producto_id = %s', (facturaServicio_id,))
    factura = cur.fetchone()

    if not factura or factura[0] != usuario_id:
        return jsonify({'Message': 'El producto no pertenece al usuario especificado'}), 404

    cur = mysql.cursor()
    cur.execute('SELECT f.facturaServicio_id, f.servicio_id, s.nombreServicio,s.servicio_id, s.fecha, s.hora FROM FacturaServicio f JOIN Servicio s ON f.servicio_id = s.servicio_id WHERE s.usuario_id = %s AND f.facturaServicio_id = %s', (usuario_id, facturaServicio_id))
    data = cur.fetchone()

    productosLista = []
    factura = {
        'facturaServicio_id': data[0],
        'servicio': {
            'servicio_id': data[1],
            'nombreServicio': data[2],
            'cliente_id': data[3],  
            'fecha': data[4],
            'hora': str(data[5]),
        }
    }
    productosLista.append(factura)
    
    return jsonify(productosLista) 


# ELIMINAR UNA FACTURA POR ID
@app.route('/usuario/<int:usuario_id>/facturaServicio/<int:facturaServicio_id>', methods=['DELETE'])
@token_required
@user_resources
def eliminar_facturas_srevicio(usuario_id,facturaServicio_id):
    cur = mysql.cursor()
    cur.execute('DELETE FROM facturaservicio WHERE facturaServicio_id = %s AND usuario_id = %s', (facturaServicio_id, usuario_id))
    mysql.commit()
    return jsonify({'Eliminamos el producto con el id': facturaServicio_id})