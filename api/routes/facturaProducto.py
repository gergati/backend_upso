from flask import request,jsonify
from api.db.db import mysql
from api import app
from api.models.factura_producto import FacturaProducto


@app.route('/facturaProd', methods=['GET'])
def factura_productos():
    cur = mysql.cursor()
    cur.execute('SELECT f.facturaProd_id, u.usuario_id, u.nombre, p.producto_id, p.nombreProd, p.marca, p.precio, p.cantidad, p.descripcion FROM FacturaProducto f JOIN Usuario u ON f.usuario_id = u.usuario_id JOIN Producto p ON f.producto_id = p.producto_id')
    data = cur.fetchall()
    productosLista = []
    for row in data:
        factura = {
            'factProd_id': row[0],
            'usuario':{
                'usuario_id': row[1],
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
@app.route('/facturaProd/<int:facturaProd_id>', methods=['PUT'])
def actualizar_facturaProd(facturaProd_id):
    producto_id = request.get_json()['producto_id']
    usuario_id = request.get_json()['usuario_id']
    cur = mysql.cursor()
    cur.execute('UPDATE facturaproducto SET producto_id = %s, usuario_id = %s WHERE facturaProd_id = %s', (producto_id, usuario_id, facturaProd_id))
    mysql.commit()
    return jsonify({'facturaProd_id': facturaProd_id, 'producto_id': producto_id, 'usuario_id': usuario_id})

# ELIMINAR UNA FACTURA POR UN ID
@app.route('/facturaProd/<int:facturaProd_id>', methods=['DELETE'])
def eliminar_factura(facturaProd_id):
    cur = mysql.cursor()
    cur.execute('DELETE FROM facturaproducto WHERE facturaProd_id = {}'.format(facturaProd_id))
    mysql.commit()
    return ({'Factura del producto eliminado con id': facturaProd_id})