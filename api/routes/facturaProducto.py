from flask import request,jsonify
from api.db.db import mysql
from api import app
from api.models.factura_producto import FacturaProducto
from api.utils import token_required, user_resources

# MOSTRAR TODAS LAS FACTURAS DE UN USUARIO DETERMINADO
@app.route('/usuario/<int:usuario_id>/facturaProd', methods=['GET'])
@token_required
@user_resources
def factura_productos(usuario_id):
    cur = mysql.cursor()
    cur.execute('SELECT f.facturaProd_id, u.usuario_id, u.nombre, p.producto_id, p.nombreProd, p.marca, p.precio, p.cantidad, p.descripcion FROM FacturaProducto f JOIN Usuario u ON f.usuario_id = u.usuario_id JOIN Producto p ON f.producto_id = p.producto_id WHERE u.usuario_id = %s', (usuario_id,))
    data = cur.fetchall()
    productosLista = []
    for row in data:
        factura = {
            'factProd_id': row[0],
            'usuario':{
                'usuario_id': usuario_id,
                'nombre': row[2],
            },
            'producto':{
                'producto_id': row[3],
                'nombreProd': row[4],
                'marca': row[5],
                'precio': row[6],
                'cantidad': row[7],
                'descripción': row[8],
            },
        }
        productosLista.append(factura)
    return jsonify(productosLista)

# MOSTRAR UNA FACTURA DE UN PRODUCTO A TRAVES DE UN ID
@app.route('/usuario/<int:usuario_id>/facturaProd/<int:facturaProd_id>', methods=['GET'])
@token_required
@user_resources
def factura_productos_por_id(usuario_id, facturaProd_id):
    cur = mysql.cursor()
    cur.execute('SELECT f.facturaProd_id, u.usuario_id, u.nombre, p.producto_id, p.nombreProd, p.marca, p.precio, p.cantidad, p.descripcion FROM FacturaProducto f JOIN Usuario u ON f.usuario_id = u.usuario_id JOIN Producto p ON f.producto_id = p.producto_id WHERE u.usuario_id = %s AND f.facturaProd_id = %s', (usuario_id, facturaProd_id))
    data = cur.fetchone()
    if data is not None:
        factura = {
            'factProd_id': data[0],
            'usuario':{
                'usuario_id': usuario_id,
                'nombre': data[2],
            },
            'producto':{
                'producto_id': data[3],
                'nombreProd': data[4],
                'marca': data[5],
                'precio': data[6],
                'cantidad': data[7],
                'descripción': data[8],
            },
        }
        
        return jsonify(factura)
    else:
        return jsonify({'error': 'Factura no encontrada'}), 404


# CREAR UNA NUEVA FACTURA DEL PRODUCTO
@app.route('/facturaProd', methods=['POST'])
def crear_factura():
    producto_id = request.get_json()['producto_id']
    usuario_id = request.get_json()['usuario_id']

    cur = mysql.cursor()
    cur.execute('INSERT INTO facturaproducto (producto_id, usuario_id) VALUES (%s, %s)', (producto_id, usuario_id))
    mysql.commit()
    return jsonify({'producto_id':producto_id, 'usuario_id': usuario_id})


#CAMBIAR DATOS A TRAVES DE SU ID
@app.route('/usuario/<int:usuario_id>/facturaProd/<int:facturaProd_id>', methods=['PUT'])
@token_required
@user_resources
def actualizar_facturaProd(usuario_id, facturaProd_id):
    data = request.get_json()
    if not data or 'producto_id' not in data:
        return jsonify({'error': 'Datos incompletos o incorrectos'}), 400

    nuevo_producto_id = data['producto_id']

    cur = mysql.cursor()
    cur.execute('SELECT usuario_id FROM FacturaProducto WHERE facturaProd_id = %s', (facturaProd_id,))
    factura = cur.fetchone()

    if not factura or factura[0] != usuario_id:
        return jsonify({'error': 'La factura de producto no pertenece al usuario especificado'}), 404

    cur.execute('UPDATE FacturaProducto SET producto_id = %s WHERE facturaProd_id = %s', (nuevo_producto_id, facturaProd_id))
    mysql.commit()

    return jsonify({'facturaProd_id': facturaProd_id, 'nuevo_producto_id': nuevo_producto_id, 'usuario_id': usuario_id})


# ELIMINAR UNA FACTURA POR UN ID
@app.route('/usuario/<int:usuario_id>/facturaProd/<int:facturaProd_id>', methods=['DELETE'])
def eliminar_factura(facturaProd_id):
    cur = mysql.cursor()
    cur.execute('DELETE FROM facturaproducto WHERE facturaProd_id = {}'.format(facturaProd_id))
    mysql.commit()
    return ({'Factura del producto eliminado con id': facturaProd_id})